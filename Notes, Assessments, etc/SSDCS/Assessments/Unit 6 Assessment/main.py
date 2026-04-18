import hashlib
import os
import time
import re
import uuid
from typing import Dict, List, Set


# ==============================
# Security Configuration
# ==============================

class SecurityConfig:
    def __init__(self, secure_mode: bool = True):
        self.secure_mode = secure_mode
        self.max_attempts = 3
        self.lockout_time = 10  # seconds
        self.rate_limit_window = 5  # seconds
        self.max_requests_per_window = 5


# ==============================
# Models (MVC - Model Layer)
# ==============================

class Customer:
    def __init__(self, username: str, password: str, role: str = "user"):
        self.username = username
        self.salt = os.urandom(16)
        self.password_hash = self._hash_password(password)
        self.role = role
        self.failed_attempts = 0
        self.locked_until = 0

    def _hash_password(self, password: str) -> bytes:
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.salt,
            100000
        )

    def verify_password(self, password: str) -> bool:
        test_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self.salt,
            100000
        )
        return test_hash == self.password_hash


class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer: Customer):
        self.order_id = str(uuid.uuid4())
        self.customer = customer.username
        self.items = []
        self.total = 0.0
        self.timestamp = time.time()

    def add_item(self, product: Product):
        self.items.append(product)
        self.total += product.price


# ==============================
# Repository (Data Layer)
# ==============================

class Repository:
    def __init__(self):
        self.users: Dict[str, Customer] = {}
        self.products: Dict[str, Product] = {}
        self.orders: List[Order] = []
        self.sessions: Set[str] = set()


# ==============================
# Authentication Service
# ==============================

class AuthService:
    def __init__(self, repo: Repository, security: SecurityConfig):
        self.repo = repo
        self.security = security

    def register(self, username: str, password: str, role="user"):
        if username in self.repo.users:
            print("User already exists.")
            return

        if self.security.secure_mode:
            if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
                print("Invalid username format.")
                return

        self.repo.users[username] = Customer(username, password, role)
        print("User registered successfully.")

    def login(self, username: str, password: str):
        user = self.repo.users.get(username)
        if not user:
            print("Invalid credentials.")
            return None

        if self.security.secure_mode:
            if time.time() < user.locked_until:
                print("Account locked. Try later.")
                return None

        if user.verify_password(password):
            user.failed_attempts = 0
            session_token = str(uuid.uuid4())
            self.repo.sessions.add(session_token)
            print("Login successful.")
            return session_token
        else:
            if self.security.secure_mode:
                user.failed_attempts += 1
                if user.failed_attempts >= self.security.max_attempts:
                    user.locked_until = time.time() + self.security.lockout_time
                    print("Account locked due to repeated failures.")
            print("Invalid credentials.")
            return None


# ==============================
# Payment Service (Mock Stripe)
# ==============================

class PaymentService:
    def __init__(self, security: SecurityConfig):
        self.security = security

    def process_payment(self, amount: float):
        if self.security.secure_mode:
            # Simulated tokenisation
            token = f"TOKEN-{uuid.uuid4()}"
            print(f"Payment processed securely via Stripe token: {token}")
        else:
            print(f"Payment processed (UNSAFE MODE): Card data handled locally.")
        return True


# ==============================
# Controller (Business Logic)
# ==============================

class RetailController:
    def __init__(self, repo: Repository, security: SecurityConfig):
        self.repo = repo
        self.security = security
        self.auth = AuthService(repo, security)
        self.payment = PaymentService(security)
        self.request_log = {}

    def _rate_limit(self, username: str):
        if not self.security.secure_mode:
            return True

        now = time.time()
        requests = self.request_log.get(username, [])
        requests = [r for r in requests if now - r < self.security.rate_limit_window]
        requests.append(now)
        self.request_log[username] = requests

        if len(requests) > self.security.max_requests_per_window:
            print("Rate limit exceeded. Try again later.")
            return False
        return True

    def create_product(self, product_id, name, price, user: Customer):
        if user.role != "admin":
            print("Access denied.")
            return

        self.repo.products[product_id] = Product(product_id, name, price)
        print("Product created.")

    def list_products(self):
        for p in self.repo.products.values():
            print(f"{p.product_id} | {p.name} | ${p.price}")

    def place_order(self, username: str):
        if not self._rate_limit(username):
            return

        user = self.repo.users.get(username)
        order = Order(user)

        for product in self.repo.products.values():
            order.add_item(product)

        if self.payment.process_payment(order.total):
            self.repo.orders.append(order)
            print(f"Order {order.order_id} placed successfully. Total: ${order.total}")


# ==============================
# CLI View (Presentation Layer)
# ==============================

def run_cli():
    secure_mode = input("Enable secure mode? (y/n): ").lower() == "y"
    security = SecurityConfig(secure_mode)
    repo = Repository()
    controller = RetailController(repo, security)

    # Create default admin
    controller.auth.register("admin", "Admin123", role="admin")

    session = None
    current_user = None

    while True:
        print("\n1. Register\n2. Login\n3. List Products\n4. Place Order\n5. Create Product (Admin)\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            controller.auth.register(u, p)

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            session = controller.auth.login(u, p)
            if session:
                current_user = repo.users[u]

        elif choice == "3":
            controller.list_products()

        elif choice == "4":
            if current_user:
                controller.place_order(current_user.username)
            else:
                print("Login required.")

        elif choice == "5":
            if current_user:
                pid = input("Product ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                controller.create_product(pid, name, price, current_user)
            else:
                print("Admin login required.")

        elif choice == "6":
            break


if __name__ == "__main__":
    run_cli()