# Student Marks Analyzer

# List of student marks
marks = [85, 72, 45, 30, 95, 60, 110, -5]

# Counters for each category
distinction_count = 0
pass_count = 0
fail_count = 0

# Process each mark using a loop
for mark in marks:

    # Ignore invalid marks
    if mark < 0 or mark > 100:
        print("Invalid mark ignored:", mark)
        continue

    # Categorize the valid marks
    if mark >= 75:
        print(mark, "- Distinction")
        distinction_count += 1

    elif mark >= 40:
        print(mark, "- Pass")
        pass_count += 1

    else:
        print(mark, "- Fail")
        fail_count += 1


# Display the number of students in each category
print("\nNumber of Distinction students:", distinction_count)
print("Number of Pass students:", pass_count)
print("Number of Fail students:", fail_count)