class Item:
    def __init__(self):
        """
        Constructor for Item class
        Initializes price to 0.0
        """
        self.__price = 0.0  # Private variable for price (using double underscore)
    
    def getPrice(self):
        """
        Public method to get the price
        Returns the current price value
        """
        return self.__price
    
    def setPrice(self, p):
        """
        Public method to set the price
        Args:
            p (float): The new price value to set
        """
        self.__price = float(p)  # Convert to float to ensure type safety
    
    def __str__(self):
        """
        String representation of the Item object
        """
        return f"Item with price: {self.__price}"


# Example usage and testing
if __name__ == "__main__":
    # Create Item objects
    item1 = Item()
    item2 = Item()
    
    print("=== Initial Items ===")
    print(f"Item1: {item1}")
    print(f"Item2: {item2}")
    
    # Test getPrice method
    print(f"\nItem1 price: {item1.getPrice()}")
    print(f"Item2 price: {item2.getPrice()}")
    
    # Test setPrice method
    item1.setPrice(25.50)
    item2.setPrice(100.75)
    
    print("\n=== After setting prices ===")
    print(f"Item1: {item1}")
    print(f"Item2: {item2}")
    
    # Test with different data types
    item3 = Item()
    item3.setPrice(50)  # Integer input
    item3.setPrice("75.25")  # String input
    
    print(f"\nItem3: {item3}")
    print(f"Item3 price: {item3.getPrice()}")
    
    # Demonstrate that price is private (cannot access directly)
    print(f"\n=== Private Access Test ===")
    print("Trying to access private variable directly...")
    try:
        print(f"item1.__price: {item1.__price}")  # This will cause an error
    except AttributeError as e:
        print(f"Error: {e}")
        print("This proves that __price is private and cannot be accessed directly!")
