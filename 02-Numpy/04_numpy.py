import numpy as np

# Numpy Dizi Metodları
benim_numpy_dizim = np.arange(30)
benim_random_dizim = np.random.randint(0, 100, 20)

print(benim_numpy_dizim.reshape(5, 6))
print(benim_numpy_dizim.max())
print(benim_random_dizim.max())
print(benim_random_dizim.min())
print(benim_random_dizim.argmax())
print(benim_random_dizim.argmin())
print(benim_numpy_dizim.shape)
reshape_dizim = benim_numpy_dizim.reshape(5, 6)
print(reshape_dizim.shape)
