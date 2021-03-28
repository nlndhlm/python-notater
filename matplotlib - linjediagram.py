import matplotlib.pyplot as plt

xpoints = [0, 5, 10]
ypoints = [0, 3, 25]

plt.plot(xpoints, ypoints)

# vi må ha likt antall punkter i hver liste:
xpoints = [0, 2, 10]
ypoints = [0, 3, 20]

# markere punkter på linja:
plt.plot(xpoints, ypoints, marker='o')

plt.grid(axis='x')
plt.grid(axis='y')
# kan forkortes ned til:
#plt.grid(axis='both')

plt.show()