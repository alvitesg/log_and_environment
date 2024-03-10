import sys
from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.commands import CommandHandler

class divideCommand(Command):
    def execute(self, *args):
        """Executes the divide command with the provided arguments."""
        if len(args) != 2:
            print("Error: divideCommand requires exactly two arguments.")
            return

        try:
            # Convert arguments to Decimal for precision in arithmetic operations
            num1, num2 = map(Decimal, args)
            if num2 == 0:
                    print("Error: Cannot divide by zero")
                    return
            result = num1 / num2
            print(f"The result of dividing {num1} and {num2} is {result}")
        except InvalidOperation:
            print(f"Error: Invalid arguments. Both arguments must be numbers.")
        except ZeroDivisionError:
            print(f"Error: Cannot divide by zero")
            
# This allows the command to be imported directly from the add package
__all__ = ['divideCommand']
