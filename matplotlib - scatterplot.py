import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [4,2,5,7,3,5,2,2,4]

# denne vil plottes blå
plt.scatter(x, y)

z = [5,3,5,3,2,5,6,7,8]
w = [1,2,4,6,3,6,3,4,5]

# denne plottes automatisk oransje
plt.scatter(z, w)

plt.show()