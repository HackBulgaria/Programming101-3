from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

    @classmethod
    def get_gender_or_female(cls, gender):
        if gender not in [member.value for _, member in cls.__members__.items()]:
            return cls.FEMALE.value

        return gender

class PandaSocialNetwork:
    def __init__(self):
        self.network = {}
    
    def has_panda(self, panda):
        return panda in self.network

    def add_panda(self, panda):
        if not self.has_panda(panda):
            raise Exception("Panda already there")

        self.network[panda] = []
    
    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        
        if self.are_friends(panda1, panda2):
            raise Exception("Pandas are already friends")

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

