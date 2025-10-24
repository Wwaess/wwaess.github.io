For **UNIT 7**
# Nested Dictionaries

A *dictionary* is a way of storing data in key:value pairs[^1]. 

A dictionary is *nested* if it contains other dictionaries. 

We want to make a class `Cars` which is a dictionary Object: we can do that by defining a dictionary in the `__init__` step: 

```py
class Car: 
    def __init__(self):
        # NESTED DICTIONARY HERE
        # Each car brand has a dictionary of models and details
        self.cars = {
            # So here, "Toyota" is its own dictionary, which itself contains the dictionaries "Aygo" and "Yaris" 
            "Toyota": {
                    "Aygo": {"year": 2011, "price": 1400},
                    "Yaris": {"year": 2010, "price": 2600}
                },
                "Honda": {
                    "Civic": {"year": 2002, "price": 1000},
                    "HR-V": {"year": 2001, "price": 750}
                },
                "Subaru": {
                    "XV": {"year": 2013, "price": 1500},
                    "Legacy": {"year": 2011, "price": 1845}
                }
            }

    # Use the ITEMS method to return each item in the dictionaries: 
    def show_items(self):
        print("Items (brand and model info): ")
        for brand, models in self.cars.items():
            print(f"{brand}: {models}")
        print() # for a blank space

    # Use the KEYS method to return the keys of the dictionary - in this case, the keys of "cars" is the brand names
    def show_keys(self):
        print("Keys (the car brands): ")
        for key in self.cars.keys():
            print(key)
        print()

    # Use the VALUES method to return the values with those keys
    def show_values(self):
        print("Values (the car model dictionaries): ")
        for value in self.cars.values():
            print(value)
        print()
```

Now if we run some test code after it like

```py
# Create an instance of the Car class
my_cars = Car()
# Call the methods to display items, keys, and values
my_cars.show_items()
my_cars.show_keys()
my_cars.show_values()
```


...we get the output:

```
Items (brand and model info): 
Toyota: {'Aygo': {'year': 2011, 'price': 1400}, 'Yaris': {'year': 2010, 'price': 2600}}
Honda: {'Civic': {'year': 2002, 'price': 1000}, 'HR-V': {'year': 2001, 'price': 750}}
Subaru: {'XV': {'year': 2013, 'price': 1500}, 'Legacy': {'year': 2011, 'price': 1845}}

Keys (the car brands):
Toyota
Honda
Subaru

Values (the car model dictionaries):
{'Aygo': {'year': 2011, 'price': 1400}, 'Yaris': {'year': 2010, 'price': 2600}}
{'Civic': {'year': 2002, 'price': 1000}, 'HR-V': {'year': 2001, 'price': 750}}
{'XV': {'year': 2013, 'price': 1500}, 'Legacy': {'year': 2011, 'price': 1845}}
``` 






# References
[^1]: https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/python_dictionaries_access.asp