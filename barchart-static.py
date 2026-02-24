import matplotlib.pyplot as plt

# Given data (static)
subjects = ["Math", "Physics", "Chemistry", "Biology", "CS"]
marks = [85, 78, 90, 72, 88]

# Create bar chart
plt.bar(subjects, marks)

# Labels
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks (Static Data)")

# Show chart
plt.show()

