# Define the Triathlon class
class triathlon:
    """store the records for their members’ times"""
    # Initialize attributes in the constructor
    def __init__(self, first_name, last_name, location, swim, cycle, run, total_time):
        self.first = first_name
        self.last = last_name
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.total = total_time
    # Method to print details
    def info(self):
        print(f"{self.first} {self.last} ({self.location}): Swim {self.swim} Cycle {self.cycle} Run {self.run} Total {self.total}")
# give an example
jack = triathlon("Jack", "Doe", "London", 15, 45, 20, 80)
print(jack.info())
