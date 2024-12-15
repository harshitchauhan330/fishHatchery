## Fish Hatchery Simulation Project
Overview
This project simulates the operations of a fish hatchery where we manage technicians, supplies, fish species, and financials over several quarters. The goal is to balance costs and revenue while avoiding bankruptcy. The simulation involves hiring/removing technicians, selling fish, and restocking supplies while managing the hatchery's cash flow.

## Files
1. hatchery.py
Defines the Hatchery class to manage:

Cash balance
Technicians
Supplies
2. technician.py
Defines the Technician class:

Models technicians with name and weekly rate
Provides methods to hire/remove technicians
3. fish.py
Defines the Fish class:

Models fish species with demand, price, and maintenance requirements
4. warehouse.py
Defines the Warehouse class:

Manages supplies in the main and auxiliary warehouses
Applies depreciation to supplies
5. main.py
Orchestrates the entire simulation
Simulates each quarter: adding/removing technicians, selling fish, updating supplies, and checking for bankruptcy
## Key Design Choices
Object-Oriented Design: Classes like Hatchery, Technician, and Fish help model real-world entities, making the simulation scalable and easy to maintain.
Technician Management: Technicians are added/removed based on user input. Technicians’ labor is crucial to fish production, so managing their costs is important.
Bankruptcy Handling: The simulation ends if the hatchery's cash goes negative after trying to restock supplies.
Supply Management: The hatchery restocks supplies based on available cash, ensuring it doesn’t overspend.
Improvements & Future Work
Dynamic Fish Market: Adjust fish demand and pricing based on market conditions.
Complex Financial Models: Introduce loans or investments to simulate a more advanced financial system.
GUI: Create a graphical interface to make interactions smoother and provide real-time updates.
## Conclusion
This project models a basic fish hatchery system, managing technicians, supplies, and fish production. It uses object-oriented principles to keep the system modular and easy to extend. Future improvements could include a dynamic market and a more complex financial model.