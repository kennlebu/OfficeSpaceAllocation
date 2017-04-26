import unittest
from ..person import Person
from ..dojo import Dojo
from ..fellow import Fellow
from ..staff import Staff

class PersonTest(unittest.TestCase):

    def test_create_person(self):
        """ Tests whether the object created is of type Person """
        dojo = Dojo()
        person = dojo.add_person("Kenneth Lebu", "fellow", "Y")
        self.assertTrue(person)

    def test_add_person(self):
        """ Tests whether a person is added to the Dojo """
        dojo = Dojo()
        initial_person_count = len(dojo.people)
        dojo.add_person("Bangi Lebu", "fellow")
        dojo.add_person("Magdalene Acio", "fellow", "Y")
        new_person_count = len(dojo.people)
        self.assertEqual(2, initial_person_count - new_person_count,
                         msg="2 new people should be added")

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
        
unittest.main()

