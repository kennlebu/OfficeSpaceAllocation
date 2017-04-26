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
            pass


        elif person_type.upper() == 'FELLOW':
            pass

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
                    (person.allocated_livingspace is None and person.wants_accommodation=='Y')):
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
        for room in self.rooms:
            room_names.append(room.room.room_name)
        if new_room_name.upper() not in room_names:
            print("There is no room with that name")
            return

        # Check if the new room has space
        target_room = None
        for room in self.rooms:
            if new_room_name.upper() == room.room_name:
                target_room = room

        if target_room.len(target_room.occupants) >= target_room.max_occupants:
            print("{} is already full.".format(target_room.room_name))

        



    def load_people(self, filename):
        """ Adds people to rooms from the specified txt file. """

        pass
