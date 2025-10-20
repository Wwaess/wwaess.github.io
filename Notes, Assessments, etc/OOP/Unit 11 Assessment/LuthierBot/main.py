from time import sleep
# --- Instrument objects --

class Instrument:
    def __init__(self, name, parts):
        # Basic attributes for an instrument
        self.name = name
        self.parts = parts

    # Method to get instrument parts
    def get_parts(self):
        return self.parts

    # Method to simulate assembly process
    # -- This method is not used in the current system but could be useful for future extensions.
    def assemble(self):
        print(f"Assembling {self.name}...")
        for part in self.parts:
            print(f"  - Attaching {part}")
        print(f"{self.name} assembly complete!\n")


class Guitar(Instrument):
    def __init__(self, subtype="Generic Guitar"):
        parts = ["body", "neck", "strings", "bridge", "tuning pegs"]
        super().__init__(subtype, parts)


class Violin(Instrument):
    def __init__(self, subtype="Generic Violin"):
        parts = ["body", "neck", "strings", "fingerboard", "bridge", "tailpiece"]
        super().__init__(subtype, parts)


class Ukulele(Instrument):
    def __init__(self, subtype="Generic Ukulele"):
        parts = ["body", "neck", "strings", "bridge", "tuners"]
        super().__init__(subtype, parts)


class BassGuitar(Instrument):
    def __init__(self, subtype="Generic Bass Guitar"):
        parts = ["body", "neck", "strings", "pickups", "bridge", "tuning pegs"]
        super().__init__(subtype, parts)


class InstructionSet:
    """
    This class holds assembly instructions for various instruments.
    Each template includes an ordered list of steps to follow and the parts to collect.
    """
    def __init__(self):
        # parts that may be shared across instruments
        self.parts_catalogue = {
            "strings": ["steel strings", "nylon strings"],
            "neck": ["short neck", "long neck"],
            "body": ["acoustic body", "electric body"],
            "bridge": ["standard bridge"],
            "fingerboard": ["standard fingerboard"],
            "tailpiece": ["standard tailpiece"],
            "tuners": ["standard tuners"],
            "pickups": ["single-coil pickups", "humbucker pickups"]
        }

        self.templates = {
            "guitar": {
                "description": "Assembly instructions for an electric guitar.",
                "parts": ["steel strings", "long neck", "electric body", "bridge"],
                "steps": [
                    "Collect parts",
                    "Attach neck to body",
                    "Install bridge",
                    "Install pickups",
                    "Attach strings", 
                    "Tune the guitar"
                ],
            }, 
            "violin": {
                "description": "Assembly instructions for a violin.",
                "parts": ["nylon strings", "short neck", "acoustic body", "bridge", "tailpiece"],
                "steps": [
                    "Collect parts",
                    "Attach neck to body",
                    "Install bridge",
                    "Attach tailpiece",
                    "Attach strings",
                    "Tune the violin"
                ],
            },
            "ukulele": {
                "description": "Assembly instructions for a ukulele.",
                "parts": ["nylon strings", "short neck", "acoustic body", "bridge", "tuners"],
                "steps": [
                    "Collect parts",
                    "Attach neck to body",
                    "Install bridge",
                    "Install tuners",
                    "Attach strings",
                    "Tune the ukulele"
                ],
            },
            "bass": {
                "description": "Assembly instructions for a bass guitar.",
                "parts": ["steel strings", "long neck", "electric body", "bridge", "pickups"],
                "steps": [
                    "Collect parts",
                    "Attach neck to body",
                    "Install bridge",
                    "Install pickups",
                    "Attach strings",
                    "Tune the bass guitar"
                ],
            }
        }
    
    def get_template(self, instrument_name : str):
        """ Returns (parts, steps) for the given instrument name or None if not found."""
        template = self.templates.get(instrument_name.lower())
        if not template:
            return None, None
        parts = template["parts"] 
        # to copy this data for further, if needed - it also makes sure we don't modify the original list
        steps = template["steps"]
        return parts, steps
    
    def list_supported_instruments(self):
        """Returns a list of supported instrument names."""
        return list(self.templates.keys())



# # --- Sensor Module ---
"""This object is currently not implemented and has been left in for posterity."""
# class Sensor:
#     def __init__(self, sensor_type: str):
#         self.sensor_type = sensor_type

#     def read_data(self):
#         print(f"Reading data from {self.sensor_type} sensor")
#         return f"Data from {self.sensor_type}"


