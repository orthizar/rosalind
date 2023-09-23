## Rabbits and Recurrence Relations
https://rosalind.info/problems/fib/

### Solution
We use a recursive fibonacci function, modified to allow the population of F_n-2 to have multiple pairs of offspring. The modified fibonacci function `fib(n)` returns `fib(n-1) + fib(n-2) * k`, where `k` is the number of pairs of offspring and `n` is the number of months.