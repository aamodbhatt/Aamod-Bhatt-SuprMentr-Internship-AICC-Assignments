# Assignment Date: 12/02/2026
# Assignment Name: Smart Input Program
# Description: Build a Python program that takes name, age, hobby and prints a
# personalized message while categorizing age using conditionals.


def categorize_age(age: int) -> str:
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"


def main() -> None:
    name = input("What is your name? ").strip()

    while True:
        try:
            age = int(input("How old are you? ").strip())
            if age < 0 or age > 120:
                print("Please enter a realistic age.")
                continue
            break
        except ValueError:
            print("Age must be a whole number.")

    hobby = input("What is your favourite hobby? ").strip()
    category = categorize_age(age)

    print("\n------ Your Personalized Message ------")
    print(f"Hi {name}! You are {age} years old and you love {hobby}.")
    print(f"Based on your age you are categorised as: {category}.")

    if category == "Child":
        print("Keep exploring and having fun with your hobby!")
    elif category == "Teenager":
        print("A great time to sharpen your skills in " + hobby + ".")
    elif category == "Adult":
        print("Balance work and your passion for " + hobby + ".")
    else:
        print("Enjoy your free time with " + hobby + "!")


if __name__ == "__main__":
    main()
