from .person import Person

class Fellow(Person):
    """Fellow inherits person. 
    
    A Fellow is allocated office space and can opt
    for living space too.
    """

    def __init__(self, person_name, wants_accommodation='N', allocated_office=None, allocated_livingspace=None):
        super().__init__(person_name, allocated_office)
        self.person_type = "fellow"
        self.allocated_office = allocated_office
        self.allocated_livingspace = allocated_livingspace
        self.wants_accommodation = wants_accommodation
