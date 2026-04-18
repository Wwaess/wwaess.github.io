"""
Main entry point for the Secure Online Retailer system.

Contains domain models, security strategies, services, controller logic,
and a CLI interface for testing authentication, ordering, and attack simulations.
"""

import hashlib
import time
import uuid


# pylint: disable=too-few-public-methods
# model/customer.py
class Customer:
    """
    Represents a customer in the online retailer system.
    """
    def __init__(self, username: str, password_hash, role="user"):
        """
        Do not store the password in plain text, only store the hash
        The hash should be generated using a secure hashing algorithm.
        When a user logs in with their password, hash the inputed password
        with the same algorithm and compare it to the stored hash
        """
        self.username = username
        self.password_hash = password_hash
        self.role = role


# model/product.py
class Product:
    """
    Represents a product in the online retailer system.
    """
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price


# model/order.py
class Order:
    """
    Represents an order placed by a customer, containing a list of products.
    """
    def __init__(self, username: str, products: list):
        self.username = username
        self.products = products # List of Product objects


# security/strategy.py
class SecurityStrategy:
    """
    This is the fallback security strategy that will be used if no
    other strategy is specified. It implements basic security measures
    such as input validation, password hashing, rate limiting, and
    logging. As such, no method here has any implementation, 
    as it is meant to be overridden by the specific strategies.
    """
    def validate_input(self, data):
        raise NotImplementedError

    def hash_password(self, password):
        raise NotImplementedError

    def apply_login_rate_limit(self, username):
        raise NotImplementedError

    def apply_request_rate_limit(self, username):
        raise NotImplementedError

    def log_event(self, event):
        raise NotImplementedError


# security/insecure_strategy.py
class InsecureStrategy:
    """
    This is an intentionally insecure strategy that does not implement any security measures.
    It is used to demonstrate the risks of not implementing proper security practices.
    """
    def validate_input(self, data):
        print(f"[InsecureStrategy] Input allowed without validation: {data}")
        return data  # No validation, allows all input

    def hash_password(self, password):
        return password  # Plain-text password, intentially bad for demonstration

    def apply_login_rate_limit(self, username):
        print(f"[InsecureStrategy] No rate limiting applied for user: {username}")
        pass  # No rate limiting, allows unlimited attempts

    def apply_request_rate_limit(self, username):
        print(f"[InsecureStrategy] No request rate limiting for {username}")
        pass  # No request rate limiting, allows unlimited requests

    def record_failure(self, username):
        pass  # No tracking of failed attempts

    def log_event(self, event):
        print(f"[InsecureStrategy] Event logged: {event}")

    def reset_failures(self, username):
        pass  # No-op for insecure strategy


# security/secure_strategy.py
class SecureStrategy:
    """
    This is a secure strategy that implements proper security measures
    such as input validation, password hashing, rate limiting, and logging.
    """
    def __init__(self):
        self.failed_attempts = {}
        self.request_counts = {}

    def validate_input(self, data):
        """Validate user input to prevent injection attacks and other malicious input."""
        if not isinstance(data, str):
            self.log_event("Invalid input type detected.")
            raise ValueError("Invalid input type")

        if any(x in data for x in ["'", "--", ";", "/*", "*/", ":"]):
            self.log_event(f"Potential injection attack blocked: {data}")
            raise ValueError("Input contains potentially malicious characters")

        self.log_event(f"Input validated successfully: {data}")
        return data

    def hash_password(self, password):
        """
        Hash the password using SHA-256.
        In a real application, you should use a stronger hashing
        algorithm with a salt, such as bcrypt or Argon2.
        """
        # We shall only store these hashes in the Customer objects, not the plain-text passwords
        return hashlib.sha256(password.encode()).hexdigest()

    def apply_login_rate_limit(self, username):
        """
        This method limits the log in attempts for a specific username
        to prevent brute force attacks.
        """
        attempts = self.failed_attempts.get(username, 0)
        if attempts >= 5:
            delay = min(2 ** (attempts - 5), 10)  # Exponential backoff with a max delay
            self.log_event(f"Rate limiting applied to user {username}. Delay: {delay}s")
            time.sleep(delay)
            raise Exception("Too many failed attempts. Please try again later.")
        self.log_event(f"Rate limiting check passed for user {username}")

    def apply_request_rate_limit(self, username):
        """
        This method can be used for other types of rate limiting,
        such as for API requests or order placements
        """
        count = self.request_counts.get(username, 0) + 1
        self.request_counts[username] = count

        if count > 10:
            delay = min(2 ** (count - 10), 10)
            self.log_event(f"DoS protection triggered for {username}: {delay}s")
            time.sleep(delay)
            raise Exception("Too many requests. Slow down.")

        self.log_event(f"Request {count} allowed for {username}")

    def record_failure(self, username):
        self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1

    def reset_failures(self, username):
        self.failed_attempts[username] = 0

    def log_event(self, event):
        print(f"[SecureStrategy] Security Event: {event}")


