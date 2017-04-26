from .person import Person

class Fellow(Person):
    """Fellow inherits person. 
    
    A Fellow is allocated office space and can opt
    for living space too.
    """

    def __init__(self, person_name, allocated='N', accommodated='N'):
        super().__init__(person_name, allocated)
        self.person_type = "fellow"
        self.allocated = allocated
        self.accommodated = accommodated
