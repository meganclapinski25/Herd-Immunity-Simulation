from person import Person 
from virus import Virus 


def test_person():
    virus = Virus("Flu", 0.5, 0.1)
    
    # Test vaccinated person
    vaccinated_person = Person(1, True)
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infected is None
    print("Vaccinated person tests passed.")
    
    # Test infected person
    infected_person = Person(2, False, virus)
    assert infected_person.is_alive is True
    assert infected_person.infected is not None
    survived = infected_person.did_survive_infection()
    print(f"Infected person survived: {survived}")
    print("Infected person tests passed.")
    

if __name__ == "__main__":
    test_person()