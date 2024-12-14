import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = False):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated 
        self.infected = infection
        # TODO Define the other attributes of a person here
        self.is_alive = True
        

    def did_survive_infection(self):
        # This method checks if a person survived an infection. 
        # TODO Only called if infection attribute is not None.
        if self.infected is  None:
            return True
        chance = random.random()
        if chance < self.infected.mortality_rate:
                
                self.is_alive = False
                return False
        else:
                self.infected = None
                self.is_vaccinated = True
                return True
        
        # If the number is less than the mortality rate of the 
        # person's infection they have passed away. 
        # Otherwise they have survived infection and they are now vaccinated. 
        # Set their properties to show this
        # TODO: The method Should return a Boolean showing if they survived.
        

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infected is None
    print(vaccinated_person)


    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person.id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infected is None
    print(unvaccinated_person)
    # TODO Test unvaccinated_person's attributes here...
    

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.infected == virus
    assert infected_person.is_vaccinated is False
    survived = infected_person.did_survive_infection()
    assert survived in [True, False]
    
    
    people = []
    for i in range(1, 101):
        person = Person(i,False,virus)
        people.append(person)
        
        

    did_survived = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()
        if survived:
            did_survived+=1
        else:
            did_not_survive+= 1
   
    print(f"Out of 100 infected people:")
    print(f"  Survivors: {did_survived}")
    print(f"  Deaths: {did_not_survive}")


    

    