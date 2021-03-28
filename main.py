
# Type as much fizzing rules you want ;-)
fizzing_rules = {
    3: "Fizz",
    5: "Buzz",
    7: "Fuzz",
    11: "Bizz",
    13: "Biff"
}


def main(dictionary):
    print("Current Fizzing Rules: ", end="")
    for multiple, value in fizzing_rules.items():
        print(f"{multiple}=> {value}, ", end="")
    print()

    for i in range(1, int(input("Range: ")) + 1):
        output = ""

        for number, value in dictionary.items():
            if i % number == 0:
                output += value
        if output == "":
            output = i

        print(output)


if __name__ == "__main__":
    main(fizzing_rules)

