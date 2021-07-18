
def solution(name, surname, age):
    return f"{str(name)[:2]}{str(surname)[:2]}{str(age)}"
    string_out = "{}{}{}".format(str(name)[:2], str(surname)[:2], str(age))
    return string_out
    pass


if __name__ == "__main__":


    name = "Jdaadd"
    surname  = "Fidasdds"
    age = 8
    string_out = solution(name, surname, age)
    print(string_out)