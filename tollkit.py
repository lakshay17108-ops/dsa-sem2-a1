"""AERT - Algorithmic Efficiency & Recursion Toolkit
Course: ETCCDS202 - Data Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data Structures (ETCCDS202)

Name of the School:	School of Engineering & Technology 
Program: B.Tech CSE (AI and ML) 
Course Title: Data Structures 
Course Code: ETCCDS202 
Unit Title: Foundations & Algorithmic Analysis 
Student Name: Lakshay
Roll Number: 2501730367
Section: A 
Semester: 2 
Batch: 2025-26 
Submitted To: Mrs. Neetu Chauhan """



# Part A: Stack ADT

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Part B: Factorial (Recursive)
def factorial(n):
    if n<0:
        return "factorial not defined"
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)



# Fibonacci - Naive (with counter)
def fib_naive(n, count_list):
    count_list[0] += 1 
    if n <= 1:
        return n
    return fib_naive(n - 1, count_list) + fib_naive(n - 2, count_list)


# Fibonacci - Memoized (with counter)
def fib_memo(n, memo, count_list):
    count_list[0] += 1  
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo, count_list) + fib_memo(n - 2, memo, count_list)
    return memo[n]



# Part C: Tower of Hanoi
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# Part D: Recursive Binary Search
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)


# Using StackADT for Fibonacci Trace
def fib_trace(n, stack):
    stack.push(f"fib({n})")

    if n <= 1:
        return n

    return fib_trace(n - 1, stack) + fib_trace(n - 2, stack)


# MAIN FUNCTION

def main():

    print("----------PART A: Stack ADT----------")
    stack = StackADT()
   
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Current size:", stack.size())
    print("Top element:", stack.peek())
    
    print("Popped:", stack.pop())
    print("Size after pop:", stack.size())
    
    print("Is stack empty?", stack.is_empty())

    print("\n----------Fibonacci Recursion Trace using Stack----------")
    trace_stack = StackADT()
    result = fib_trace(5, trace_stack)
    print("Fibonacci Result:", result)
    print("Trace (Top to Bottom):")
    while not trace_stack.is_empty():
        print(trace_stack.pop())

    print("\n----------PART B: Factorial----------")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) =", factorial(n))

    print("\n----------Fibonacci Comparison----------")
    for n in [10, 20, 30]:
        naive_calls = [0]
        memo_calls = [0]
    
        fib_naive(n, naive_calls)
        fib_memo(n, {}, memo_calls)
    
        print(f"n = {n}:")
        print(f"  Naive Calls: {naive_calls[0]}")
        print(f"  Memo Calls:  {memo_calls[0]}")
        print("-" * 20)

    print("\n----------PART C: Tower of Hanoi (N=3)----------")
    hanoi(3, 'A', 'B', 'C')

    print("\n----------PART D: Recursive Binary Search----------")

    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        index = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} -> Index:", index)

    empty_arr = []
    print("Search in empty array ->",
        binary_search(empty_arr, 5, 0, -1))


if __name__ == "__main__":
    main()
