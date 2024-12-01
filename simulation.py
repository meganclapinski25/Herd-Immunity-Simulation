import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        logger = Logger(logger.py)
        
        self.virus = virus
        self.pop_size = pop_size
        
        
       
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        
        
        self.population = self._create_population(vacc_percentage,initial_infected)
        pass

    def _create_population(self):
        
        population = []
        
        for _ in range(initial_infected):
            population.append(Person(is_infected=True, is_vaccinated=False))
            
        for _ in range(self.pop_size - initial_infected):
            is_vaccinated = random.random() < vacc_percentage
            population.append(Person(is_infected=False, is_vaccinated=is_vaccinated))
            
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        
        return population

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        
        
        for person in self.population:
            #If one person is still infected keep simulation going, if no one is meaning virus is dead or people are dead stop simulation. 
            if person.is_infected:
                return True
            else:
                return False 
        

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter+=1
            self.time_step()
            
            
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            should_continue = self._simulation_should_continue()
            pass

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        
        for person in self.population:
            if person.is_infected == True:
                other_people = [person for p in self.population if p != person]
                interactions = random.sample(other_people, min(100, len(other_people)))
                for other_person in interactions:
                    newly_infected = self.interaction(person, other_person) 
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        

    def interaction(self, infected_person, random_person):
        newly_infected = []
        if random_person:  
            temp = random.randint(0.0 , 1.0)
            if temp < self.repro_rate:
                random_person.is_infected = True
                newly_infected.append(random_person)
    
        # TODO: Call logger method during this method.
        return newly_infected

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        
        for person in self.newly_infected:
            person.is_infected = True
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
