"""Test plan for commands"""
import pytest
from app import App
from app.plugins.exit import ExitCommand
from app.plugins.greet import GreetCommand
from app.plugins.add import addCommand
from app.plugins.subtract import subtractCommand
from app.plugins.multiply import multiplyCommand
from app.plugins.divide import divideCommand

# pylint: disable=unused-variable, unused-argument
def test_greet_command(capfd):
    """Test the functionality of a command"""
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_exit_command(capfd):
    """Test the functionality of a command"""
    command = ExitCommand()
    with pytest.raises(SystemExit) as e:  # Expect a SystemExit exception
        command.execute()
    assert str(e.value) == "Exiting...", "The exit message did not match expected output."

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_add_command_success(capfd):
    """test additional of decimal places"""
    # Instantiate your command
    command = addCommand()
    # Execute the command with valid arguments
    command.execute("2.5", "3.5")
    # Capture the output
    out, err = capfd.readouterr()
    # Assert on the expected output
    assert "The result of adding 2.5 and 3.5 is 6.0" in out

def test_add_command_failure_invalid_arguments(capfd):
    """Test physical numbers"""
    command = addCommand()
    command.execute("two", "three")
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_add_command_failure_incorrect_argument_count(capfd):
    """Test incorrect arguments"""
    command = addCommand()
    # Test with too few arguments
    command.execute("5")
    out, err = capfd.readouterr()
    assert "Error: addCommand requires exactly two arguments." in out

    # Test with too many arguments
    command.execute("1", "2", "3")
    out, err = capfd.readouterr()
    assert "Error: addCommand requires exactly two arguments." in out

def test_subtract_command_success(capfd):
    """Test that subtractCommand correctly subtracts two numbers."""
    command = subtractCommand()
    command.execute("5", "3")
    out, _ = capfd.readouterr()
    assert "The result of subtracting 5 and 3 is 2\n" in out

def test_subtract_command_invalid_arguments(capfd):
    """Test subtractCommand with non-numeric arguments."""
    command = subtractCommand()
    command.execute("five", "three")
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_subtract_command_incorrect_argument_count(capfd):
    """Test subtractCommand with incorrect number of arguments."""
    command = subtractCommand()
    # Too few arguments
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Error: subtractCommand requires exactly two arguments." in out

    # Too many arguments
    command.execute("5", "3", "1")
    out, _ = capfd.readouterr()
    assert "Error: subtractCommand requires exactly two arguments." in out

#Multiply command test
def test_multiply_command_success(capfd):
    """Test that multiplyCommand correctly multiplies two numbers."""
    command = multiplyCommand()
    command.execute("4", "5")
    out, _ = capfd.readouterr()
    assert "The result of multiplying 4 and 5 is 20" in out

def test_multiply_command_invalid_arguments(capfd):
    """Test multiplyCommand with non-numeric arguments."""
    command = multiplyCommand()
    command.execute("four", "five")
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_multiply_command_incorrect_argument_count(capfd):
    """Test multiplyCommand with incorrect number of arguments."""
    command = multiplyCommand()
    # Too few arguments
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Error: multiplyCommand requires exactly two arguments." in out

    # Too many arguments
    command.execute("5", "3", "2")
    out, _ = capfd.readouterr()
    assert "Error: multiplyCommand requires exactly two arguments." in out

def test_divide_command_success(capfd):
    """Test that divideCommand correctly divides two numbers."""
    command = divideCommand()
    command.execute("10", "2")
    out, _ = capfd.readouterr()
    assert "The result of dividing 10 and 2 is 5\n" in out

def test_divide_command_by_zero(capfd):
    """Test divideCommand with division by zero."""
    command = divideCommand()
    command.execute("10", "0")
    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero\n" in out

def test_divide_command_invalid_arguments(capfd):
    """Test divideCommand with non-numeric arguments."""
    command = divideCommand()
    command.execute("ten", "two")
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_divide_command_incorrect_argument_count(capfd):
    """Test divideCommand with incorrect number of arguments."""
    command = divideCommand()
    # Too few arguments
    command.execute("10")
    out, _ = capfd.readouterr()
    assert "Error: divideCommand requires exactly two arguments." in out

    # Too many arguments
    command.execute("10", "2", "1")
    out, _ = capfd.readouterr()
    assert "Error: divideCommand requires exactly two arguments." in out
    