import os
import pkgutil
import importlib
from app.commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor and logging
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv() #loads the .env file contents
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.") 
        logging.info("")
        logging.error("Errors need to be checked")
        logging.debug("Need to fix") 
        logging.warning("Run tests again") 
        logging.critical("prioritize these tests")
        

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

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
        logging.info("Application started. Type 'exit' to exit.")
        print("menu command provides a list of commands. Type command then number space number to execute commandexit.")
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip()
            parts = user_input.split(maxsplit=1)
            command_name = parts[0] if parts else ''
            args = parts[1].split() if len(parts) > 1 else []
            # Execute the command with any argument that were provided
            if command_name:
                self.command_handler.execute_command(command_name, *args)

if __name__ == "__main__":
    app = App()
    app.start()
                