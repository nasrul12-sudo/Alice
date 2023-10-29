import numpy as np

x = list(map(int, input(">>> ").split()))

# bobot
W = []
for i in range(len(x)):
    w = np.random.rand(len(x))
    W.append(w)
print(W)

temp = 0
for i in range(0, len(W)):
    for j in range(0, len(x)):
        data = x[i] * W[i][j]
    print(data)
        