import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("simulation_log.txt")
        self.virus = virus 
        self.pop_size = int(pop_size)
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        
        self.newly_infected = []
        # TODO: Store the virus in an attribute
        # TODO: Store pop_size in an attribute
        # TODO: Store the vacc_percentage in a variable
        # TODO: Store initial_infected in a variable
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        self.population = self._create_population(vacc_percentage, initial_infected)
        

    def _create_population(self, vacc_percentage, initial_infected):
        population = []
        for i in range(self.pop_size):
            if i < self.initial_infected:
                infected = self.virus
            else:
                infected = None
            vacc_status = random.random() < vacc_percentage
            person = Person(i, vacc_status, infected)
            population.append(person)
        return population

    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True
        
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, virus.name,
                                   virus.mortality_rate, virus.repro_rate)
        while should_continue:
            # TODO: Increment the time_step_counter
            time_step_counter+=1
            self.time_step()
            
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            self.logger.log_interactions(time_step_counter, 100, len(self.newly_infected))
            should_continue = self._simulation_should_continue()
            
            
        living_count = sum(1 for p in self.population if p.is_alive)
        dead_count = self.pop_size - living_count
        vaccinated_count = sum(1 for p in self.population if p.is_vaccinated)
        self.logger.log_final_results(time_step_counter, self.pop_size, living_count, dead_count, vaccinated_count)
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
            if person.is_alive and person.infected is not None:
                for _ in range (100):
                    random_person = random.choice(self.population)
                    while not random_person.is_alive or random_person == person:
                        random_person = random.choice(self.population)
                    self.interaction(person, random_person)
       

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated:
            
            return
        if random_person.is_alive and random_person.is_vaccinated is None:
            infection_chance = random.random()
            if infection_chance < virus.repro_rate:
                self.newly_infected.append(random_person)
                random_person.infected = infected_person.infected  
                self.time_step+=1
                infected_person.infected = True
        self.logger.log_interactions(self.time_step,1,1)
                
        
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.       
            
        

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infected = self.virus
        self.newly_infected = []
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.


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
    #virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()