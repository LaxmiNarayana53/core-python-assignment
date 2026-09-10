"""
Classroom Performance Tracker
Calculates student averages and identifies the top performer.
"""

def calculate_average(marks):
    """Calculate the average marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def calculate_student_averages(students):
    """Calculate the average marks for every student."""
    averages = {}

    for name, marks in students.items():
        averages[name] = calculate_average(marks)

    return averages


def find_top_performer(averages):
    """Find the student with the highest average."""
    if not averages:
        return None

    return max(averages, key=averages.get)


def main():
    students = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }

    averages = calculate_student_averages(students)
    top_performer = find_top_performer(averages)

    formatted_averages = {
        name: round(average, 2)
        for name, average in averages.items()
    }

    print("Average Marks:", formatted_averages)
    print("Top Performer:", top_performer)


if __name__ == "__main__":
    main()
