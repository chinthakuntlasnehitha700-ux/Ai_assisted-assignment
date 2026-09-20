# Product Inventory Management

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Calculate the total value of this product
    def total_value(self):
        return self.price * self.quantity


# Create a list of Product objects
products = [
    Product("Laptop", 50000, 3),
    Product("Mouse", 800, 10),
    Product("Keyboard", 1500, 4)
]

# Calculate total inventory value
total_inventory_value = 0

print("Product Inventory")
print("-" * 40)

for product in products:
    value = product.total_value()
    total_inventory_value += value

    print("Product Name:", product.name)
    print("Price: ₹", product.price)
    print("Quantity:", product.quantity)
    print("Total Value: ₹", value)

    # Check for low stock
    if product.quantity < 5:
        print("Status: Low Stock")

    print("-" * 40)


# Display total inventory value
print("Total Inventory Value: ₹", total_inventory_value)