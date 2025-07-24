#Iterators & Iterable Protocol

#What Are Iterators & Iterables?
#Iterable:
#An object capable of returning its members one at a time, allowing it to be looped over using a for loop.

#Examples:

#list, tuple, set, str, dict, generators

#Iterator:
#An object with a state so it remembers where it is during iteration.

#To be an iterator, an object must implement two methods:

#__iter__()   # Returns the iterator object itself
#__next__()   # Returns the next value from the object, or raises StopIteration

# How Iteration Works Internally For Loop Example:

numbers = [1, 2, 3]
for num in numbers:
    print(num)

#Example 

class CountToN:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Using the iterator
counter = CountToN(5)
for num in counter:
    print(num)
