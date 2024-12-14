class Logger(object):
    def __init__(self, file_name):
       
        self.file_name = file_name 
        

    

    def write_metadata(self, population_size, vaccination_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, 'a') as file:
            file.write(f"Initial Population Size: {population_size}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Virus Mortality Rate: {mortality_rate}\n")
            file.write(f"Virus Reproduction Rate: {repro_rate}\n")
            file.write(f"Vaccination Percentage: {vaccination_percentage * 100}%\n")
            file.write("\n")
            
        

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
    

    def log_final_results(self, total_time_steps, vaccinated_count, total_interactions):
        with open(self.file_name, 'a') as file:
            file.write("\n--- Simulation Ended ---\n")
            file.write(f"Total Time Steps: {total_time_steps}\n")
            file.write(f"Vaccinated Population: {vaccinated_count}\n")
            file.write(f"Total Interactions: {total_interactions}\n")
            