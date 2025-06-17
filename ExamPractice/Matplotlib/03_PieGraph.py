import matplotlib.pyplot as plt

l1 = ['Sleeping', 'Eating', 'Working', 'Playing']
l2 = [8, 2, 10, 4]
c = ['b', 'g', 'y', 'r']

plt.pie(l2, labels=l1, colors=c, autopct='%.1f', startangle=90)
plt.title("Pie Chart Representation of Hours spent in different activity")
plt.show()