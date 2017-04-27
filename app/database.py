import sqlite3
from .dojo import Dojo
from .staff import Staff
from .fellow import Fellow
from .office import Office
from .living_space import LivingSpace
from termcolor import colored

class Database():
    """ Contains CRUD operations for the database """

    conn = None

    def __init__(self, dojo):
        self.dojo = dojo
        self.db = None
    
    # Create DB

    def save_state(self, db='dojo'):
        """ Saves all data stored in the app to the specified database or a default database """
        self.db = db + '.sqlite'
        conn = sqlite3.connect(self.db)
        with conn:
            cursor = conn.cursor()

            # Create tables 
            create_room = '''CREATE TABLE if not exists room
            (room_id integer primary key not null,
            room_name text not null,
            room_type text not null
            )
            '''

            create_person = '''CREATE TABLE if not exists person
            (person_id integer primary key autoincrement not null,
            person_name text not null,
            person_type text not null,
            allocated_office text,
            allocated_livingspace text,
            wants_accommodation text
            )
            '''

            create_allocations = '''CREATE TABLE if not exists allocation
            (allocation_id integer primary key autoincrement not null,
            person_id int not null,
            room_id int not null
            )
            '''

            cursor.execute(create_room)
            cursor.execute(create_person)
            cursor.execute(create_allocations)

            # Check if db has a state already saved
            cursor.execute('''SELECT room_id FROM room''')
            entries = cursor.fetchall()
            if len(entries) >= 1:
                # Purge db
                cursor.execute('DELETE FROM room')
                cursor.execute('DELETE FROM person')
                cursor.execute('DELETE FROM allocation')

            # Insert data
            saved_people = []
            for room in self.dojo.rooms:
                # Insert rooms
                cursor.execute("""INSERT INTO room (room_name, room_type) VALUES
                            ('{0}', '{1}')""".format(room.room_name, room.room_type))
                inserted_room = cursor.lastrowid

                for person in room.occupants:
                    if person.person_name in saved_people:
                        break
                    # Insert people
                    person_name = person.person_name
                    person_type = person.person_type
                    allocated_office = person.allocated_office
                    allocated_living = None if person_type == 'staff' else person.allocated_livingspace
                    wants_accommodation = None if person_type == 'staff' else person.wants_accommodation
                    cursor.execute("""INSERT INTO person (person_name, person_type, allocated_office,
                                allocated_livingspace, wants_accommodation) VALUES
                                ('{0}', '{1}', '{2}', '{3}', '{4}')
                                """.format(person_name, person_type, allocated_office,
                                           allocated_living, wants_accommodation))

                    inserted_person = cursor.lastrowid
                    saved_people.append(person.person_name)

                    cursor.execute("""INSERT INTO allocation (person_id, room_id) VALUES
                                ('{0}', '{1}')""".format(inserted_person, inserted_room))

            print(colored('State has been saved successfully', 'green'))


    def load_state(self, database):
        """ Loads the state of the application from the database """
        if database is None or database.strip() == '':
            print(colored('Specify a database to load state from.', 'red'))
            return 'NO DATABASE'

        try:
            conn = sqlite3.connect(database)
            with conn:
                cursor = conn.cursor()

                # Load rooms into Dojo
                cursor.execute("""SELECT room_name, room_type FROM room""")
                db_rooms = cursor.fetchall()
                for row in db_rooms:
                    if row[1] == 'office':
                        self.dojo.rooms.append(Office(row[0]))
                    else:
                        self.dojo.rooms.append(LivingSpace(row[0]))

                # Load people into Dojo
                cursor.execute("""SELECT person_name, person_type, allocated_office,
                               allocated_livingspace, wants_accommodation FROM person""")
                for row in cursor.fetchall():
                    person_name = row[0]
                    person_type = row[1]
                    allocated_office = row[2]
                    allocated_livingspace = row[3]
                    wants_accommodation = row[4]

                    if person_type == 'staff':
                        self.dojo.people.append(Staff(person_name, allocated_office))
                    elif person_type == 'fellow':
                        self.dojo.people.append(Fellow(person_name, wants_accommodation,
                                                       allocated_office, allocated_livingspace))

                # Add people into their rooms
                for person in self.dojo.people:
                    for room in self.dojo.rooms:
                        if room.room_type == 'office':
                            if person.allocated_office == room.room_name:
                                room.occupants.append(person)
                        else:
                            if person.person_type == 'fellow':
                                if person.allocated_livingspace == room.room_name:
                                    room.occupants.append(person)

            print(colored('State has been restored successfully', 'green'))

        except sqlite3.Error as e:
            print(colored('Error {}'.format(e.args[0]), 'red'))
            return 'FAILED TO CONNECT'

