import matplotlib.pyplot as plt

# Number of items
n = int(input("Enter number of subjects: "))

subjects = []
marks = []

# Taking input
for i in range(n):
    name = input(f"Enter subject {i+1} name: ")
    score = int(input(f"Enter marks for {name}: "))

    subjects.append(name)
    marks.append(score)

# Create bar chart
plt.bar(subjects, marks)

# Labels
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks (Dynamic Data)")

# Show chart
plt.show()

