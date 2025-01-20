class DamController:
    def __init__(self, max_capacity, warning_threshold, critical_threshold, total_gates):
        self.max_capacity = max_capacity  # Maximum water level capacity
        self.warning_threshold = warning_threshold  # Level to issue warnings
        self.critical_threshold = critical_threshold  # Level to open gates
        self.total_gates = total_gates  # Total number of gates available
        self.current_level = 0  # Current water level

    def update_water_level(self, level):
        """Update the water level."""
        self.current_level = level
        print(f"Current water level updated to: {self.current_level}%")

    def calculate_gates_to_open(self):
        """
        Calculate the number of gates to open based on the water level.
        Returns the number of gates to open.
        """
        if self.current_level < self.critical_threshold:
            return 0  # No need to open gates

        # Calculate excess water percentage above the critical threshold
        excess_water_percentage = self.current_level - self.critical_threshold

        # Calculate proportionate number of gates to open
        gates_to_open = (excess_water_percentage / (100 - self.critical_threshold)) * self.total_gates
        return max(1, int(gates_to_open))  # At least 1 gate if critical level is reached

    def check_status(self):
        """Check the dam status and determine actions."""
        if self.current_level >= self.critical_threshold:
            gates_to_open = self.calculate_gates_to_open()
            return f"Critical! Opening {gates_to_open} gate(s) to release water."
        elif self.current_level >= self.warning_threshold:
            return "Warning! Water level is high. Monitor closely."
        else:
            return "Normal. No action needed."


class DamChatBot:
    def __init__(self, dam_controller):
        self.dam_controller = dam_controller

    def interact(self):
        """Simple chatbot interaction."""
        while True:
            print("\nOptions:")
            print("1. Update water level")
            print("2. Check dam status")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    level = float(input("Enter the current water level (%): "))
                    if 0 <= level <= 100:
                        self.dam_controller.update_water_level(level)
                    else:
                        print("Invalid input! Enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")

            elif choice == "2":
                status = self.dam_controller.check_status()
                print(f"Dam Status: {status}")

            elif choice == "3":
                print("Exiting chatbot. Stay safe!")
                break
            else:
                print("Invalid choice! Please select a valid option.")


# Initialize the dam controller with thresholds and total gates
max_capacity = 100
warning_threshold = 75
critical_threshold = 90
total_gates = 12  # Example: The dam has 10 gates

dam_controller = DamController(max_capacity, warning_threshold, critical_threshold, total_gates)
chatbot = DamChatBot(dam_controller)


chatbot.interact()
