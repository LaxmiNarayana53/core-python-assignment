"""
Hospital Patient Management
Stores patient records and searches patients by disease.
"""

def search_by_disease(patients, disease):
    """Return names of patients having the specified disease."""
    matching_patients = []

    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            matching_patients.append(patient["Name"])

    return matching_patients


def main():
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]

    search_disease = "Flu"
    result = search_by_disease(patients, search_disease)

    print(f"Patients with {search_disease}: {result}")


if __name__ == "__main__":
    main()
