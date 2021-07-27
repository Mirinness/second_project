import random
import math
'''Generate sequence 5 integers long from range(0, 100)'''
int_seq = (random.sample(range(100), 5))
print(int_seq)

'''Generate random float'''
float_random = random.random()
print(float_random)

'''Find max element from generated sequence'''
int_seq_max = max(int_seq)
print(int_seq_max)

'''Make a floor division between max element and generated float'''
floor_div_result = int_seq_max // float_random

'''Find factorial of the result above'''
print(math.factorial(floor_div_result))