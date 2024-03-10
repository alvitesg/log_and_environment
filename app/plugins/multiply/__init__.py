import sys
from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.commands import CommandHandler

class multiplyCommand(Command):
    def execute(self, *args):
        """Executes the multiply command with the provided arguments."""
        if len(args) != 2:
            print("Error: multiplyCommand requires exactly two arguments.")
            return

        try:
            # Convert arguments to Decimal for precision in arithmetic operations
            num1, num2 = map(Decimal, args)
            result = num1 * num2
            print(f"The result of multiplying {num1} and {num2} is {result}")
        except InvalidOperation:
            print(f"Error: Invalid arguments. Both arguments must be numbers.")

# This allows the command to be imported directly from the add package
__all__ = ['multiplyCommand']
