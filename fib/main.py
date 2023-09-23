# arguments = "5 3"
arguments = open('rosalind_fib.txt').read().strip()
n, k = map(int, arguments.split(" "))

def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2) * k

print(fib(n))