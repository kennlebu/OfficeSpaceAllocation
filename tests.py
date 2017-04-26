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

class TestCreateRoom(unittest.TestCase):
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


#unittest.main()
if __name__ == '__main__':
    nose.run(defaultTest=__name__)


