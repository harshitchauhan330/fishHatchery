class Fish:
    def __init__(self, species, fertilizer, feed, salt, maintenance_time, price, demand):
        """
        Initialize a Fish species.
        :param species: Name of the fish species.
        :param fertilizer: Fertilizer needed (ml).
        :param feed: Feed needed (kg).
        :param salt: Salt needed (kg).
        :param maintenance_time: Maintenance time required (weeks).
        :param price: Selling price per unit.
        :param demand: Quarterly demand.
        """
        self.species = species
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintenance_time = maintenance_time
        self.price = price
        self.demand = demand
