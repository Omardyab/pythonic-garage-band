    def __repr__ (self):
        pass
    def play_solo(self):
        pass
    def get_instrument(self):
        pass

    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod
    def __repr__ (self):
        pass

# """
# as in lab 
# A Band instance should have a name attribute which is a string.
# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.

# """

    class Band :
    
      band=[]

    def __init__(self,name,members):
        self.name=name
        self.members=members
        self.instances.append(self)