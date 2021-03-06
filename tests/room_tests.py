from app.room import Room
from app.dojo import Dojo
from app.living_space import LivingSpace
from app.office import Office
from app.person import Person
from app.dojo import Dojo
from app.fellow import Fellow
from app.staff import Staff
import unittest
import nose
import coverage
import os

class TestRoom(unittest.TestCase):
    """ Tests whether Offices and Living Spaces are created correctly """

    def test_create_room_successfully(self):
        """ Tests whether a room has been created and added to the Dojo """
        dojo = Dojo()
        initial_room_count = len(dojo.rooms)
        blue_office = dojo.create_room("office", ["Blue"])
        green_livingspace = dojo.create_room('livingspace', ['Green'])
        self.assertTrue(blue_office)
        self.assertTrue(green_livingspace)
        new_room_count = len(dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_create_existing_room(self):
        """ Tests whether the room to be created already exists """
        dojo6 = Dojo()
        office_one = dojo6.create_room('office', ['One'])
        office_two = dojo6.create_room('office', ['One'])
        self.assertEquals('EXISTS', office_two)

    def test_create_livingspace(self):
        """ Tests whether LivingSpace is created and added to the Dojo """
        dojo1 = Dojo()
        white_livingspace = dojo1.create_room("livingspace", ["White"])
        self.assertTrue(white_livingspace)
        self.assertTrue(isinstance(white_livingspace, LivingSpace),
                        msg='Living Space should be an instance of LivingSpace')
        self.assertTrue(white_livingspace in dojo1.rooms, msg='Room should be in rooms')

    def test_create_office(self):
        """ Tests whether an office is created and added to the Dojo """
        dojo2 = Dojo()
        warriors = dojo2.create_room("office", ["Warriors"])
        self.assertTrue(warriors)
        self.assertTrue(isinstance(warriors, Office),
                        msg='Office should be an instance of Office')
        self.assertTrue(warriors in dojo2.rooms, msg='Room should be in rooms')

    def test_print_room(self):
        """ Tests whether the members in a room are printed """
        dojo3 = Dojo()
        warriors = dojo3.create_room("office", ["Warriors"])
        green_livingspace = dojo3.create_room('livingspace', ['Green'])
        self.assertEqual([], dojo3.print_room('warriors'))

    def test_print_allocations(self):
        """ Tests whether room allocations are printed correctly """
        my_dojo = Dojo()
        # Create rooms
        my_office = my_dojo.create_room("office", ['my_office'])
        other_office = my_dojo.create_room("office", ['other_office'])
        my_living = my_dojo.create_room('livingspace', ['my_room'])
        # Assert whether the rooms have been created
        self.assertTrue(my_office, msg='An office should be created')
        self.assertTrue(other_office, msg='An office should be created')
        self.assertTrue(my_living, msg='A living space should be created')
        # Check whether the rooms have been added to the Dojo
        self.assertEqual(3, len(my_dojo.rooms))
        # Create staff
        my_dojo.add_person('Ken Lebu', 'staff')
        my_dojo.add_person('John Doe', 'staff')
        my_dojo.add_person('Sarah Doe', 'staff')
        # Create fellows
        my_dojo.add_person('Big Show', 'fellow', 'Y')
        my_dojo.add_person('Steven Segal', 'fellow')
        my_dojo.add_person('Jackie Chan', 'fellow', 'Y')
        my_dojo.add_person('Johnny Bravo', 'fellow', 'Y')
        my_dojo.add_person('Samurai Jack', 'fellow', 'Y')
        # Check whether people have been added to the Dojo
        self.assertEqual(8, len(my_dojo.people))
        # Check whether the members' list has the correct number of people
        self.assertEqual(12, len(my_dojo.print_allocations()))
        # Check whether list is printed to a file
        my_dojo.print_allocations('allocations')
        list_file = open('allocations.txt', 'r')
        text = list_file.readlines()
        self.assertTrue(len(text) > 3)


if __name__ == '__main__':
    unittest.main()

