#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB program.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached (Ctrl+D).
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
