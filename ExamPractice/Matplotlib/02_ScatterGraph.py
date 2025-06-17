import matplotlib.pyplot as plt

l1 = [60, 40, 90, 30]
l2 = [16, 12, 18, 4]

plt.scatter(l1, l2, color='blue', s=100, marker='o')
plt.xlabel("Programming Practiced")
plt.ylabel("Marks Obtained")
plt.title("Scatter Plot Representation of Corelation between Hours of Programming Practice and Marks Obtained")
plt.show()