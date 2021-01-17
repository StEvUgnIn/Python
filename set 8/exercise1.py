import numpy as np

arr = np.array([3,8,7,2,5,4,1,9])

print(np.sort(arr))

A = np.array([[4, 0, 3, 1],
            [2, 4, 3, 2],
            [3, 1, 2, 0],
            [1, 2, 4, 2]])

print(np.sort(A))

print(np.sort(np.random.randint(0, 11, size=(6, 10))))
print(np.sort(np.random.randint(100, 201, size=(6, 10))))
print(np.sort(np.random.randint(-50, -9, size=(6, 10))))