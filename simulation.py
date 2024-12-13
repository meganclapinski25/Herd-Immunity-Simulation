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
        infected_and_alive = any(person.infected and person.is_alive for person in self.population)
        all_vaccinated_or_dead = all(person.is_alive and person.is_vaccinated or not person.is_alive for person in self.population)
        return infected_and_alive and not all_vaccinated_or_dead

    def run(self):
        time_step_counter = 0
        should_continue = True
        self.logger.log_metadata(self.pop_size, self.virus)

        while should_continue:
            time_step_counter += 1
            self.logger.log_step(time_step_counter)
            self.time_step()
            should_continue = self._simulation_should_continue()

        self.logger.log_summary(time_step_counter, self.population)

    def time_step(self):
        for person in self.population:
            if person.infected:
                other_people = [p for p in self.population if p != person and p.is_alive]
                interactions = random.sample(other_people, min(100, len(other_people)))
                for other_person in interactions:
                    self.interaction(person, other_person)
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated or random_person.infected:
            return  # Nothing happens if vaccinated or already infected
        if random_person.is_alive and random_person.infected is None:
            temp = random.uniform(0.0, 1.0)
            if temp < infected_person.infected.repro_rate:
                random_person.infected = self.virus
                self.newly_infected.append(random_person)

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
    #sim.run()
