class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        
    def __str__(self):
        return f"Virus(name={self.name}, repro_rate={self.repro_rate}, mortality_rate={self.mortality_rate})"


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    
    virus2 = Virus("test2", 0.2, 0.7)
    assert virus.name == "test2"
    assert virus.repro_rate == 0.2
    assert virus.mortality_rate == 0.7
    
    
    virus3 = Virus("test3", 0.9, 0.9)
    assert virus.name == "test3"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.9

