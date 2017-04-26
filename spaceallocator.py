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

from docopt import docopt, DocoptExit
import cmd
from termcolor import cprint
from app.dojo import Dojo

def docopt_cmd(prompt):
    """ Thus decorator is used to simplify the try/except block and pass
    the result of the decopt parsing to the called action.
    """

    def function(self, args):
        try:
            option = docopt(function.__doc__, args)
        except DocoptExit as sys_exit:
            # This is thrown when the args don't match
            cprint('That command is not recognized', 'Red' 'on_grey')
            print(sys_exit)
            return

        except SystemExit:
            # Prints the usage for --help
            return

        return prompt(self, option)

    function.__name__ = function.__name__
    function.__doc__ = function.__doc__
    function.__dict__.update(prompt.__dic__)
    return function


class InteractiveShell (cmd.Cmd):
    cprint("Welcome to Office Space Allocator", 'cyan', attrs=['bold'])
    cprint("Type -h or --help for a list of commands", 'cyan')
    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, args):
      """Usage: create_room <room_type> <room_name>..."""
      dojo.create_room(args['<room_type>'], args['<room_name>'])



if __name__ == '__main__':
    argu = docopt(__doc__, version='Office Space Allocator 1.0')
    print(argu)
