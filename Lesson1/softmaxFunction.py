"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np
import math

def softmax(x):
	try:
		x = [list(i) for i in zip(*x)]
		probList = []
		for i in x:
			probList.append(softmaxCol(i))

		return np.transpose(np.asarray(probList))
	except:
		return softmaxCol(x)
def softmaxCol(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    totalSum = 0.0
    for score in x:
    	totalSum += math.exp(score)
    probList = []
    for score in x:
    	probList.append(math.exp(score)/totalSum)
    return np.asarray(probList)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
