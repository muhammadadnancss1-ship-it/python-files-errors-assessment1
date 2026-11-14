import csv


try:
    # Read every line from the original attendance file.
    with open("attendance.txt", "r", encoding="utf-8") as file:
        original_names = file.readlines()

except FileNotFoundError:
    # Show a helpful message if the input file does not exist.
    print("attendance.txt was not found. Create it with one student name per line.")

else:
    # List comprehension: trim spaces, fix capitalization, and skip blank lines.
    cleaned_names = [name.strip().title() for name in original_names if name.strip()]

    # A set removes duplicate names after cleaning.
    unique_students = set(cleaned_names)

    # sorted() returns the unique names as an alphabetical list.
    sorted_students = sorted(unique_students)

    # Save the result to CSV. newline="" prevents extra blank rows.
    with open("attendance_clean.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Student Name"])  # Add the column heading.

        for name in sorted_students:
            writer.writerow([name])  # Write one name in each row.

    # Count the original lines and the unique students.
    print("Original number of records:", len(original_names))
    print("Unique student count:", len(unique_students))

    # Display the final cleaned and sorted names.
    print("\nCleaned attendance list:")
    for name in sorted_students:
        print(name)

    print("\nSaved to attendance_clean.csv")
