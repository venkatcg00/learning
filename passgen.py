"""
A password generator program that generates strong passwords based on user input.
"""

import random
import string
import time


class Color:
    """
    A class representing different colors for console output
    """
    RED: str = '\033[91m'
    GREEN: str = '\033[92m'
    YELLOW: str = '\033[93m'
    BLUE: str = '\033[94m'
    MAGENTA: str = '\033[95m'
    CYAN: str = '\033[96m'
    RESET: str = '\033[0m'


class Printer:
    """
    A class to handle printing with different colors.
    """
    @staticmethod
    def print_with_color(text: str, color: str) -> None:
        """
        Prints the specified text in the specified color
        """
        print(color + text + Color.RESET)

    @staticmethod
    def print_dashed_line() -> None:
        """
        Prints a dashed line to separate different segments of code output.
        """
        Printer.print_with_color('-' * 50, Color.CYAN)


class PasswordGenerator:
    """
    A class to generate a strong password.
    """
    total_attempts: int = 0  # Track the total number of attempts

    def __init__(self, length: int) -> None:
        self.length: int = length
        self.attempt: int = 0
        self.password: str = ''

    def generate_password(self) -> str:
        """
        Generate an encrypted password with the specified length.

        Returns:
            str: Generated strong password
        """
        is_password_strong: bool = False

        while not is_password_strong:
            self.attempt += 1
            PasswordGenerator.total_attempts += 1  # Increment the total attempts
            Printer.print_with_color(f"Attempt {self.attempt}: Generating password...", Color.YELLOW)
            self.password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation,
                                                   k=self.length))
            Printer.print_with_color(f"Generated password: {self.password}", Color.MAGENTA)
            print()

            # Check if the generated password passes the strong password policy.
            # Add the reasons to a list if the password does not pass strong password policy.
            reasons = []

            if not any(char.isupper() for char in self.password):
                reasons.append("Missing uppercase characters")
            if not any(char.islower() for char in self.password):
                reasons.append("Missing lowercase characters")
            if not any(char.isdigit() for char in self.password):
                reasons.append("Missing digits")
            if not any(char in string.punctuation for char in self.password):
                reasons.append("Missing special characters")
            if self.password[-1].isdigit() or self.password[-1] in string.punctuation:
                reasons.append("Last character cannot be a digit or special character")
            if self.password[-2].isdigit() or self.password[-2] in string.punctuation:
                reasons.append("Second last character cannot be a digit or special character")
            if self.password[0] in string.punctuation:
                reasons.append("First character cannot be a special character")


            if not reasons:
                is_password_strong = True
                Printer.print_with_color("Checking if the generated password is as per standards...", Color.YELLOW)
                print()
                time.sleep(1)
                Printer.print_with_color("Generated password is strong and meets all the requirements.", Color.GREEN)
                print()
            else:
                Printer.print_with_color("Checking if the generated password is as per standards...", Color.YELLOW)
                print()
                time.sleep(1)
                Printer.print_with_color("Generated password is not strong. Reasons:", Color.RED)
                print()
                for reason in reasons:
                    Printer.print_with_color(f"- {reason}", Color.RED)
                print()
                Printer.print_with_color("Generating a new password...", Color.RED)
                print()

        return self.password


class PasswordManager:
    """
    A class to manage the password generation process.
    """
    @staticmethod
    def get_password_length() -> int:
        """
        Gets the desired password length from user input.

        Returns:
            int: The desired password length.
        """
        while True:
            try:
                password_length = int(input(Color.YELLOW + "Enter the desired password length (minimum 8): " + Color.RESET))
                if password_length >= 8:
                    print()
                    Printer.print_with_color("Password Length is meeting the threshold.",Color.GREEN)
                    print()
                    return password_length
                else:
                    print()
                    Printer.print_with_color("Password length should be greater than 8.", Color.RED)
                    print()
            except ValueError:
                print()
                Printer.print_with_color("Invalid Input! Please enter a valid integer.", Color.RED)
                print()

    @staticmethod
    def generate_password() -> None:
        """
        Generate a strong password based on user input.
        """
        Printer.print_dashed_line()
        Printer.print_with_color("Password Generator", Color.MAGENTA)
        Printer.print_dashed_line()

        # Get user input for password length
        password_length = PasswordManager.get_password_length()

        Printer.print_dashed_line()
        Printer.print_with_color("Generating Strong Password...", Color.YELLOW)
        Printer.print_dashed_line()

        # Generate password and measure time taken
        start_time: float = time.time()
        generator: PasswordGenerator = PasswordGenerator(password_length)
        generated_password: str = generator.generate_password()
        end_time: float = time.time()
        time_taken: float = round(end_time - start_time, 2)

        Printer.print_dashed_line()
        Printer.print_with_color("Password Generation Complete.", Color.BLUE)
        Printer.print_dashed_line()
        print()
        Printer.print_with_color(f"Generated Password: {generated_password}", Color.GREEN)
        Printer.print_with_color(f"Time Taken: {time_taken} seconds", Color.GREEN)
        Printer.print_with_color(f"Total Attempts: {PasswordGenerator.total_attempts}", Color.GREEN)  # Print total attempts
        print()
        Printer.print_dashed_line()


def main() -> None:
    """
    The main function to execute the password generation process.
    """
    Printer.print_dashed_line()
    Printer.print_with_color("Welcome to Password Generator!", Color.BLUE)
    Printer.print_with_color("This program generates a strong password based on your input.", Color.BLUE)
    print()

    # Generate Password
    PasswordManager.generate_password()

    Printer.print_with_color("Thank you for using Password Generator!", Color.BLUE)


if __name__ == "__main__":
    main()
