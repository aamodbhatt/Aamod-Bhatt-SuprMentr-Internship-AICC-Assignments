# Assignment Date: 09/02/2026
# Assignment Name: AI Around Me
# Description: List 10 real-life AI applications you use daily and explain how
# ML might work behind each in 1-2 lines.

applications = [
    (
        "Google Search",
        "Learns from billions of click patterns (ranking models) to show the "
        "most relevant results for your query.",
    ),
    (
        "YouTube Recommendations",
        "Collaborative filtering and deep neural nets predict which next video "
        "you are most likely to watch based on your history.",
    ),
    (
        "Gmail Spam Filter",
        "A classifier (Naive Bayes / neural net) trained on labelled emails "
        "predicts whether a message is spam.",
    ),
    (
        "Google Maps ETA / Traffic",
        "Regression models use historical and live GPS data to predict travel "
        "time and congestion.",
    ),
    (
        "Instagram / Reels Feed",
        "Ranking models learn what kind of content keeps you engaged and pushes "
        "similar posts to the top of the feed.",
    ),
    (
        "Voice Assistants (Alexa/Siri/Google)",
        "Speech-to-text uses RNN/Transformer models and intent classifiers "
        "understand what you want to do.",
    ),
    (
        "Face Unlock on Phone",
        "A CNN extracts facial features and compares them with the stored "
        "embedding to authenticate you.",
    ),
    (
        "Netflix / Prime Recommendations",
        "Matrix factorisation and neural recommenders predict ratings for "
        "unseen movies and surface top matches.",
    ),
    (
        "Autocorrect / Keyboard Predictions",
        "Language models learn common character and word sequences to suggest "
        "the next word or fix typos.",
    ),
    (
        "Online Shopping (Amazon/Flipkart)",
        "Recommendation engines and demand-forecasting models suggest products "
        "and optimise prices.",
    ),
]


def main() -> None:
    print("=== 10 AI Applications I Use Daily ===\n")
    for i, (name, how) in enumerate(applications, start=1):
        print(f"{i}. {name}")
        print(f"   -> {how}\n")


if __name__ == "__main__":
    main()
