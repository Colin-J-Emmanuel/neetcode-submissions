from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    list_of_names = []

    for key in age_dict:   # the names are the keys in this scenario
        list_of_names.append(key)

    return list_of_names


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    list_of_ages = []

    for key, value in age_dict.items():
        list_of_ages.append(value)

    return list_of_ages

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
