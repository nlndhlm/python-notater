import matplotlib.pyplot as plt

# data
x = ['Arne', 'Bent', 'Charlie']
y = [190, 175, 160]


plt.bar(x, y, color='pink')

# for horisontale søyler bruk plt.barh(x, y)


plt.xlabel("Navn")
plt.ylabel("Høyde")

plt.show()