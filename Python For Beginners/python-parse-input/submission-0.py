from typing import List

def read_integers() -> List[int]:
    numbers = input()

    list_of_integers = numbers.split(",")
    
    list_of_numbers = list(int(num) for num in list_of_integers)
    
    return list_of_numbers

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
