import matplotlib.pyplot as plt
import numpy as np

# normalfordelt IQ; snitt = 100, stdavvik = 15, n = 250:
# numpy genererer en liste for oss:
iq_scores = np.random.normal(100, 15, 250)

plt.hist(iq_scores)

plt.show()

