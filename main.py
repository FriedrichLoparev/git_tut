def say_hello(name: str) -> str:
    print(f"Hello, {name}")


def calculate(number_1: int, number_2: int, command: str) -> float:
    match command:
        case "add":
            return number_1 + number_2
        case "subtract":
            return number_1 - number_2
        case "multiply":
            return number_1 * number_2
        case "divide":
            return number_1 / number_2
        case _:
            print("Incorrect command")
            return 0.0

number_1: int = int(input("What is the first number for the calculation?"))
number_2: int = int(input(What is the second number for the calculation?"))
command: str = input("What calculation do you want to perform?")
calculate(number_1, number_2, command)
