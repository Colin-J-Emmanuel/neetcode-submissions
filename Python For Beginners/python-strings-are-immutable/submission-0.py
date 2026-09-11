def remove_fourth_character(word: str) -> str:
    part_1 = word[:3]
    part_2 = word[4:]

    return part_1 + part_2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