# --- Assembly Module ---
class AssemblyModule:
    def __init__(self, instruction_set):
        """
        Initializes the assembly module with the shared InstructionSet object.
        instruction_set: An instance of InstructionSet containing the assembly templates.
        """
        self.instruction_set = instruction_set

    def build_instrument(self, instrument_name):
        instrument_name = instrument_name.lower() # Normalise input

        """Handle an empty/invalid instrument name"""
        if not instrument_name:
            print("No instrument name provided.")
            return
        if not instrument_name in self.instruction_set.templates:
            print(f"\n[ERROR] Instrument '{instrument_name}' not supported.\n")
            return
        print(f"\nStarting assembly of {instrument_name.title()}...\n")

        """1 - Get the template for the requested instrument"""
        parts, steps = self.instruction_set.get_template(instrument_name)
        
        # If no template found, handle gracefully
        if not parts or not steps:
            print(f"[ERROR] No template found for '{instrument_name}'.")
            return
        
        """2 - Collect parts"""
        print("Collecting parts:")
        for part in parts:
            print(f"  - {part}")   
            sleep(0.5)  # Simulate time taken to collect each part
        
        """3 - Follow assembly steps"""
        print("\nAssembly steps:")
        for step in steps:
            print(f"- {step} - Done") 
            sleep(0.5)  # Simulate time taken for each step

        print(f"\n{instrument_name.title()} assembly complete!\n")

# class AssemblyModule:
    """Previous version of AssemblyModule without InstructionSet integration, kept for reference."""
    # def __init__(self): 
    #     # Shared and unique parts for each instrument
    #     self.parts_catalogue = {
    #         "strings": ["steel strings", "nylon strings"],
    #         "wood": ["maple", "mahogany"],
    #         "bridge": ["standard bridge"],
    #         "neck": ["short neck", "long neck"],
    #         "body": ["acoustic body", "electric body"],
    #     }

    #     # Assembly instructions for each instrument
    #     self.instructions = {
    #         "guitar": ["Collect: steel strings, long neck, electric body, bridge", "Assemble body and neck", "Attach strings"],
    #         "violin": ["Collect: nylon strings, short neck, acoustic body, bridge", "Assemble body and neck", "Attach strings"],
    #         "ukulele": ["Collect: nylon strings, short neck, acoustic body, bridge", "Assemble body and neck", "Attach strings"],
    #         "bass": ["Collect: steel strings, long neck, electric body, bridge", "Assemble body and neck", "Attach strings"]
    #     }

    # def build_instrument(self, instrument_name):
    #     print(f"\nStarting assembly of {instrument_name.title()}...\n")
    #     steps = self.instructions[instrument_name]

    #     for step in steps:
    #         print(f"- {step}")

    #     print(f"\n{instrument_name.title()} assembly complete!\n")



# --- Navigation Module ---
"""This has been replaced by NavigationSystem below, but is kept for reference."""
# class Navigation:
#     def __init__(self):
#         self.current_position = (0, 0)

#     def move_to(self, x, y):
#         self.current_position = (x, y)
#         print(f"Moving to position: {self.current_position}")

#     def return_home(self):
#         self.move_to(0, 0)
#         print("Returned to home position.")

