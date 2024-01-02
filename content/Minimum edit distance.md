# Minimum edit distance

Source: CSES

## Problem

Suppose you have two strings $s$ and $t$, both with at most 5000 characters. You can do three operations.

- Insert a character $c$ anywhere in the string
- Delete a character at any index in the string
- Change any character in the string to another character

What is the minimum number of operations to transform $s$ into $t$?

## Solution

### State

We can solve this problem using dynamic programming. Let $\mathrm{dp}_{ij}$ denote the minimum edit distance between a prefix of length $i$ from $s$ and a prefix of length $j$ from $t$.

### Base case

The base case is simply the empty string $\varepsilon$. If either string is empty, the best we can do is delete every character we have, which takes as many operations as the length of the string. Therefore

$$\begin{align*}\mathrm{dp}_{i0} = i \\\mathrm{dp}_{0j} = j\end{align*}$$

### Transition

We transition on all possible operations.

1. Delete a character from the longer string
2. Insert the last character of the longer string into the shorter string
3. Change the last character of both characters to match (if they are already the same, do not impose a cost)

$$\mathrm{dp}_{ij} =
\min \begin{cases} 
1 + \mathrm{dp}_{i-1, j} \\
1 +  \mathrm{dp}_{i, j-1} \\
\mathrm{dp}_{i-1, j-1} + 
\begin{cases}
1 & \text{if $s[i] \neq t[i]$}\\
0 & \text{if $s[i] = t[i]$}
\end{cases}\end{cases}$$

### Code

```python
def edit_distance(s, t):
        n = len(s)
        m = len(t)
        dp = [[m for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                delete = dp[i-1][j] + 1
                insert = dp[i][j-1] + 1
                substitute = dp[i-1][j-1] + 1

                if s[i-1] == t[j-1]: 
                    substitute -= 1
                
                dp[i][j] = min(min(delete, insert), substitute)
        return dp[n][m]
```

