import random

from .office import Office
from .living_space import LivingSpace
from .staff import Staff
from .fellow import Fellow

class Dojo():
    """ Dojo is a facility that accommodates Andelans in Kenya.

    A Dojo has many rooms and new fellows and staff are assigned
    rooms at random. A new fellow is assigned an office and can
    opt for living space too.
    New staff can only be allocated office space.
    """

    def __init__(self):
        self.rooms = []
        self.people = []

    def add_person(self, person_name, person_type, wants_accommodation='N'):
        """ Randomly adds a person to a room.
        Staff can only be added to offices. Fellows can be added to offices
        and living spaces. Living spaces however, are optional. A fellow is
        only added to a living space if they opt in by passing 'Y' as an
        argument on <wants_accommodation>
        """

        if person_type.upper() == 'STAFF':
            # Add an occupant to a random Office
            #print('Adding {}, type {}'.format(person_name, person_type))

            # Create Staff object
            new_staff = Staff(person_name)

            # Add the staff to the Dojo
            self.people.append(new_staff)

            # Allocate the staff an office
            self.allocate_office(new_staff)

            return new_staff


        elif person_type.upper() == 'FELLOW':
            #print('Adding {}, type {}, accommodation {}'.format(person_name,person_type,wants_accommodation))

            # Create a Fellow object
            new_fellow = Fellow(person_name, wants_accommodation)

            # Add the fellow to the Dojo
            self.people.append(new_fellow)

            # Allocate the fellow an Office
            self.allocate_office(new_fellow)

            if wants_accommodation.upper() == 'Y':
            # Allocate the fellow living space
                self.allocate_livingspace(new_fellow)

            return new_fellow

        else:
            print("A person can only be staff or a fellow")



    def allocate_livingspace(self, person):
        """ Allocates a new fellow living space at random """
        # Get living spaces available in the Dojo
        living_spaces = []
        for room in self.rooms:
            if room.room_type == 'livingspace':
                living_spaces.append(room)

        if len(living_spaces) < 1:
        # There is no living space in the Dojo
            print("There are no living spaces in the Dojo yet.",
                  "Create one using: create_room livingspace <room_name>")
            return 'NO LIVING SPACES'

        # Get rooms with space left in them
        unfilled_spaces = []
        for living_space in living_spaces:
            if len(living_space.occupants) < int(living_space.max_occupants):
                unfilled_spaces.append(living_space)

        if len(unfilled_spaces) < 1:
        # There are no living spaces with space in them
            print("All living spaces are full.",
                  "Create a new one using: create_room livingspace <room_name>")
            return 'NO SPACE'

        # Select a living space at random and add the fellow to it
        selected_space = random.choice(unfilled_spaces)
        selected_space.occupants.append(person)
        person.allocated_livingspace = selected_space.room_name
        print("{0} has been allocated the living space {1}"
              .format(person.person_name.split()[0], selected_space.room_name))


    def allocate_office(self, person):
        """ Allocates a person office space at random """

        # Get office spaces available in the Dojo
        office_spaces = []
        for room in self.rooms:
            if room.room_type == 'office':
                office_spaces.append(room)

        if len(office_spaces) < 1:
        # There is no office in the Dojo
            print("There are no offices in the Dojo yet.",
                  "Create one using: create_room office <room_name>")
            return 'NO OFFICES'

        # Get offices with space left in them
        unfilled_spaces = []
        for office in office_spaces:
            if len(office.occupants) < int(office.max_occupants):
                unfilled_spaces.append(office)

        if len(unfilled_spaces) < 1:
        # There are no offices with space in them
            print("All offices are full. Create a new one using: create_room office <room_name>")
            return 'NO SPACE'

        # Select an office at random and add the person in it
        selected_office = random.choice(unfilled_spaces)
        selected_office.occupants.append(person)
        person.allocated_office = selected_office.room_name
        print("{0} has been allocated the office {1}".format(person.person_name.split()[0],
                                                             selected_office.room_name))




    def list_rooms(self):
        """ Lists the rooms that are existing in the Dojo and the number
        of occupants they have
        """
        print('ROOM\t\t|\tOCCUPANTS')
        print('-----------------------------------------')
        for room in self.rooms:
            print(room.room_name + '\t\t :\t' + str(len(room.occupants)))




    def create_room(self, room_type, *room_name):
        """ Creates a room of type <room_type> called <room_name>.
        If more than one name is passed, it creates as many rooms
        with the different names of type <room_type>.
        """

        if len(room_name) >= 1:
            for room in self.rooms:
                for each_name in room_name:
                    if each_name.upper() == room.room_name:
                        return 'EXISTS'
            for name in room_name:
                new_room = Office(name) if room_type.upper() == 'OFFICE' else LivingSpace(name)
                self.rooms.append(new_room)
                return new_room

        else:
            print("Specify at least one room name")



    def print_room(self, room_name):
        """ Prints the names of all the people in the room """

        room_name = room_name.upper()
        output = []
        target_room = None
        for room in self.rooms:
            if room.room_name == room_name:
                target_room == room

        if target_room is None:
            print("There is no room called {}".format(room_name))
        else:
            for person in self.people:
                if (person.allocated_office == room_name or
                        person.allocated_livingspace == room_name):
                    print(person.person_name)
                    output.append(person.person_name)

        return output


    def print_allocations(self, filename=None):
        """ Prints a list of room allocations. If filename is specified,
        the list of allocations are outputted to the specified txt file.
        """
        output = ''
        all_members = [] # List of all members in the rooms
        for room in self.rooms:
            members = [] # List of memebers in the room
            output += room.room_name.upper() + '\n'
            output += '-------------------------------------\n'
            # Get the people in the room
            for member in room.occupants:
                members.append(member.person_name)
                all_members.append(member.person_name)

            output += ', '.join(members) + '\n\n'

        if filename is None:
            print(output)
        else:
            try:
                with open(filename + ".txt", "w+") as output_file:
                    output_file.write(output)
            except IOError:
                print('Failed to write to file')

        return all_members




    def print_unallocated(self, filename=None):
        """ Prints a list of unallocated people. If filename is specified,
        the list is outputted to the specified txt file.
        """
        unallocated_offices = []
        unallocated_living = []
        output = ''
        for person in self.people:
            if person.allocated_office is None:
                unallocated_offices.append(person.person_name)
            if person.person_type == 'fellow':
                if person.allocated_livingspace is None and person.wants_accommodation == 'Y':
                    unallocated_living.append(person.person_name)

        output += 'NOT ALLOCATED OFFICES\n'
        output += '----------------------------------\n'
        output += '\n'.join(unallocated_offices) + '\n'
        output += 'NOT ALLOCATED LIVING SPACES'
        output += '----------------------------------\n'
        output += '\n'.join(unallocated_living) + '\n'

        if filename is None:
            print(output)
        else:
            try:
                with open(filename + ".txt", "w+") as output_file:
                    output_file.write(output)
            except IOError:
                print('Failed to write to file')

        return [unallocated_living, unallocated_offices]


    def reallocate_person(self, person_identifier, new_room_name):
        """ Reallocates the person identified by <person_identifier>
        to a new room specified by <room_name>
        """
        # Check if the new room exixts
        room_names = []
        new_room = None
        for room in self.rooms:
            room_names.append(room.room_name)
        if new_room_name.upper() not in room_names:
            print("There is no room with that name")
            return 'NO SUCH ROOM'

        # Check if the new room has space
        for room in self.rooms:
            if new_room_name.upper() == room.room_name:
                new_room = room

        if len(new_room.occupants) >= int(new_room.max_occupants):
            print("{} is already full.".format(new_room.room_name))
            return "ROOM FULL"

        # Remove occupant from former room.
        # First, get their former room.
        former_room_name = None
        the_person = None
        for person in self.people:
            if person.person_name == person_identifier.upper():
                the_person = person
                if new_room.room_type == 'office':
                    former_room_name = person.allocated_office
                    person.allocated_office = None
                elif new_room.room_type == 'livingspace':
                    former_room_name = person.allocated_livingspace
                    person.allocated_livingspace = None

        if the_person is None:
            print('That person does not exist')
            return 'NO SUCH PERSON'

        # Reduce occupants in that room
        for room in self.rooms:
            if room.room_name == former_room_name:
                room.occupants.remove(the_person)

        # Add person to the new room
        new_room.occupants.append(the_person)
        if new_room.room_type == 'office':
            the_person.allocated_office = new_room.room_name
        else:
            the_person.allocated_livingspace = new_room.room_name




    def load_people(self, filename):
        """ Adds people to rooms from the specified txt file. """

        new_people = []
        try:
            input_file = open(filename)
            new_people = input_file.readlines()
        except IOError:
            print('Failed to read that file')

        if len(new_people) < 1:
            print('The file has no readable data')
        else:
            for person in new_people:
                person_args = person.split()
                person_name = ' '.join([person_args[0], person_args[1]])
                person_type = person_args[2]
                if len(person_args) > 3:
                    self.add_person(person_name, person_type, person_args[3])
                else:
                    self.add_person(person_name, person_type)

