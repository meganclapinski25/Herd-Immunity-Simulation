import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger("simulation_log.txt") 
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population(vacc_percentage, initial_infected)
        self.newly_infected = []
        self.all_infected = []
        self.num_interactions = 0

    def _create_population(self, vacc_percentage, initial_infected):
        population = []
        starting_id = 1
        #number of people vaccinated 
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        # added vacinated people to poplulation
        for _ in range(num_vaccinated):
            population.append(Person(_id=starting_id,is_vaccinated=True, infection=False))
            starting_id+=1
        # add inital infected to population
        for _ in range(self.initial_infected):
            population.append(Person(_id=starting_id,is_vaccinated=False, infection=True))
            starting_id+=1
        remaining = self.pop_size - self.initial_infected - num_vaccinated
        for _ in range(remaining):
            population.append(Person(_id=starting_id,is_vaccinated=False, infection=False))
            starting_id+=1
        
        
        return population

    def _simulation_should_continue(self):
       return any(person.infected for person in self.population)
    
    def run(self):
        time_step_counter = 0
        should_continue = True
        
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate,self.virus.repro_rate)

        while should_continue:
            time_step_counter += 1
            num_interactions, new_infections = self.time_step()
            self.logger.log_interactions(time_step_counter,num_interactions,new_infections)
            should_continue = self._simulation_should_continue()

        self.logger.log_final_results(self.time_step,self.pop_size,self.population)

    def time_step(self):
        num_interactions = 0
        new_infections = 0

        # Create lists of uninfected and infected people
        uninfected_people = [p for p in self.population if not p.infected and not p.is_vaccinated]
        infected_people = [p for p in self.population if p.infected]

        for infected_person in infected_people:
            # Each infected person interacts with up to 100 healthy individuals
            interactions = min(10, len(uninfected_people))  # Cap at the available healthy individuals
            
            for _ in range(interactions):
                if not uninfected_people:  # Stop if no uninfected people are left
                    break

                # Choose a random uninfected person to interact with
                random_person = random.choice(uninfected_people)
                num_interactions += 1

                # Determine if the random person gets infected based on the reproduction rate
                if random.random() < self.virus.repro_rate:
                    random_person.infected = True
                    new_infections += 1
                    uninfected_people.remove(random_person)  # Remove from uninfected list to avoid re-interaction

        # Infect the newly infected people
        self._infect_newly_infected()
        return num_interactions, new_infections


    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infected:
            return  # Nothing happens if vaccinated or already infected
        if random_person.is_alive and random_person.infected is None:
            temp = random.uniform(0.0, 1.0)
            if temp < virus.repro_rate:
                random_person.infected = self.virus
                self.newly_infected.append(random_person)
                if random_person not in self.all_infected:
                    self.all_infected.append(random_person)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infected = self.virus
        self.newly_infected.clear()


if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    
    
    sim.run()