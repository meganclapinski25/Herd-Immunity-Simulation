import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    newly_infected = []
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        
        
        self.logger = Logger("simulation.log") 
        
        self.virus = virus
        self.pop_size = pop_size
        
        
       
       
        
        
        self.population = self._create_population(vacc_percentage, initial_infected)

    def _create_population(self, vacc_percentage, initial_infected):
        
        population = []
        
        for _ in range(initial_infected):
            population.append(Person(_id=len(population), is_vaccinated=False, infection=virus))
            
        for _ in range(self.pop_size - initial_infected):
            is_vaccinated = random.random() < vacc_percentage
            population.append(Person(_id=len(population), is_vaccinated=is_vaccinated, infection=None))

            
        
        
        return population

    def _simulation_should_continue(self):
        
        
        
        for person in self.population:
            if person.infected:
                return True
            
        return False 
        

    def run(self):
       

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter+=1
            self.time_step()
            
            
           
            should_continue = self._simulation_should_continue()
            pass

        

    def time_step(self):
        newly_infected = []
        for person in self.population:
            if person.infected == True:
                other_people = [person for p in self.population if p != person]
                interactions = random.sample(other_people, min(100, len(other_people)))
                for other_person in interactions:
                    newly_infected = self.interaction(person, other_person) 
                    self.newly_infected.extend(newly_infected)
       
        

    def interaction(self, infected_person, random_person):
        
        if random_person:  
            temp = random.uniform(0.0 , 1.0)
            if temp < infected_person.infected.repro_rate:
                random_person.infected = True
                self.newly_infected.append(random_person)
    
        
        return self.newly_infected

    def _infect_newly_infected(self):
        
        
        for person in self.newly_infected:
            person.infected = True
        self.newly_infected = []


if __name__ == "__main__":
    
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    
    
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    #sim.run()
