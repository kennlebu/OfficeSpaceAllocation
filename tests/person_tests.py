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
        dojo5.create_room('office', ['corner office'])
        dojo5.create_room('livingspace', ['home'])
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

    def test_reallocate_person(self):
        """ Tests whether a person is reallocated to a new room """
        dojo7 = Dojo()
        # Add rooms to the Dojo
        dojo7.create_room('office', ['Big office'])
        dojo7.create_room('office', ['Small office'])
        dojo7.create_room('livingspace', ['Tiny home'])
        # Add people
        ken = dojo7.add_person('Ken Lebu', 'staff')
        steve = dojo7.add_person('Steve Rogers', 'staff')
        tony = dojo7.add_person('Tony Stark', 'fellow', 'Y')
        bucky = dojo7.add_person('Bucky Barnes', 'fellow', 'Y')
        # Get the current room of a Person
        current_room = ken.allocated_office
        new_room = None
        # Pick another room to put him in
        for room in dojo7.rooms:
            if room.room_name != current_room:
                new_room = room.room_name
        # Reallocate to new Room
        dojo7.reallocate_person(ken.person_name, new_room)
        # Get his new room to compare
        reallocated_room = None
        for person in dojo7.people:
            if person.person_name == ken.person_name:
                reallocated_room = person.allocated_office
        # Assert whether they are equal
        self.assertEqual(current_room, reallocated_room,
                         msg='Former and current room should be different')

    def test_load_people(self):
        """ Tests whether people are loaded from a file and added to the Dojo """
        dojo8 = Dojo()
        initial_people = len(dojo8.people)
        dojo8.load_people('input.txt')
        new_people = len(dojo8.people)
        # Check whether new people have been added
        self.assertTrue(new_people > initial_people,
                        msg='Number of people should increase')
        # Check whether the correct number of people have been added
        self.assertEqual(7, len(dojo8.people),
                         msg='There should be 7 new people')

if __name__ == '__main__':
    unittest.main()
