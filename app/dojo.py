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
            print('Adding {}, type {}'.format(person_name, person_type))


        elif person_type.upper() == 'FELLOW':
            print('Adding {}, type {}, accommodation {}'.format(person_name,person_type,wants_accommodation))

        else:
            print("A person can only be staff or a fellow")



    def list_rooms(self):
        """ Lists the rooms that are existing in the Dojo """
        pass


    def create_room(self, room_type, *room_name):
        """ Creates a room of type <room_type> called <room_name>.
        If more than one name is passed, it creates as many rooms
        with the different names of type <room_type>.
        """

        if len(room_name) >= 1:
            for name in room_name:
                new_room = Office(name) if room_type.upper() == 'OFFICE' else LivingSpace(name)
                self.rooms.append(new_room)



    def print_room(self, room_name):
        """ Prints the names of all the people in the room """

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


    def print_allocations(self, filename=None):
        """ Prints a list of room allocations. If filename is specified,
        the list of allocations are outputted to the specified txt file.
        """
        output = ''
        for room in self.rooms:
            members = [] # List of members in the room
            output += room.room_name.upper() + '\n'
            output += '-------------------------------------\n'
            # Get the people in the room
            for person in self.people:
                if (person.allocated_office == room.room_name or
                        person.allocated_livingspace == room.room_name):
                    members.append(person.person_name.upper())

            output += ', '.join(members) + '\n'

        if filename is None:
            print(output)
        else:
            try:
                output_file = open('../' + filename, 'w+')
                output_file.write(output)
                output_file.close()
            except IOError:
                print('Failed to write to file')



    def print_unallocated(self, filename=None):
        """ Prints a list of unallocated people. If filename is specified,
        the list is outputted to the specified txt file.
        """
        unallocated_people = []
        output = ''
        for person in self.people:
            if (person.allocated_office is None or
                    (person.allocated_livingspace is None and person.wants_accommodation == 'Y')):
                unallocated_people.append(person.person_name)

            output += '\n'.join(unallocated_people)

        if filename is None:
            print(output)
        else:
            try:
                output_file = open('../' + filename, 'w+')
                output_file.write(output)
                output_file.close()
            except IOError:
                print('Failed to write to file')


    def reallocate_person(self, person_identifier, new_room_name):
        """ Reallocates the person identified by <person_identifier>
        to a new room specified by <room_name>
        """
        # Check if the new room exixts
        room_names = []
        new_room = None
        for room in self.rooms:
            room_names.append(room.room.room_name)
        if new_room_name.upper() not in room_names:
            print("There is no room with that name")
            return

        # Check if the new room has space
        for room in self.rooms:
            if new_room_name.upper() == room.room_name:
                new_room = room

        if new_room.len(new_room.occupants) >= new_room.max_occupants:
            print("{} is already full.".format(new_room.room_name))
            return

        # Remove occupant from former room.
        # First, get their former room.
        former_room = None
        the_person = None
        for person in self.people:
            if person.person_name == person_identifier.upper():
                the_person = person
                if new_room.room_type == 'office':
                    former_room = person.allocated_office
                    person.allocated_office = None
                elif new_room.room_type == 'livingspace':
                    former_room = person.allocated_livingspace
                    person.allocated_livingspace = None

        # Reduce occupants in that room
        for room in self.rooms:
            if room.room_name == former_room:
                room.occupants =- 1 

        # Add person to the new room
        new_room.occupants += 1
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

