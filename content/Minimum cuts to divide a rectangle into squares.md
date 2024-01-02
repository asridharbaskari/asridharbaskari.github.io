# Minimum cuts to divide a rectangle into squares

Problem source: [CSES](https://cses.fi/problemset/submit/1744/)

# Problem
Given a rectangle with integer side lengths $n$ and $m$, suppose you can divide it into two rectangles with integer side lengths by cutting along one direction.

What is the minimum number of cuts required to divide it into squares?
# Solution
## State
We can solve the problem using dynamic programming. Define $\mathrm{dp}_{nm}$ to be the minimum number of cuts to divide an $n \times m$ rectangle into squares. 
## Base case
We can consider two base cases.
- **The rectangle is a square**: In this case, we don't have to do anything, so $\mathrm{dp}_{nn} = 0$
- **One of the side lengths is 1**: In this case, the best we can do is slice it into $1 \times 1$ squares, which takes $s - 1$ moves if $s$ is the longer side. Therefore, $\mathrm{dp}_{1m} = \mathrm{dp}_{m1} = m-1$
## Transition
Observe that there are a fixed number of starting moves. We can cut along the horizontal and vertical directions on any of the integers $1 \leq i < n$ or $1 \leq j < m$. 

Thus, 
$$\begin{align*}
\mathrm{dp}_{nm} = \min(&\min\limits_{i=1}^{n-1} [1 + \mathrm{dp}_{im} + \mathrm{dp}_{(n-i)m}], \\
                      &\min\limits_{j=1}^{m-1} [1 + \mathrm{dp}_{nj} + \mathrm{dp}_{n(m-j)}])
\end{align*}
$$
## Code
```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios::sync_with_stdio(false); 
	cin.tie(0);
	int a, b; cin >> a >> b;
	vector<vector<int>> dp(a + 1, vector<int>(b + 1, INT_MAX));
	for (int i = 1; i <= a; i++) {
		for (int j = 1; j <= b; j++) {
			if (i == j) {
				dp[i][j] = 0;
			}
			else if (i == 1 || j == 1) {
				dp[i][j] = (i==1) ? (j-1) : (i-1);
			}
			else {
				for (int k = 1; k < i; k++) {
					dp[i][j] = min(dp[i][j], 1+dp[k][j]+dp[i-k][j]);
				}
				for (int k = 1; k < j; k++) {
					dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[i][j-k]);
				}
			}
		}
	}
	cout << dp[a][b] << endl;
}
```

