"""class MenuCommand(Command):
    def execute(self):
        print("Menu:")
        print("  add <number1> <number2> - Add two numbers.")
        print("  exit - Exit the application.")
        print("  subtract <number1> <number2> - Subtracts two numbers.")
        print("  divide <number1> <number2> - Divides two numbers.")
        print("  multiply <number1> <number2> - Multiply two numbers.")"""

from app.commands import Command

class MenuCommand(Command):
    requires_command_handler = True # This is the new identifier
    def __init__(self, command_handler):
        # commands should be a list of command names
        self.commands_handler = command_handler

    def execute(self, *args):
        print("Available commands:")
        #Access the comand names from teh CommandHandler's commands dictionary
        for command_name in self.commands_handler.commands.keys():
            print(f"- {command_name}")
            