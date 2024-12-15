class Technician:
    def __init__(self, name, weekly_rate, specialty=None):
        """
        Initialize a Technician.
        :param name: Technician's name.
        :param weekly_rate: Weekly pay rate.
        :param specialty: Fish species the technician specializes in (optional).
        """
        self.name = name
        self.weekly_rate = weekly_rate
        self.specialty = specialty

    def __str__(self):
        return f"Technician {self.name}, Rate: £{self.weekly_rate}, Specialty: {self.specialty or 'None'}"