class NavigationSystem:
    def __init__(self, instruction_set):
        """Initialises navigation and collection system."""
        self.instruction_set = instruction_set  # Shared instruction set for reference
        self.home_position = (4, 0)  # Starting position
        self.current_position = (4, 0)  # Start at home position
        self.assembly_station = (2, 2)  # Central assembly station

        self.part_to_inventory_map = {
            "steel strings": "strings",
            "nylon strings": "strings",
            "short neck": "neck",
            "long neck": "neck",
            "acoustic body": "body",
            "electric body": "body",
            "bridge": "bridge",
            "fingerboard": "fingerboard",
            "tailpiece": "tailpiece",
            "tuners": "tuners",
            "pickups": "pickups",
            "tailpiece": "tailpiece"
        }

        # Define part locations around the room edges
        self.map_layout = {
            "assembly_station": self.assembly_station,

            "strings": (0, 4),
            "neck": (2, 4),
            "body": (4, 4),
            "bridge": (4, 2),
            "fingerboard": (2, 0),
            "tailpiece": (4, 1),
            "tuners": (1, 4),
            "pickups": (3, 4)
        }

        # Each part type stored along the edges
        self.inventory = {
            "strings": 10,
            "neck": 5,
            "body": 5,
            "bridge": 5,
            "fingerboard": 5,
            "tailpiece": 5,
            "tuners": 5,
            "pickups": 5
        }

        # Grid dimensions for ASCII visualisation
        self.rown = 5
        self.coln = 5


    def visualise_map(self):
        """Draws a simple ASCII representation of the grid."""
        sleep(1)  # Pause to allow user to see the map
        print("\nWorkshop Layout:")
        for r in range(self.rown):
            row_display = ""
            for c in range(self.coln):
                if (r, c) == self.current_position:
                    row_display += "  R  "  # Robot
                elif (r, c) == self.assembly_station:
                    row_display += "  A  "  # Assembly
                elif (r, c) == self.home_position:
                    row_display += "  H  "  # Home
                elif (r, c) in self.map_layout.values():
                    # Mark other storage points by their first letter
                    part_name = [k for k, v in self.map_layout.items() if v == (r, c)][0]
                    row_display += f" [{part_name[0].upper()}] "
                else:
                    row_display += " [ ] "
            print(row_display)
        print()
        

    def move_to(self, target, visualise=False):
        """Moves the robot to the target location if valid."""
        # Validate target
        if isinstance(target, str):
            if target not in self.map_layout:
                print(f"⚠️ Unknown target location '{target}'.")
                return False
            tx, ty = self.map_layout[target]
        elif isinstance(target, tuple) and len(target) == 2:
            tx, ty = target
        else:
            print("⚠️ Invalid target format. Use a location name or (x, y) tuple.")
            return False

        """Move step-by-step to the target location"""
        print(f"Moving from {self.current_position} to {target}...")
        while self.current_position != target:
            cx, cy = self.current_position
            if cx < tx:
                cx += 1
            elif cx > tx:
                cx -= 1
            if cy < ty:
                cy += 1
            elif cy > ty:
                cy -= 1
            self.current_position = (cx, cy)
            if visualise: self.visualise_map()
            sleep(0.5)  # Simulate time taken to move
        
    def collect_part(self, part, visualise=False):
        """Move to the correct area and collects the specified part."""
        inv_type = self.part_to_inventory_map.get(part)
        # Validate part and inventory
        if not inv_type:
            print(f"⚠️ Unknown part '{part}' - skipping.")
            return False

        if inv_type not in self.inventory:
            print(f"⚠️ No inventory record for {inv_type} - skipping.")
            return False

        if self.inventory[inv_type] <= 0:
            print(f"⚠️ Out of stock for {inv_type}! Cannot collect {part}.")
            return False

        # Move to the part's location
        target_pos = self.map_layout.get(inv_type)
        if target_pos:
            print(f"\nNavigating to {inv_type} area to collect {part}...")
            self.move_to(target_pos, visualise)
            self.inventory[inv_type] -= 1
            print(f"✅ Collected {part}. Remaining {inv_type} stock: {self.inventory[inv_type]}")
            return True
        else:
            print(f"⚠️ No location found for {inv_type}.")
            return False
        
    def return_parts(self, parts_list, visualise=False):
        """Returns collected parts back to their storage locations."""
        print("\nReturning collected parts to storage...")
        for part in parts_list:
            inv_type = self.part_to_inventory_map.get(part)
            if inv_type and inv_type in self.inventory:
                target_pos = self.map_layout.get(inv_type)
                if target_pos:
                    self.move_to(target_pos, visualise)
                    self.inventory[inv_type] += 1
                    print(f"🔄 Returned {part}. New {inv_type} stock: {self.inventory[inv_type]}")
                    if visualise:
                        self.visualise_map()
                    sleep(0.5)  # Simulate time taken to return each part
        print("All parts returned to storage.\n")

    def collect_all_parts(self, parts_list, visualise=True):
        """Collects all parts in the provided list."""
        collected_parts = []
        for part in parts_list:
            """set a flag to check if parts are collected"""
            success = self.collect_part(part, visualise)
            """...and check it"""
            if not success:
                print(f"⚠️ Cannot continue: {part} missing. Aborting collection.")
                """return collected parts so far"""
                self.return_parts(collected_parts, visualise)
                self.return_home(visualise)
                return False # Return False if any part is missing
            collected_parts.append(part)
            if visualise:
                self.visualise_map()
            sleep(0.5)  # Simulate time taken to collect each part
        
        # After collecting all parts, return to assembly station
        self.move_to(self.map_layout["assembly_station"])
        print("All parts collected and at assembly station.\n")
        return True # Return True since all parts were collected successfully

    def report_inventory(self):
        """Prints the current inventory status."""
        print("\n Current Inventory Status:")
        for part, stock in self.inventory.items():
            print(f"  - {part}: {stock} units")
        print("")

    def return_home(self, visualise=False):
        """Returns the robot to its home position."""
        print("Returning to home position...")
        self.move_to(self.home_position, visualise)
        print("Arrived at home position.\n")



