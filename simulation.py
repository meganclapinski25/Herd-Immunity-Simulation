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
        self.total_infected = initial_infected
        self.current_infected = self.initial_infected
        self.total_vacc = int(vacc_percentage*self.pop_size)
        self.total_dead = 0

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
        if self.total_vacc + self.total_dead >= self.pop_size:
            should_continue = False 
        else:
            should_continue = True

        return should_continue

    
    def run(self):
        time_step_counter = 0
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()

        return print(f'The simulation has ended after {self.time_step_counter} turns.')

    def time_step(self):
        newly_infected = []
        interactions_count = 0  # Track total interactions
        new_infections_count = 0  # Track new infections

        for person in self.population:
            if person.infected and person.is_alive:
                for _ in range(100):  # Each infected person interacts with 100 random people
                    random_person = random.choice(self.population)

                    # Skip dead individuals
                    if not random_person.is_alive:
                        continue
                    
                    # Log interaction outcomes
                    interactions_count += 1

                    if random_person.is_vaccinated:
                        self.logger.log_interactions(
                            step_number=self.current_infected,
                            number_of_interactions=interactions_count,
                            number_of_new_infections=new_infections_count,
                        )

                    elif random_person.infected:
                        continue  # No need to log sick person interaction repeatedly

                    else:  # Healthy and unvaccinated person
                        if random.random() < self.virus.repro_rate:
                            newly_infected.append(random_person)
                            new_infections_count += 1

        # Apply infections to newly infected
            for person in newly_infected:
                person.infected = True
                self.total_infected += 1

            self.logger.log_interactions(
                step_number=self.current_infected,
                number_of_interactions=interactions_count,
                number_of_new_infections=new_infections_count,
            )


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