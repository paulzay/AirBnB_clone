#!/usr/bin/python3
import cmd, sys


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to my shell! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """ Quit command to exit the program """
        print('exiting')
        return True

    def do_EOF(self, arg):
        """ END OF FILE """
        return True
    
    def emptyline(self):
        """ Dont execute anything """
        return ""



if __name__ == '__main__':
    HBNBCommand().cmdloop()
