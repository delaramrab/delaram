def compare_two_string(string_1: str, string_2: str) -> str:
    while len(string_1) != 0 and string_2:
        if string_1[0] > string_2[0]:
            string_2 = string_2[1:]
        elif string_1[0] == string_2[0]:
            string_2 = string_2[1:]
            string_1 = string_1[1:]
        else:
            string_1 = string_1[1:]

        if string_1 and len(string_2) != 0:
            string_1 = string_1[::-1]
            string_2 = string_2[::-1]

    if string_1 or string_2:
        return string_1 + string_2
    else:
        return "both of two strings are empty"


print(compare_two_string("ali", "mahdi"))
