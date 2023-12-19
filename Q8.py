'''8. (Car-Pool Savings Calculator) Research several car-pooling websites. Create an application
that calculates your daily driving cost, so that you can estimate how much money could be 
saved by car pooling, which also has other advantages such as reducing carbon emissions 
and reducing traffic congestion. The application should input the following information and 
display the user’s cost per day of driving to work: 
a) Total miles driven per day.
b) Cost per gallon of gasoline.
c) Parking fees per day.
d) Average miles per gallon
e) Tolls per day'''
def car_pool_saving_calculator():
    Total_miles_driven_per_day=float(input("Please enter Total miles driven:"))
    Cost_per_gallon_of_gasoline=float(input("Please enter Cost per gallon of gasoline:"))
    Parking_fees_per_day=float(input("Please enter parking fees per day:"))
    Average_miles_per_gallon=float(input("Please enter average miles per gallon:"))
    Tolls_per_day=float(input("Please enter tolls per day:"))
    cost_per_day=(Total_miles_driven_per_day/Average_miles_per_gallon)*Cost_per_gallon_of_gasoline+Parking_fees_per_day+Tolls_per_day
    print("\nCost per day of driving to work is:Tsh",cost_per_day)
car_pool_saving_calculator()
