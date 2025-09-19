class House:
    def __init__(self, numberOfBedrooms, color):
        """
        Initialize a House object with number of bedrooms and color
        
        Args:
            numberOfBedrooms (int): Number of bedrooms in the house
            color (str): Color of the house
        """
        self.numberOfBedrooms = numberOfBedrooms
        self.color = color
    
    def get_number_of_bedrooms(self):
        """Get the number of bedrooms"""
        return self.numberOfBedrooms
    
    def get_color(self):
        """Get the color of the house"""
        return self.color
    
    def set_number_of_bedrooms(self, numberOfBedrooms):
        """Set the number of bedrooms"""
        self.numberOfBedrooms = numberOfBedrooms
    
    def set_color(self, color):
        """Set the color of the house"""
        self.color = color
    
    def __str__(self):
        """String representation of the House object"""
        return f"House with {self.numberOfBedrooms} bedrooms, color: {self.color}"


# Example usage
if __name__ == "__main__":
    # Create a house instance
    my_house = House(3, "blue")
    print(my_house)
    
    # Create another house
    another_house = House(2, "red")
    print(another_house)
    
    # Modify properties
    my_house.set_color("green")
    my_house.set_number_of_bedrooms(4)
    print(f"Updated house: {my_house}")
