from hatchery import Hatchery
from technician import Technician
from fish import Fish
from warehouse import Warehouse

def main():
    # Initialize supplies and objects
    supplies = {"fertilizer": 2000, "feed": 20000, "salt": 5000}  # Starting supplies
    main_capacity = {"fertilizer": 20, "feed": 400, "salt": 200}
    aux_capacity = {"fertilizer": 10, "feed": 200, "salt": 100}
    depreciation = {"fertilizer": 0.4, "feed": 0.1, "salt": 0}
    costs = {"fertilizer": 0.10, "feed": 0.001, "salt": 0.001}
    
    warehouse = Warehouse(main_capacity, aux_capacity, depreciation, costs)
    technicians = []
    hatchery = Hatchery(cash=10000, technicians=technicians, supplies=supplies)

    # Define fish species
    fish_species = [
        Fish("Clef Fins", 100.0, 12, 2, 2.0, 250, 25),
        Fish("Timpani Snapper", 50.0, 9, 2, 1.0, 350, 10),
        Fish("Andalusian Brim", 90.0, 6, 2, 0.5, 250, 15),
        Fish("Plagal Cod", 100.0, 10, 2, 2.0, 400, 20),
        Fish("Fugue Flounder", 200.0, 12, 2, 2.5, 550, 30),
        Fish("Modal Bass", 300.0, 12, 6, 3.0, 500, 50),
    ]

    # Simulation parameters
    num_quarters = int(input("Enter the number of quarters to run the simulation (default 8): ") or 8)
    fixed_costs = 1500  # Quarterly fixed costs
    vendor_prices = {
        1: {"fertilizer": 0.30, "feed": 0.10, "salt": 0.05},
        2: {"fertilizer": 0.20, "feed": 0.40, "salt": 0.25}
    }

    # Simulation loop
    for quarter in range(1, num_quarters + 1):
        print(f"\n================================")
        print(f"====== SIMULATING quarter {quarter} ======")
        print(f"================================")

                # Add or remove technicians
        try:
            num_technicians = int(input("To add enter positive, to remove enter negative, no change enter 0: "))
        except ValueError:
            print("Invalid input! Please enter an integer value.")
            return  # Exits the current iteration or can use continue to retry
        
        if num_technicians > 0:
            for _ in range(num_technicians):
                name = input("Enter technician name: ")
                hatchery.hire_technician(Technician(name=name, weekly_rate=500))
                print(f"Hired {name}, weekly rate=500 in quarter {quarter}")
        elif num_technicians < 0:
            # Automatically remove a technician (e.g., remove the last technician in the list)
            for _ in range(-num_technicians):
                if hatchery.technicians:  # Ensure there is at least one technician to remove
                    technician_to_remove = hatchery.technicians.pop()  # Remove the last technician
                    print(f"Let go {technician_to_remove.name}, weekly rate=500 in quarter {quarter}")
                else:
                    print("No technicians to remove.")
        else:
            print("No technicians added or removed.")


        # Calculate available labour
        total_labour_weeks = len(hatchery.technicians) * 9  # Each technician provides 9 weeks of labour

        # Selling fish (adjusted initial supplies and labour)
        total_revenue = 0

        for fish in fish_species:
            to_sell = min(
                fish.demand,
                total_labour_weeks // fish.maintenance_time,
                supplies["fertilizer"] // fish.fertilizer,
                supplies["feed"] // fish.feed
            )
            if to_sell > 0:
                print(f"Fish {fish.species}, demand {fish.demand}, sell {to_sell}: {to_sell}")
                total_labour_weeks -= to_sell * fish.maintenance_time
                supplies["fertilizer"] -= to_sell * fish.fertilizer
                supplies["feed"] -= to_sell * fish.feed
                supplies["salt"] -= to_sell * fish.salt
                total_revenue += to_sell * fish.price
            else:
                print(f"Fish {fish.species}, demand {fish.demand}, sell {to_sell}: 0 ")
        
        # Update cash with revenue
        hatchery.update_cash(total_revenue)
        

        # Pay technicians
        technician_costs = len(hatchery.technicians) * 9 * 500
        hatchery.update_cash(-technician_costs)

        # Pay fixed costs
        hatchery.update_cash(-fixed_costs)

        # Depreciate warehouse
        warehouse.apply_depreciation()

        # Display warehouse and hatchery status
        print(f"\nHatchery Name: Eastaboga, Cash: £{hatchery.cash:.2f}")
       
        # Update warehouse supplies based on the current supplies
        for supply, quantity in supplies.items():
            warehouse.add_supply(supply, quantity)

        # Select vendor and restock supplies
        print("List of Vendors\n1. Slippery Lakes\n2. Scaly Wholesaler")
        vendor_choice = int(input("Enter number of vendor to purchase from: "))
        vendor = vendor_prices[vendor_choice]

        for supply, max_quantity in main_capacity.items():
            to_restock = max_quantity - supplies[supply]
            cost = to_restock * vendor[supply]
            if hatchery.cash >= cost:
                supplies[supply] += to_restock
                hatchery.update_cash(-cost)
            else:
                print(f"Can't restock {supply}, insufficient funds, need £{cost:.2f} but only have £{hatchery.cash:.2f}")

        # Check for bankruptcy after attempting to restock
        if hatchery.cash < 0:
            print(f"Went bankrupt restocking warehouse Main in quarter {quarter}")
            print(f"Hatchery Name: Eastaboga, Cash: £{hatchery.cash:.2f}")
            
            # Display warehouse and technician status at the time of bankruptcy
            print("\nWarehouse Main")
            for supply, quantity in warehouse.storage['main'].items():
                print(f"  {supply.capitalize()}: {quantity:.2f} (capacity={main_capacity[supply]})")
            
            print("\nWarehouse Auxilliary")
            for supply, quantity in warehouse.storage['aux'].items():
                print(f"  {supply.capitalize()}: {quantity:.2f} (capacity={aux_capacity[supply]})")
            
            print("\nTechnicians:")
            for technician in hatchery.technicians:
                print(f"  Technician {technician.name}, weekly rate={technician.weekly_rate}")
            
            print(f"END OF QUARTER {quarter}")
            break  # End the simulation if bankrupt

        # Limit the number of technicians to avoid excessive cost
        if len(hatchery.technicians) > 5:
            print("Max technicians reached.")
        else:
            num_technicians = int(input("Enter number of technicians: "))

        # Example: Skip fixed costs if cash is too low
        if hatchery.cash < 2000:
            print("Skipping fixed costs for this quarter due to insufficient cash.")
        else:
            hatchery.update_cash(-fixed_costs)
        # Example: Allow the simulation to continue even with negative cash, but stop after a few quarters
        if hatchery.cash < 0:
            print("Warning: Hatchery is in debt!")
            if quarter > 3:  # Bankruptcy only if it's been more than 3 quarters of negative cash flow
                print("Went bankrupt! Simulation ended.")
                break
        # Display a warning if cash is running low
        if hatchery.cash < 1000:  # You can adjust this threshold as needed
            print(f"Warning: Cash is low, only £{hatchery.cash:.2f} remaining.")
                
if __name__ == "__main__":
    main()
