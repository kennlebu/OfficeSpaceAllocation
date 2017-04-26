from ..room import Room
from ..dojo import Dojo
import unittest

class TestCreateRoom(unittest.TestCase):
    
    def test_create_room_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.rooms)
        blue_office = dojo.create_room("office", "Blue")
        self.assertTrue(blue_office)
        new_room_count = len(dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_livingspace(self):
        dojo = Dojo()
        white_office = dojo.create_room("office", "White")
        self.assertTrue(white_office)
        self.assertTrue(isinstance(white_office, Room, 
                msg='Office should be an instance of Room'))

    def test_create_office(self):
        dojo = Dojo()
        warriors = dojo.create_room("livingspace", "Warriors")
        self.assertTrue(warriors)
        self.assertTrue(isinstance(warriors, Room, 
                msg='Living space should be an instance of Room'))

unittest.main()

    
