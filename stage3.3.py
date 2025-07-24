#Generators

#yield keyword
#Memory efficiency
#Difference from return

# 1.  What Are Generators?
#Generators are special types of iterators that allow you to iterate over data without 
#storing the entire dataset in memory. They are created using functions with the yield keyword.

#2. yield Keyword
#What does yield do?
#yield is used instead of return in a function to make it a generator.
#Each time yield is called, it pauses the function and returns a value.
#When the generator is resumed (next time), it continues right after the yield.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)

for number in counter:
    print(number)

#Internally, this function:
#Does not return all values at once
#Creates a generator object
#Returns one value at a time on demand

#3. Memory Efficiency
#Generators are lazy iterators, meaning:
#They generate values only when needed
#They do not store the entire result in memory

# List (eager evaluation - uses more memory)
nums = [x * 2 for x in range(1000000)]  # Creates and stores all values

# Generator (lazy evaluation - memory efficient)
nums = (x * 2 for x in range(1000000))  # Uses generator expression

#With a generator, Python:
#Keeps only one value in memory at a time
#Ideal for big data, log processing, file reading, etc.

#4. Difference Between return and yield
#Feature	                     return	                                        yield
#Terminates the function	     Yes	                                        No,pauses and resumes
#Returns	                     Single value	                                Generator object (stream of values)
#Memory usage	                 High (all values stored)	                    Low (values generated on the fly)
#Use case	                     One-time value	                                Series of values
#Multiple calls	                 Starts over each time	                        Resumes from last yield

#Real word example 

def infinite_counter(start=1):
    while True:
        yield start
        start += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))
