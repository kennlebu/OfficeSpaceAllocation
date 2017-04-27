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

class TestRoom(unittest.TestCase):
    """ Tests whether Offices and Living Spaces are created correctly """

    def test_create_room_successfully(self):
        """ Tests whether a room has been created and added to the Dojo """
        dojo = Dojo()
        initial_room_count = len(dojo.rooms)
        blue_office = dojo.create_room("office", "Blue")
        green_livingspace = dojo.create_room('livingspace', 'Green')
        self.assertTrue(blue_office)
        self.assertTrue(green_livingspace)
        new_room_count = len(dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_create_existing_room(self):
        """ Tests whether the room to be created already exists """
        dojo6 = Dojo()
        office_one = dojo6.create_room('office', 'One')
        office_two = dojo6.create_room('office', 'One')
        self.assertEquals('EXISTS', office_two)

    def test_create_livingspace(self):
        """ Tests whether LivingSpace is created and added to the Dojo """
        dojo1 = Dojo()
        white_livingspace = dojo1.create_room("livingspace", "White")
        self.assertTrue(white_livingspace)
        self.assertTrue(isinstance(white_livingspace, LivingSpace),
                        msg='Living Space should be an instance of LivingSpace')
        self.assertTrue(white_livingspace in dojo1.rooms, msg='Room should be in rooms')

    def test_create_office(self):
        """ Tests whether an office is created and added to the Dojo """
        dojo2 = Dojo()
        warriors = dojo2.create_room("office", "Warriors")
        self.assertTrue(warriors)
        self.assertTrue(isinstance(warriors, Office),
                        msg='Office should be an instance of Office')
        self.assertTrue(warriors in dojo2.rooms, msg='Room should be in rooms')

    def test_print_room(self):
        """ Tests whether the members in a room are printed """
        dojo3 = Dojo()
        warriors = dojo3.create_room("office", "Warriors")
        green_livingspace = dojo3.create_room('livingspace', 'Green')
        self.assertEqual([], dojo3.print_room('warriors'))

    def test_print_allocations(self):
        """ Tests whether room allocations are printed correctly """
        my_dojo = Dojo()
        # Create rooms
        my_office = my_dojo.create_room("office", 'my_office')
        other_office = my_dojo.create_room("office", 'other_office')
        my_living = my_dojo.create_room('livingspace', 'my_room')
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


class PersonTest(unittest.TestCase):
    """ Tests whether a person is created and added to the Dojo """

    def test_create_person(self):
        """ Tests whether the object created is of type Person """
        dojo4 = Dojo()
        person = dojo4.add_person("Kenneth Lebu", "staff")
        self.assertTrue(person)
        self.assertTrue(isinstance(person, Person))

    def test_add_person(self):
        """ Tests whether a person is added to the Dojo """
        dojo = Dojo()
        initial_person_count = len(dojo.people)
        dojo.add_person("Bangi Lebu", "fellow")
        dojo.add_person("Magdalene Acio", "fellow", "Y")
        dojo.add_person("Jackie Chan", 'staff')
        new_person_count = len(dojo.people)
        self.assertEqual(3, new_person_count - initial_person_count,
                         msg="3 new people should be added")

    def test_add_fellow(self):
        """ Tests whether the object created is of type Fellow """
        dojo = Dojo()
        resident_fellow = dojo.add_person("Daisy Asio", "fellow")
        non_resident_fellow = dojo.add_person("Nokia Face", "fellow", "Y")
        self.assertTrue(isinstance(resident_fellow, Fellow))
        self.assertTrue(isinstance(non_resident_fellow, Fellow))

    def test_add_staff(self):
        """ Tests whether the object created is of type Staff """
        dojo = Dojo()
        new_staff = dojo.add_person("Moses Ayiga", "staff")
        self.assertTrue(isinstance(new_staff, Staff))

    def test_print_unallocated(self):
        """ Tests whether unalloacted people are printed properly """
        dojo5 = Dojo()
        # Add a room to the Dojo
        dojo5.create_room('office', 'corner office')
        dojo5.create_room('livingspace', 'home')
        # Create staff
        dojo5.add_person('Ken Lebu', 'staff')
        dojo5.add_person('John Doe', 'staff')
        dojo5.add_person('Sarah Doe', 'staff')
        # Create fellows
        dojo5.add_person('Big Show', 'fellow', 'Y')
        dojo5.add_person('Steven Segal', 'fellow')
        dojo5.add_person('Jackie Chan', 'fellow', 'Y')
        dojo5.add_person('Johnny Bravo', 'fellow', 'Y')
        dojo5.add_person('Samurai Jack', 'fellow', 'Y')
        dojo5.add_person('Will Smith', 'fellow', 'Y')
        # Check for unallocated
        # 3 will miss offices, 1 will miss living space
        self.assertEqual(4, len(dojo5.print_unallocated()[0] + dojo5.print_unallocated()[1]),
                         msg='4 should be unallocated')
        self.assertEqual(1, len(dojo5.print_unallocated()[0]), msg='1 should miss living space')
        self.assertEqual(3, len(dojo5.print_unallocated()[1]), msg='3 should miss offices')



#unittest.main()
if __name__ == '__main__':
    #unittest.main()
    nose.run(argv=['--with-coverage'])


