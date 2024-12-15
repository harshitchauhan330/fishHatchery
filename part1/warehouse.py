class Warehouse:
    def __init__(self, main_capacity, aux_capacity, depreciation, costs):
        """
        Initialize the Warehouse.
        :param main_capacity: Capacity of the main warehouse.
        :param aux_capacity: Capacity of the auxiliary warehouse.
        :param depreciation: Depreciation rates for supplies.
        :param costs: Costs per unit of storage.
        """
        self.main_capacity = main_capacity
        self.aux_capacity = aux_capacity
        self.depreciation = depreciation
        self.costs = costs
        self.storage = {"main": {}, "aux": {}}

    def add_supply(self, supply, quantity, location="main"):
        if location in self.storage:
            current_quantity = self.storage[location].get(supply, 0)
            max_capacity = self.main_capacity[supply] if location == "main" else self.aux_capacity[supply]
            self.storage[location][supply] = min(current_quantity + quantity, max_capacity)


    def apply_depreciation(self):
        """Apply depreciation to supplies."""
        for location in self.storage:
            for supply, quantity in self.storage[location].items():
                self.storage[location][supply] = max(0, quantity - self.depreciation.get(supply, 0))
