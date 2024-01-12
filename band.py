class Musician:
    """
    A class to represent a Musician.
    
    Attributes:
    name: str - the name of the band member
    
    Methods:
    get_instrument: returns the instrument the musician plays
    """
    def __init__(self, name="unknown"):
        self.name = name
        """
        Constructs all the necessary attributes for the musician object.
        
        Parameters:
        name: str - the name of the band member
        """
        
    def __str__(self):
        """Greets with the musician's name and instrument"""
        return f"My name is {self.name} and I play {self.get_instrument()}"
        
    
    def __repr__(self):
        """Identifies the class instance"""
        return f"Musician instance. Name = {self.name}"
        

class Guitarist(Musician):
    """
    A class to represent a Guitarist. It inherits attributes from the Musician.
    
    Attributes:
    name: str - the name of the band member
    
    Methods:
    get_instrument: returns the instrument the musician plays
    """
    def get_instrument(self):
        """returns the instrument the musician plays"""
        return "guitar"

    def play_solo(self):
        """returns the musician's solo"""
        return "face melting guitar solo" 
    
    def __repr__(self):
        """Identifies the class instance"""
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):
    """
    A class to represent a Bassist. It inherits attributes from the Musician.
    
    Attributes:
    name: str - the name of the band member
    
    Methods:
    get_instrument: returns the instrument the musician plays
    """
    def get_instrument(self):
        """returns the instrument the musician plays"""
        return "bass"
    
    def play_solo(self):
        """returns the musician's solo"""
        return "bom bom buh bom"
    
    def __repr__(self):
        """Identifies the class instance"""
        return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):
    """
    A class to represent a Bassist. It inherits attributes from the Musician.
    
    Attributes:
    name: str - the name of the band member
    
    Methods:
    get_instrument: returns the instrument the musician plays
    """        
    def get_instrument(self):
        """returns the instrument the musician plays"""
        return "drums"
    
    def play_solo(self):
        """returns the musician's solo"""
        return "rattle boom crash"
    
    def __repr__(self):
        """Identifies the class instance"""
        return f"Drummer instance. Name = {self.name}"


class Band:
    """
    A class to represent a Band made up of different kinds of musicians.
    
    Attributes:
    name: str - the name of band
    members: list - includes the names of band members
    
    Methods:
    add_musician: adds musician to the list of members
    play_solos: for each musician on the list of members, returns their solos as string
    to_list: returns the list of Band instances
    """
    instances = []
    
    def __init__(self, name="unknown", members=None):
        """
        Constructs all the necessary attributes for the band object.
        
        Class attribute assignment: instances; updates a class attribute to keep a record of created instances
        
        Parameters:
            name: str - name of the band
            members: list of strings - members of the bands
        """
        self.name = name
        self.members = members or []
        Band.instances.append(self)  # When a Band instance is created, it is added to the instances
        
    def add_musician(self, musician):
        """adds musician to the list of members"""
        self.members.append(musician)
        
    def play_solos(self):
        """for each musician on the list of members, returns their solos as string"""
        solos = []
        for musician in self.members:
            solos.append(musician.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        """returns the list of Band instances"""
        return cls.instances 
    
    def __str__(self):
        """returns string of each member"""
        member_strings = [str(member) for member in self.members] # list comprehension: iterates in place; get str and pass into arr
        return ' '.join(member_strings)
    
    def __repr__(self):
        """Identifies the class instance"""
        return f"Band instance. Name = {self.name}"