# services/session_manager.py
class SessionManager:
    """
    Manages user sessions, including creation, validation, and invalidation
    of session tokens.
    """
    def __init__(self):
        self.active_sessions = {}  # Storing session tokens, mapped to usernames, as a set

    def create_session(self, username):
        """Create a new session for the given username and return a session token."""
        token = str(uuid.uuid4())
        self.active_sessions[token] = username
        # This is a simple implementation. In a real application,
        # you would want to associate the token with the user's identity
        # and possibly an expiration time.
        return token

    def get_username(self, token):
        """Get the username from a session token (None if invalid)."""
        return self.active_sessions.get(token)

    def invalidate_session(self, token):
        """Invalidate a session token, effectively logging the user out."""
        # The if statement prevents KeyError if the token does not exist
        if token in self.active_sessions:
            del self.active_sessions[token]

    def invalidate_user_sessions(self, username):
        """Invalidate all sessions for a specific user, used when a user is deleted."""
        # Invalidate all sessions for a specific user
        tokens_to_invalidate = [
            token for token,
            user in self.active_sessions.items()
            if user == username
        ]
        for token in tokens_to_invalidate:
            del self.active_sessions[token]


# services/auth_service.py
class AuthService:
    """
    Handles user authentication, including login and logout processes,
    and interacts with the security strategy for validation and rate limiting.
    """
    def __init__(self, users, strategy):
        self.users = users  # dictionary of username to Customer objects
        self.strategy = strategy

    def register(self, username: str, password: str):
        """
        Register a new user with the given username and password.
        The username needs to be checked for uniqueness.
        The password should be "encoded" using the security strategy
        before storing.
        (This means that it will be plain-text in the insecure
        strategy and hashed in the secure strategy.)
        """

        if username in self.users:
            raise Exception(
                "Username already exists. Please choose a different username."
                )

        # Validate the input using the security strategy.
        # This will raise an exception if the input is invalid,
        # which should be handled by the caller.
        password = self.strategy.validate_input(password)

        password_hash = self.strategy.hash_password(password)
        self.users[username] = Customer(username, password_hash)
        self.strategy.log_event(f"User registered: {username}")

    def register_admin(self, username: str, password: str, admin_key: str):
        """
        Register a new admin user. Requires an admin key for authorization.
        """
        if admin_key != "SECRET_ADMIN_KEY":
            raise Exception("Invalid admin key. You are not authorized to create an admin.")

        if username in self.users:
            raise Exception("Username already exists. Please choose a different username.")

        password = self.strategy.validate_input(password)
        password_hash = self.strategy.hash_password(password)
        self.users[username] = Customer(username, password_hash, role="admin")
        self.strategy.log_event(f"Admin registered: {username}")

    def login(self, username: str, password: str):
        """
        Authenticate a user with the given username and password.
        The password should be "encoded" using the security strategy
        before comparing it to the stored hash.
        The security strategy should also be used to apply rate limiting
        and log events.
        """
        self.strategy.apply_login_rate_limit(username)

        user = self.users.get(username)
        password = self.strategy.validate_input(password)
        hashed_password = self.strategy.hash_password(password)

        if user is None:
            self.strategy.record_failure(username)
            # Check if we need to apply rate limiting after recording the failure
            self.strategy.apply_login_rate_limit(username)
            self.strategy.log_event(f"Login failure for: {username} (user not found)")
            return False

        # Check if the user exists and the password hash matches
        if user and user.password_hash == hashed_password:
            self.strategy.reset_failures(username)  # Reset failed attempts on successful login
            self.strategy.log_event(f"Login success: logged in as {username}")
            return True

        # If login fails, apply rate limiting and record failure
        self.strategy.apply_login_rate_limit(username)
        self.strategy.record_failure(username)
        self.strategy.log_event(f"Login failure for: {username}")
        return False

    def delete_user(self, username):
        """Delete own account or, if admin, delete any user account."""
        if username in self.users:
            del self.users[username]
            self.strategy.log_event(f"User deleted: {username}")
            return True
        return False


