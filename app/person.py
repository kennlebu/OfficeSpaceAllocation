class Person(object):
    """Person class defines a person that has just joined 
    the Andela fellowship. They can either be a fellow
    or staff.
    """
    
    def __init__(self, person_name, allocated='N'):
        self.person_name = person_name
        self.allocated = allocated
            
        
            