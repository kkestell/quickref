```python
import random

# Random integers
randint = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)

# Random floats
random_float = random.random()  # Generates a random float between 0 and 1 (exclusive)
uniform = random.uniform(1.0, 10.0)  # Generates a random float between 1.0 and 10.0 (inclusive)

# Random sequences
sequence = [1, 2, 3, 4, 5]
shuffle = random.shuffle(sequence)  # Shuffles the sequence in place
sample = random.sample(sequence, k=3)  # Returns a random sample of 3 elements from the sequence

# Random choices
choice = random.choice(sequence)  # Returns a random element from the sequence
choices = random.choices(sequence, weights=[1, 1, 2, 3, 5], k=5)  # Returns a list of 5 random elements from the sequence, with the weights determining the probability of each element being chosen

# Random strings
letters = 'abcdefghijklmnopqrstuvwxyz'
string = ''.join(random.choice(letters) for i in range(10))  # Generates a random string of length 10, consisting of lowercase letters

# Random seeds
random.seed(42)  # Sets the random seed to ensure reproducibility


```
