"""Office Space Allocator.

Usage:
    spaceallocator create_room <room_type> <room_name>...
    spaceallocator add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    spaceallocator print_room <room_name>
    spaceallocator print_allocations [-o=filename]
    spaceallocator print_unallocated [-o=filename]
    spaceallocator reallocate_person <person_identifier> <new_room_name>
    spaceallocator load_people <filename>
    spaceallocator save_state [--db=sqlite_database]
    spaceallocator load_state <sqlite_database>
    spaceallocator (-h | --help)
    spaceallocator (-i | --interactive)
    spaceallocator --version

Options:
    -h --help    Sorry mate, no help for you.
    -v --version    Show version.
    -i --interactive    Interactive Mode
"""

import cmd
import sys
from docopt import docopt, DocoptExit
from termcolor import colored, cprint
from pyfiglet import figlet_format
from app.dojo import Dojo

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class InteractiveShell(cmd.Cmd):
    print(colored(figlet_format('Office Space Allocator', font='contrast'), 'cyan',
                  attrs=['bold']))
    intro = 'Welcome to Office Space Allocator \nType help to get a list of commands to use'

    prompt = '(Space Allocator) '

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        Dojo.create_room(args['<room_type>'], args['<room_name>'])

    @docopt_cmd
    def do_add_person(self, args):
        """ Usage: add_person <first_name> <last_namae> <FELLOW|STAFF> [wants_accommodation] """
        person_name = args['first_name'] + ' ' + args['last_name']
        person_type = args['']
        #Dojo.add_person(person_name, person_type)

    @docopt_cmd
    def do_print_room(self, args):
        """ Usage: print_room <room_name> """
        # room_name = args['<room_name>']
        # Dojo.print_room(room_name)
        print(args)

    @docopt_cmd
    def do_print_allocation(self, args):
        """ Usage: print_allocations [-o=filename] """
        print(args)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """ Usage: spaceallocator print_unallocated [-o=filename] """
        print(args)

    @docopt_cmd
    def do_reallocate_persom(self, args):
        """ Usage: reallocate_person <person_identifier> <new_room_name> """
        print(args)

    @docopt_cmd
    def do_load_people(self, args):
        """ Usage: load_people <filename> """
        print(args)

    @docopt_cmd
    def do_save_state(self, args):
        """ Usage: save_state [--db=sqlite_database] """
        print(args)

    @docopt_cmd
    def do_load_state(self, args):
        """ Usage: load_state <sqlite_database> """
        print(args)

    @docopt_cmd
    def do_quit(self, args):
        """ Quits the interactive mode """
        print("Bye!")
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    InteractiveShell().cmdloop()

# if __name__ == '__main__':
#     argu = docopt(__doc__, version='Office Space Allocator 1.0')
#     print(argu)
