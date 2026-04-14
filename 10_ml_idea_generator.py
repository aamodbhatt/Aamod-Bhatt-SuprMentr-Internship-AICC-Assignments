# Assignment Date: 02/03/2026
# Assignment Name: ML Idea Generator
# Description: Suggest ML problems in college, healthcare, shopping and
# describe input -> output.


ideas = [
    {
        "domain": "College",
        "problem": "Predict whether a student is at risk of failing a course.",
        "input":   "Attendance %, past test scores, hours studied, assignment "
                   "submission rate, subject difficulty.",
        "output":  "Probability / class label: 'At Risk' vs 'Safe'.",
        "type":    "Supervised Classification",
    },
    {
        "domain": "College",
        "problem": "Recommend elective courses to students.",
        "input":   "Past grades, interests, career goal, peer choices.",
        "output":  "Ranked list of recommended electives.",
        "type":    "Recommendation System",
    },
    {
        "domain": "Healthcare",
        "problem": "Diabetes risk prediction.",
        "input":   "Age, BMI, glucose level, insulin, blood pressure, family "
                   "history.",
        "output":  "Risk score 0-1 plus class label (Diabetic / Not).",
        "type":    "Supervised Classification",
    },
    {
        "domain": "Healthcare",
        "problem": "Medical image diagnosis (e.g., X-ray pneumonia detection).",
        "input":   "Chest X-ray image.",
        "output":  "Probability of pneumonia + region highlighted.",
        "type":    "Deep Learning (CNN)",
    },
    {
        "domain": "Shopping",
        "problem": "Personalised product recommendations.",
        "input":   "User profile, previous purchases, clicks, cart history.",
        "output":  "Top-N products the user is most likely to buy.",
        "type":    "Collaborative Filtering",
    },
    {
        "domain": "Shopping",
        "problem": "Dynamic price prediction.",
        "input":   "Historical prices, demand, season, stock, competitor price.",
        "output":  "Recommended price for today.",
        "type":    "Regression",
    },
]


def main() -> None:
    print("=== ML Idea Generator ===\n")
    for i, idea in enumerate(ideas, start=1):
        print(f"{i}. [{idea['domain']}] {idea['problem']}")
        print(f"   Type  : {idea['type']}")
        print(f"   Input : {idea['input']}")
        print(f"   Output: {idea['output']}\n")


if __name__ == "__main__":
    main()
