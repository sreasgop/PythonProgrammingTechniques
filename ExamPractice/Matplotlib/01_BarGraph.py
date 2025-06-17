import matplotlib.pyplot as plt

subjects = ["English", "Math", "History", "Science", "Computer Science"]
marks = [58, 56, 60, 90, 100]

plt.bar(subjects, marks, color='crimson')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Graph Representation of Sreas's Marks")

plt.show()