# --- Core Robot System ---
class Robot:
    def __init__(self, name):
        self.name = name
        self.status = "Idle"

    def update_status(self, status):
        self.status = status
        print(f"[{self.name}] Status: {self.status}")

# --- THIS IS THE MAIN SYSTEM THAT INTEGRATES ALL MODULES ---
class RobotSystem:
    def __init__(self, robot_name):
        """Initializes the robot system with core modules."""
        self.robot = Robot(robot_name)
        self.instruction_set = InstructionSet()  # Shared instruction set for assembly
        self.navigation = NavigationSystem(self.instruction_set)
        self.assembly_module = AssemblyModule(self.instruction_set)
        self.current_task = None # Track current task

    def set_current_task(self, task):
        """Sets the current task and prints it."""
        self.current_task = task
        print(f"Current task: {self.current_task} --- ")

    def run(self):
        """Main method to run the robot system."""
        self.robot.update_status("Active")
        print("System running core modules...\n")
        self.interactive_loop() # Start the interactive loop, defined below

    def interactive_loop(self):
        """Main interactive loop for user input to build instruments. The loop continues until 'EXIT' is entered."""
        while True:
            choice = input("\nEnter instrument to build (guitar / violin / ukulele / bass) or 'EXIT' to quit: ").strip().lower()

            """Exit condition"""
            if choice == "exit":
                self.robot.update_status("Idle")
                print("Shutting down system. Goodbye.")
                break
            
            """ Validate other inputs and proceed with assembly """
            if choice in self.instruction_set.templates:
                self.robot.update_status(f"Preparing {choice} assembly.")
                self.set_current_task("COLLECTING PARTS")

                # Step 1: get parts and steps from instruction set
                parts, _ = self.instruction_set.get_template(choice)

                # Step 2: Navigate and collect parts
                all_collected = self.navigation.collect_all_parts(parts, visualise=True) # set a flag to check if all parts were collected
                """Check all parts collected"""
                if not all_collected: # check the flag
                    print(f"⚠️ Aborting {choice} assembly due to missing parts. Returning home.")
                    self.navigation.return_home(visualise=True)
                    self.robot.update_status("Idle")
                    continue  # Skip to next iteration of the loop

                self.navigation.report_inventory()

                """If any part was out of stock, return home and skip assembly"""
                if not all_collected:
                    print(f"Cannot proceed with {choice} assembly due to insufficient parts. Returning home.")
                    self.navigation.move_to(self.navigation.home_position)
                    self.robot.update_status("Idle")
                    continue  # Skip to next iteration of the loop
                """ Proceed to assembly if all parts collected """
                self.set_current_task("ASSEMBLING INSTRUMENT")
                self.navigation.move_to(self.navigation.assembly_station)
                self.robot.update_status(f"Assembling {choice}.")
                sleep(1)  # Simulate time taken to prepare for assembly
                

                # Step 3: Assemble the instrument
                self.assembly_module.build_instrument(choice)

                # Step 4: Return to home position
                self.set_current_task("RETURNING HOME") 
                self.navigation.move_to(self.navigation.home_position)
                self.robot.update_status("Idle")

            else:
                print("Invalid input. Please choose a valid instrument.")


# --- Main Execution ---
if __name__ == "__main__":

    """Automated testing section (required by the brief)"""
   # Basic module tests before running the system
    test_instructions = InstructionSet()
    test_nav = NavigationSystem(test_instructions)
    test_assembly = AssemblyModule(test_instructions)

    # Assert statements for automated testing
    assert "guitar" in test_instructions.list_supported_instruments(), "Guitar template missing."
    parts, steps = test_instructions.get_template("guitar")
    assert parts and steps, "InstructionSet did not return valid parts and steps."
    assert isinstance(test_nav.map_layout, dict), "Navigation map should be a dictionary."
    assert test_assembly.instruction_set is test_instructions, "AssemblyModule should share InstructionSet instance."

    print("✅ All automated tests passed!\n")

    # Run the main robot system
    system = RobotSystem("LuthierBot")
    system.run()
