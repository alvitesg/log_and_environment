import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command):
                        try:
                            # Check if special initialization is required
                            if hasattr(item, 'requires_command_handler') and item.requires_command_handler:
                                instance = item(self.command_handler)
                            else:
                                instance = item()  # Ensure this else block is correctly aligned
                        
                            # This part of the code should execute for every command
                            command_name = getattr(instance, 'command_name', plugin_name)
                            self.command_handler.register_command(command_name, instance)
                        except TypeError:
                            continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip()
            parts = user_input.split(maxsplit=1)
            command_name = parts[0] if parts else ''
            args = parts[1].split() if len(parts) > 1 else []
            # Execute the command with any argument that were provided
            if command_name:
                self.command_handler.execute_command(command_name, *args)
                