class Person(object):
    """Person class defines a person that has just joined
    the Andela fellowship. They can either be a fellow
    or staff.
    """

    def __init__(self, person_name, allocated_office=None):
        self.person_name = person_name.title()
        self.allocated_office = allocated_office

            