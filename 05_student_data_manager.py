# Assignment Date: 19/02/2026
# Assignment Name: Student Data Manager
# Description: Store data for 5 students using dictionaries, print topper,
# class average, and assign grades.


students = {
    "Aarav":   {"math": 85, "science": 92, "english": 78},
    "Diya":    {"math": 72, "science": 65, "english": 80},
    "Kabir":   {"math": 95, "science": 98, "english": 90},
    "Meera":   {"math": 60, "science": 55, "english": 70},
    "Rohan":   {"math": 88, "science": 75, "english": 82},
}


def grade(percentage: float) -> str:
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def main() -> None:
    averages = {}
    for name, marks in students.items():
        avg = sum(marks.values()) / len(marks)
        averages[name] = avg

    print("=== Student Report Card ===")
    print(f"{'Name':<10}{'Math':<8}{'Sci':<8}{'Eng':<8}{'Avg':<8}{'Grade':<6}")
    for name, marks in students.items():
        avg = averages[name]
        print(
            f"{name:<10}{marks['math']:<8}{marks['science']:<8}"
            f"{marks['english']:<8}{avg:<8.2f}{grade(avg):<6}"
        )

    topper = max(averages, key=averages.get)
    class_average = sum(averages.values()) / len(averages)

    print("\n--- Summary ---")
    print(f"Class Topper : {topper} ({averages[topper]:.2f}%)")
    print(f"Class Average: {class_average:.2f}%")


if __name__ == "__main__":
    main()
