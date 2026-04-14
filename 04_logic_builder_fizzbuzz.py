# Assignment Date: 17/02/2026
# Assignment Name: Logic Builder
# Description: Print numbers 1-50 with Fizz/Buzz logic and count occurrences
# using loops and functions.


def fizz_buzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def run(limit: int = 50) -> dict:
    counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0, "Number": 0}
    for i in range(1, limit + 1):
        result = fizz_buzz(i)
        print(f"{i:>2} -> {result}")
        if result in counts:
            counts[result] += 1
        else:
            counts["Number"] += 1
    return counts


def main() -> None:
    counts = run(50)
    print("\n--- Count Summary (1 to 50) ---")
    for label, count in counts.items():
        print(f"{label:<9}: {count}")


if __name__ == "__main__":
    main()
