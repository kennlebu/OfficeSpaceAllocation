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
  -h --help     Sorry mate, no help for you.
  -v --version     Show version.
  -i --interactive      Interactive Mode
"""

import cmd
import sys
from docopt import docopt, DocoptExit
from termcolor import cprint
from app.dojo import Dojo

def docopt_cmd(prompt):
    """ Thus decorator is used to simplify the try/except block and pass
    the result of the decopt parsing to the called action.
    """

    def fun(self, args):
        try:
            opt = docopt(fun.__doc__, args)
        except DocoptExit as sys_exit:
            # This is thrown when the args don't match
            cprint('That command is not recognized', 'Red' 'on_grey')
            print(sys_exit)
            return

        except SystemExit:
            # Prints the usage for --help
            return

        return prompt(self, opt)

    fun.__name__ = fun.__name__
    fun.__doc__ = fun.__doc__
    fun.__dict__.update(prompt.__dict__)
    return fun


class InteractiveShell(cmd.Cmd):
    cprint("Welcome to Office Space Allocator", 'cyan', attrs=['bold'])
    cprint("Type -h or --help for a list of commands", 'cyan')

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

    @docopt
    def do_save_state(self, args):
        """ Usage: save_state [--db=sqlite_database] """
        print(args)

    @docopt
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
