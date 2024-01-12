class Musician:
    def __init__(self, name="unknown"):
        self.name = name
        
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    
    def __repr__(self):
        return f"Musician instance. Name = {self.name}"
        

class Guitarist(Musician):

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo" 
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):

    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"
    
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):
        
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    instances = []
    
    def __init__(self, name="unknown", members=None):
        self.name = name
        self.members = members or []
        Band.instances.append(self)  # When a Band instance is created, it is added to the instances
        
    def add_musician(self, musician):
        self.members.append(musician)
        
    def play_solos(self):
        solos = []
        for musician in self.members:
            solos.append(musician.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        return cls.instances # returns the list of Band instances
    
    def __str__(self):
        member_strings = [str(member) for member in self.members] # list comprehension: iterates in place; get str and pass into arr
        return ' '.join(member_strings)
    
    def __repr__(self):
        return f"Band instance. Name = {self.name}"