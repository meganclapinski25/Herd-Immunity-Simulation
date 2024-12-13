from virus import Virus 


def test_virus():
    virus = Virus("covid-19", 0.8, 0.2)
    assert virus.name == "covid-19"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.2
    print("Virus tests passed.")
    print(virus)
if __name__ == "__main__":
    test_virus()