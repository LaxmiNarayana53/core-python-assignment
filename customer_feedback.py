"""
Customer Feedback Analysis
Calculates the percentage of positive ratings.
Ratings of 4 or 5 are considered positive.
"""

def calculate_positive_percentage(ratings):
    """Calculate the percentage of positive feedback."""
    if not ratings:
        return 0

    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100


def main():
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]

    percentage = calculate_positive_percentage(ratings)
    print(f"Positive Feedback: {percentage:.1f}%")


if __name__ == "__main__":
    main()
