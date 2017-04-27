import sqlite3
from .dojo import Dojo

class Database():
    """ Contains CRUD operations for the database """

    conn = None

    def __init__(self, dojo):
        self.dojo = dojo
        self.db = None
    
    # Create DB

    def save_state(self, db='dojo.db'):
        """ Saves all data stored in the app to the specified database or a default database """
        self.db = db
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor

        # Create tables 
        create_room = '''CREATE TABLE room
        (room_id int primary key not null,
        room_name text not null,
        room_type text not null
        )
        '''

        create_person = '''CREATE TABLE person
        (person_id int primary_key not null,
        person_name text not null,
        person_type text not null,
        allocated_office text,
        allocated_livingspace text,
        wants_accommodation text
        )
        '''

        create_allocations = '''CREATE TABLE allocation
        (allocation_id int primary key not null,
        person_id int not null,
        room_id int not null
        )
        '''

        cursor.execute(create_room)
        cursor.execute(create_person)
        cursor.execute(create_allocations)

        # Check if db has a state already saved
        entries = cursor.execute('''SELECT room_id FROM room''')
        if len(entries) >= 1:
            # Purge db
            cursor.execute('DELETE FROM room')
            cursor.execute('DELETE FROM person')
            cursor.execute('DELETE FROM allocation')

        # Insert data
        saved_rooms = []
        for room in self.dojo.rooms:
            # Insert rooms
            cursor.execute('''INSERT INTO room (room_name, room_type) VALUES
                           ({0}, {1})'''.format(room.room_name, room.room_type))
            inserted_room = cursor.lastrowid

            for person in room.occupants:
                # Insert people
                person_name = person.person_name
                person_type = person.person_type
                allocated_office = person.allocated_office
                allocated_living = None if person_type == 'staff' else person.allocated_livingspace
                wants_accommodation = None if person_type == 'staff' else person.wants_accommodation
                cursor.execute('''INSERT INTO person (person_name, person_type, allocated_office,
                            allocated_livingspace, wants_accommodation) VALUES
                            ({0}, {1}, {2}, {3}, {4})
                            '''.format(person_name, person_type, allocated_office,
                                       allocated_living, wants_accommodation))

                inserted_person = cursor.lastrowid

                cursor.execute('''INSERT INTO allocation (person_id, room_id) VALUES
                               ({0}, {1})'''.format(inserted_person, inserted_room))

                saved_rooms.append(room)

