# This is my version of the greedy algorthim for a free MIT course. This is lession 1.
# Course: https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/


"""
The fundamental problem with greedy sorting is that you can find a local best, but not a global best.
This is because you can't see the future. You can't know if the next item will be better than the current one.
"""


# PARTS = [["cpu", 500, 100], ["gpu", 1000, 200], ["PSU", 800, 150]]


class Part:
    def __init__(self, name: str, value: int | float, weight: int | float):
        """
        A basic class to represent a Computer part.
        """
        self.name = name
        self.value = value
        self.weight = weight
    
    def get_name(self) -> str:
        return self.name
    
    def get_value(self) -> int | float:
        return self.value
    
    def get_weight(self) -> int | float:
        return self.weight

    def density(self) -> int | float:
        return self.get_value() / self.get_weight()


class Sorter:
    def greedy_sort(self, parts, max_weight, key_function):
        """
        An example of the greedy sorting algorithm.
        """
        # Use sorted because it doesnt modify the original list
        # Use reverse=True to sort in descending order, smallest first
        fixed_list = sorted(parts, key=key_function, reverse=True)
        result = []
        total_cost = 0.0
        total_weight = 0.0

        for i in range(len(fixed_list)):
            # Check if the total weight + the weight of the item is less than or equal to the max weight
            if total_weight + fixed_list[i].get_weight() <= max_weight:
                result.append(fixed_list[i])
                total_weight += fixed_list[i].get_weight()
                total_cost += fixed_list[i].get_value()
        
        return (result, total_cost)


class Printer:
    def fprint(self, sort_type: str, values: tuple[list[Part], float | int]) -> str:
        """
        A Custom formatter for printing values. Currently made for greedy sorting, in the future for other types as well.
        """
        msg = f"Sorting by {sort_type}.\n"
        msg += f"{'-' * len(msg)}\n"

        for part in values[0]:
            name = part.get_name()
            msg += f"{name},\n"

        msg += f"Total value: {values[1]}"

        print(msg)
        return msg


class Tester:
    def __init__(self):
        """
        A universal testing class, it handels all the formatting and techincal stuff you need todo.
        """
        self.printer = Printer()
        self.sorter = Sorter()
    

    def greedy(self, parts, max_weight, sort_by: list[list[str, any]]):
        """
        Test greedy sorting algorithm.
        """
        for sorting_method in sort_by:
            self.printer.fprint(sorting_method[0], values=self.sorter.greedy_sort(parts, max_weight, sorting_method[1]))
            print()

cpu1 = Part("AMD Ryzen 7 7700", 329, 0.5)
gpu1 = Part("Nvidia GeForce RTX 2080", 699, 1.5)
psu1 = Part("Corsair 650W", 99, 2.5)
cpu2 = Part("Intel Core i9", 499, 0.6)
gpu2 = Part("AMD Radeon RX 6700 XT", 479, 1.3)
psu2 = Part("EVGA 750W", 129, 2.6)
ram1 = Part("Corsair Vengeance 16GB", 79, 0.1)
ram2 = Part("Kingston HyperX 16GB", 75, 0.1)
ssd1 = Part("Samsung 860 EVO 1TB", 109, 0.2)
ssd2 = Part("Crucial MX500 1TB", 98, 0.2)

PARTS = [cpu1, gpu1, psu1, cpu2, gpu2, psu2, ram1, ram2, ssd1, ssd2]
MAX_WEIGHT = 5

SORTING_METHODS = [("value", Part.get_value), ("weight", Part.get_weight), ("density", Part.density)]

test = Tester()

test.greedy(PARTS, MAX_WEIGHT, SORTING_METHODS)

# Output:

# Sorting by value.       
# ------------------      
# Nvidia GeForce RTX 2080,
# Intel Core i9,
# AMD Radeon RX 6700 XT,  
# AMD Ryzen 7 7700,       
# Samsung 860 EVO 1TB,    
# Crucial MX500 1TB,      
# Corsair Vengeance 16GB, 
# Kingston HyperX 16GB,   
#
# Total value: 2367.0     
#
#  
# Sorting by weight.      
# -------------------     
# EVGA 750W,
# Nvidia GeForce RTX 2080,
# Intel Core i9,
# Samsung 860 EVO 1TB,    
# Corsair Vengeance 16GB, 
#
# Total value: 1515.0     
# 
#
# Sorting by density.     
# --------------------    
# Intel Core i9,
# Corsair Vengeance 16GB, 
# Kingston HyperX 16GB,   
# AMD Ryzen 7 7700,       
# Samsung 860 EVO 1TB,    
# Crucial MX500 1TB,      
# Nvidia GeForce RTX 2080,
# AMD Radeon RX 6700 XT,
#   
# Total value: 2367.0   
