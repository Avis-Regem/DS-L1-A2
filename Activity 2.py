#performing arithmetic operations on an array
import numpy as np
a = np.arange(9, dtype = np.float64).reshape(3,3)
print('First Array:')
print(a)
print('\n')

b = np.array([10, 10, 10])
print('Second Array:')
print(b)
print('\n')

print('Add the two arrays:')
print(np.add(a, b))
print('\n')

print('Subtract the 2 arrays:')
print(np.subtract(a, b))
print('\n')

print('Multiply the 2 arrays: ')
print(np.multiply(a, b))
print('\n')

print('Divide the 2 arrays:')
print(np.divide(a, b))
print('\n')