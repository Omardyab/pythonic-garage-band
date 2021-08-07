
class Musician:

    def __init__(self, name, inst):
        self.name = name
        self.inst=inst
    def __repr__ (self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
    def __str__ (self):
        return f"My name is {self.name} and I play {self.inst}"
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return self.inst
class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"
# band = []
    # def play_solo(self):
    #     return "face melting guitar solo"

    # def play_solo(self):
    #     pass
    # def get_instrument(self):
    #     pass
    # @abstractmethod
    # def __str__ (self):
    #     pass
    # @abstractmethod
    # def __repr__ (self):
        pass
# class Band():
#     newband=[]
#     def __init__(self,name,members):
#         self.name=name
#         self.members=members
#         self.newband.append(self)

#     def __str__(self):
#         return "Band Class"
#     def __repr__ (self):
#             "Band Class"
#     def play_solos(self):
#         solo_bands=[]
#         for band in self.members:
#               solo_bands.append(band.play_solo())
#         return  solo_bands
#     @classmethod
#     def to_list(cls):
# """
# as in lab 
# A Band instance should have a name attribute which is a string.
# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.

# """

    # class Band :
    
    #   band=[]

    # def __init__(self,name,members):
    #     self.name=name
    #     self.members=members
    #     self.instances.append(self)
#          return cls.newband
class Band():
    newbands=[]
    def __init__(self,name,member):
        self.name=name
        self.members=member
        self.newbands.append(self)

    def __str__(self):
        return "Band Class"
    def __repr__ (self):
            "Band Class"
    def play_solos(self):
        solo_bands=[]
        for b in self.members:
              solo_bands.append(b.play_solo())
        return  solo_bands
    @classmethod
    def to_list(cls):
 
         return cls.newbands

