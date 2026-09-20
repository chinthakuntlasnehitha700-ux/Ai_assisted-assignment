# Electricity Bill Calculator

class ElectricityBill:
    def __init__(self, consumer_name, units):
        self.consumer_name = consumer_name
        self.units = units

    # Calculate electricity bill
    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 2

        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)

        else:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        return bill

    # Display bill details
    def display_bill(self):
        total_bill = self.calculate_bill()

        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Total Bill: ₹", total_bill)
        print("-" * 35)


# Create three ElectricityBill objects
consumer1 = ElectricityBill("Rahul", 100)
consumer2 = ElectricityBill("Priya", 200)
consumer3 = ElectricityBill("Anil", 250)

# Display bills
consumer1.display_bill()
consumer2.display_bill()
consumer3.display_bill()