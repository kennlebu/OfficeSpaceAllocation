from .person import Person

class Staff(Person):
    """Staff inherits from the person class.
    A staff is allocated office space but cannot be
    allocated living space
    """
    def __init__(self, name, allocated='N'):
        super().__init__(name, allocated)
        self.person_type = "staff"
        self.allocated = allocated
        