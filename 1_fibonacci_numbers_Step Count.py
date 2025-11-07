# Q1/A1. Write a program to calculate Fibonacci numbers and find its step count.


import time

# ---------- Recursive Fibonacci with Step Count ----------
count_recursive = 0
def fib_recursive(n):
    global count_recursive
    count_recursive += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Non-Recursive Fibonacci with Step Count ----------
def fib_non_recursive(n):
    count = 0
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        count += 1
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()
    return count

# ---------- Main Function ----------
def main():
    global count_recursive
    n = int(input("Enter the number of Fibonacci terms: "))

    # ----- Recursive -----
    print("\nFibonacci Sequence (Recursive): ", end="")
    start1 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end1 = time.time()
    time_recursive = (end1 - start1) * 1_000_000  # in microseconds

    # ----- Non-Recursive -----
    print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
    start2 = time.time()
    count_nonrec = fib_non_recursive(n)
    end2 = time.time()
    time_nonrecursive = (end2 - start2) * 1_000_000  # in microseconds

    # ---------- Output Analysis ----------
    print("\n=== Step Count and Complexity Analysis ===")
    print(f"Recursive Step Count: {count_recursive}")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Step Count: {count_nonrec}")
    print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()
