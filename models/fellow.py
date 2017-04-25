from person import Person

class Fellow(Person):
    """Fellow inherits person. 
    
    A Fellow is allocated office space and can opt
    for living space too.
    """

    def __init__(self, person_name):
        super.__init__(self, person_name)
        self.person_type = "fellow"
