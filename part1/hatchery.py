class Hatchery:
    def __init__(self, cash, technicians, supplies):
        """
        Initialize the Hatchery.
        :param cash: Initial cash balance.
        :param technicians: List of technician objects.
        :param supplies: Dictionary of supply types and their quantities.
        """
        self.cash = cash
        self.technicians = technicians
        self.supplies = supplies

    def update_cash(self, amount):
        """Update cash balance."""
        self.cash += amount

    def hire_technician(self, technician):
        """Add a technician to the team."""
        self.technicians.append(technician)

    def remove_technician(self, name):
        """Remove a technician by name."""
        self.technicians = [t for t in self.technicians if t.name != name]

    def get_status(self):
        """Display current hatchery status."""
        print(f"Cash: £{self.cash}")
        print("Technicians:")
        for t in self.technicians:
            print(f"  - {t.name}, Weekly rate: £{t.weekly_rate}")
        print("Supplies:")
        for supply, quantity in self.supplies.items():
            print(f"  - {supply}: {quantity}")
