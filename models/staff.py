from person import Person

class Staff(Person):
    """Staff inherits from the person class.
    A staff is allocated office space but cannot be
    allocated living space
    """
    def __init__(self, name):
        super.__init__(self, name)
        self.person_type = "staff"