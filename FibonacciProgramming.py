# Fibonacci using Memoization
def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = (fibonacci_memoization(n - 1, memo) +
               fibonacci_memoization(n - 2, memo))

    return memo[n]


def fibonacci_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Input
n = int(input("Enter the value of n: "))

# Calculate Fibonacci using both methods
memo_result = fibonacci_memoization(n)
tabulation_result = fibonacci_tabulation(n)

# Display results
print("\nUsing Memoization:")
print("Fibonacci number =", memo_result)

print("\nUsing Tabulation:")
print("Fibonacci number =", tabulation_result)