class Controller:
    """
    The Controller class manages the overall application logic,
    including user registration, login, order placement, and user deletion.
    It interacts with the AuthService for authentication
    and the SessionManager for session handling.
    It also uses the security strategy to enforce security measures across all operations.
    """
    def __init__(self, strategy):
        self.strategy = strategy
        self.users = {}    # dictionary of username to Customer objects
        self.orders = []    # list of Order objects
        self.sessions = SessionManager()

        self.auth_service = AuthService(self.users, self.strategy)

    def register(self, username: str, password: str):
        """Register new user with given credentials."""
        self.auth_service.register(username, password)

    def register_admin(self, username: str, password: str, admin_key: str):
        """
        Register a new admin user.
        This method requires an admin key for authorisation.
        This runs through the AuthService object.
        """
        self.auth_service.register_admin(username, password, admin_key)

    def login(self, username: str, password: str):
        """
        If the login is successful,
        create a session and return the session token.
        """
        if self.auth_service.login(username, password):
            return self.sessions.create_session(username)
        return None

    def logout(self, token):
        """Invalidate the session token to log the user out."""
        self.sessions.invalidate_session(token)

    def get_username_from_token(self, token):
        return self.sessions.active_sessions.get(token)

    def place_order(self, token, products):
        """
        Place an order for the user associated with the given session token.
        This method should check if the user is authenticated,
        apply rate limiting, validate the input,
        and log the event using the security strategy.
        """

        # Get the username associated with the session token
        username = self.sessions.get_username(token)
        if not username:
            raise Exception(
                "User not authenticated. Please log in to place an order."
                )

        # Apply rate limiting
        self.strategy.apply_request_rate_limit(username)

        # Simulate input validation for each product (injection possibility)
        for product in products:
            self.strategy.validate_input(product)

        order = Order(username, products)
        self.orders.append(order)

        # Log order placement event
        self.strategy.log_event(f"Order placed by {username}: {products}")

    def delete_user(self, token, target_username):
        """
        Delete a user account, checking if the requester is authorised to do so.
        """
        # Who is making this deletion request?
        requester = self.sessions.get_username(token)
        if not requester:
            raise Exception("User not authenticated. Please log in to delete a user.")
        # Is this requester allowed to delete the target?
        requester_obj = self.users.get(requester)
        # RBAC check
        if requester_obj.role != "admin" and requester != target_username:
            self.strategy.log_event(
                f"Unauthorized deletion attempt by {requester} to delete {target_username}"
            )
            raise Exception(
                "Access denied. You can only delete your own account "
                "or you need admin privileges to delete other users."
            )

        # Perform the deletion and log the event
        success = self.auth_service.delete_user(target_username)
        if success:
            # Invalidate all sessions for the deleted user
            self.sessions.invalidate_session(target_username)
            self.strategy.log_event(f"User {target_username} deleted by {requester}")

        return success

    def view_profile(self, username):
        """
        Simulate viewing a user's profile.
        This could include sensitive information,
        so it should be protected by the security strategy.
        """
        user = self.users.get(username)
        if user:
            self.strategy.log_event(f"Profile viewed: {username}")
            return {
                "username": user.username,
                "role": user.role
            }
        return "User not found"

        # def _require_role(self, token, required_role):
        #     """
        #     Helper method to check if the user associated
        #     with the session token has the required role.
        #     """
        #     username = self.sessions.get_username(token)
        #     if not username:
        #         raise Exception("User not authenticated.")

        #     user = self.users.get(username)
        #     if not user or user.role != required_role:
        #         raise Exception("Access denied. Insufficient permissions.")

        #     return username

    def set_secure_mode(self, enable_secure_mode):
        """
        Dynamically switch the security strategy based on the enable_secure_mode flag.
        """
        if enable_secure_mode:
            self.strategy = SecureStrategy()
        else:
            self.strategy = InsecureStrategy()

        # Update the AuthService with the new strategy
        self.auth_service.strategy = self.strategy

    def simulate_dos_attack(self, token):
        """
        Simulate a DoS attack by making multiple rapid requests to the place_order method.
        This should trigger the rate limiting in the secure strategy.
        """
        username = self.sessions.get_username(token)
        if not username:
            raise Exception("User not authenticated. Please log in to simulate a DoS attack.")

        self.strategy.log_event(f"Simulating DoS attack initiated by {username}")
        print("Simulating DoS attack with rapid order placements...")

        for i in range(20):
            try:
                self.place_order(token, {f"Product {i}"})
                print(f"Order {i+1}: SUCCESS.")
            except Exception as e:
                print(f"Order {i+1} BLOCKED: {e}")
                break  # Stop the attack after the first block to avoid spamming the console

        self.strategy.log_event(f"Simulating DoS attack completed for {username}")

    def simulate_injection_attack(self, token):
        """
        Simulate an injection attack by attempting to place an order with malicious input.
        This should trigger the input validation in the secure strategy.
        """
        username = self.sessions.get_username(token)
        if not username:
            raise Exception(
                "User not authenticated. "
                "Please log in to simulate an injection attack.")

        self.strategy.log_event(f"Simulating injection attack initiated by {username}")
        print("Simulating injection attack with malicious input...")

        # This input is designed to look like an SQL injection attempt.
        # In a real application, this could be something
        # that tries to manipulate a database query.
        malicious_input = "Product1; DROP TABLE users; --"
        try:
            self.place_order(token, {malicious_input})
            print("Order placed with malicious input - this should not happen in secure mode!")
        except Exception as e:
            print(f"Injection attack blocked: {e}")

        self.strategy.log_event(f"Simulating injection attack completed for {username}")


