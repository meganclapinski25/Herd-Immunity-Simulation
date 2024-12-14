class Logger(object):
    def __init__(self, file_name):
       
        self.file_name = file_name 
        

    

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        with open(self.file_name, "a") as file:
            file.write(f"Population Size:{pop_size}\n")
            file.write(f"Vaccination Percentage:{vacc_percentage}\n")
            file.write(f"Virus Name:{virus_name}\n")
            file.write(f"Mortality Rate:{mortality_rate}\n")
            file.write(f"Basic Reproduction Number:{basic_repro_num}\n")
            
        

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        
        with open(self.file_name, 'a') as file:
            file.write(f"Step Interactions: {step_number} \n")
            file.write(f"Number of Interactions: {number_of_interactions} \n")
            file.write(f"Number of New Infections: {number_of_new_infections} \n")
            
    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        
        with open(self.file_name, 'a') as file:
            file.write(f"Step Interactions: {step_number} \n")
            file.write(f"Population Count: {population_count} \n")
            file.write(f"Number of New Fatalities: {number_of_new_fatalities} \n")
    

    def log_final_results(self, total_steps, pop_size, living_count, dead_count, vaccinated_count):
        with open(self.file_name, 'a') as file:
            file.write("Final Simulation Results:\n")
            file.write(f"    Total Time Steps:{total_steps}\n")
            file.write(f"    Initial Population Size:{pop_size}\n")
            file.write(f"    Living Population:{living_count}\n")
            file.write(f"    Deceased Population:{dead_count}\n")
            file.write(f"    Vaccinated Population:{vaccinated_count}\n")