# ==============================
# CLI for testing the application
# ==============================


secure_mode = True  # Default to secure mode


def run_cli():
    """
    Run a simple command-line interface to interact with the Controller and test the application.
    This CLI allows you to register users, log in, place orders, view profiles,
    and simulate attacks.
    """
    global secure_mode
    controller = Controller(SecureStrategy() if secure_mode else InsecureStrategy())
    session_token = None

    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Place Order")
        print("4. View Profile")
        print("5. Logout")
        print("6. Delete User")
        print("7. Simulate Brute Force Attack")
        print("8. Simulate DoS Attack")
        print("9. Simulate Injection Attack")
        print("10. Register Admin")
        print(
            f"11. Toggle Secure Mode (Currently: "
            f"{'Secure' if secure_mode else 'Insecure'} Mode)"
            )
        print("12. Exit")

        choice = input("> ")

        # Handle user input and call the appropriate controller methods
        # This is done in a try-except block to catch any exceptions
        # raised by the security strategy.
        try:
            if choice == "1":
                # Register a new user
                u = input("Username: ")
                p = input("Password: ")
                controller.register(u, p)
                print("User registered successfully.")

            elif choice == "2":
                # Log in as an existing user
                u = input("Username: ")
                p = input("Password: ")
                token = controller.login(u, p)

                # Check for successful login and track token if needed
                if token:
                    current_user = u
                    session_token = token
                    print(f"Login successful. Hello, {u}!")
                else:
                    print("Login failed.")

            elif choice == "3":
                # Place an order for a user, assuming they are logged in

                # Check if logged in
                if not session_token:
                    print("Please log in to place an order.")
                    continue

                # Simulate placing an order with product names as input
                items_input = input("Enter products to order (comma-separated): ")
                items = {item.strip() for item in items_input.split(",")}

                controller.place_order(session_token, items)
                print(f"Order placed for {controller.get_username_from_token(session_token)}:")
                for item in items:
                    print(f"- {item}")

            elif choice == "4":
                # View the profile of the logged-in user
                if not session_token:
                    print("Please log in to view your profile.")
                    continue

                profile = controller.view_profile(current_user)
                print("Profile Information:")
                for key, value in profile.items():
                    print(f"{key}: {value}")

            elif choice == "5":
                # Log out the current user
                if session_token:
                    controller.logout(session_token)
                    print("Logged out successfully.")
                    session_token = None
                    current_user = None
                else:
                    print("No user is currently logged in.")

            elif choice == "6":
                # Delete the current user's account
                if not session_token:
                    print("No user is currently logged in. Please log in to delete your account.")
                    continue

                user_obj = controller.users.get(current_user)

                # Admin flow:
                if user_obj.role == "admin":
                    target_username = input("Enter the username of the account to delete: ")
                else:
                    target_username = current_user
                    # Regular users can only delete their own account

                confirmation = input(
                    f"Are you sure you want to delete the account for {target_username}? (y/n): "
                    ).lower()
                if confirmation == "y":
                    controller.delete_user(session_token, target_username)
                    print("Account deleted successfully.")
                    session_token = None
                    current_user = None
                else:
                    print("Account deletion cancelled. Your account is safe.")

            # ==============================
            # Attack simulations
            # ==============================

            elif choice == "7":
                # Simulate a brute force attack by attempting multiple logins 
                # with wrong passwords
                print("Simulating brute force attack...")
                success = False

                for i in range(10):
                    try:
                        attempt_password = f"wrongpassword{i}"
                        result = controller.login("admin", attempt_password)
                        print(
                            f"Attempt {i+1}: Login attempt with wrong password - "
                            f"{'SUCCESS' if result else 'FAILURE'}"
                            )
                        if result:
                            success = True
                            break
                    except Exception as e:
                        print(f"Attempt {i + 1}: BLOCKED ({e})")
                        break

                if not success:
                    print("Brute force attack failed - blocked successfully.")

                time.sleep(0.5)  # Short delay between attempts

            elif choice == "8":
                # Simulate a DoS attack
                if not session_token:
                    print(
                        "Please log in as an admin to simulate a DoS attack."
                        )
                    continue

                controller.simulate_dos_attack(session_token)

            elif choice == "9":
                # Simulate an injection attack
                if not session_token:
                    print(
                        "Please log in as an admin to simulate an injection attack."
                        )
                    continue

                controller.simulate_injection_attack(session_token)

            elif choice == "10":
                # Register a new admin user
                admin_key = input("Enter admin key: ")
                u = input("Admin Username: ")
                p = input("Admin Password: ")
                controller.register_admin(u, p, admin_key)
                print("Admin registered successfully.")

            elif choice == "11":
                # Toggle secure mode
                secure_mode = not secure_mode
                controller.set_secure_mode(secure_mode)
                print(
                    f"Secure mode is now {'ON' if secure_mode else 'OFF'}"
                    )

            elif choice == "12":
                # Exit the application
                print("Exiting...")
                break

        except Exception as e:
            print("Error encountered: ", e)


if __name__ == "__main__":
    run_cli()
