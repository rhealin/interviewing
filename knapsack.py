def dp_knapsack(N, W, val, wt):
    """
    Given weights and values of n items, put these items in a knapsack of capacity W 
    to get the maximum total value in the knapsack. In other words, given two integer 
    arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated 
    with n items respectively. Also given an integer W which represents knapsack capacity, 
    find out the maximum value subset of val[] such that sum of the weights of this 
    subset is smaller than or equal to W. You cannot break an item, either pick the 
    complete item, or don’t pick it (0-1 property).

    @param N number of items
    @param W max capacity 
    @param val values of items
    @param wt weights of items
    @return maximum total value in knapsack
    """
    wt, val = (list(t) for t in zip(*sorted(zip(wt, val))))

    # rows represent weights from 0 to W inclusive
    # cols represent items sorted by weight
    dp = [[0 for w in range(W+1)] for n in range(N)]
    
    for r in range(N):
        for c in range(W+1):
            if r == 0:
                if wt[r] <= c:
                    dp[r][c] = val[r]
            else:
                best_value = dp[r-1][c]
                if wt[r] <= c:
                    best_value = max(best_value, val[r] + dp[r-1][c-wt[r]])
                dp[r][c] = best_value
                
    # max value is in the bottom right corner
    return dp[-1][-1]

def naive_recursive_knapsack(N, W, val, wt):
    """
    Given weights and values of n items, put these items in a knapsack of capacity W 
    to get the maximum total value in the knapsack. In other words, given two integer 
    arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated 
    with n items respectively. Also given an integer W which represents knapsack capacity, 
    find out the maximum value subset of val[] such that sum of the weights of this 
    subset is smaller than or equal to W. You cannot break an item, either pick the 
    complete item, or don’t pick it (0-1 property).

    @param N number of items
    @param W max capacity 
    @param val values of items
    @param wt weights of items
    @return maximum total value in knapsack
    """
    # Base Case
    if N == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[N-1] > W):
        return naive_recursive_knapsack(N-1, W, val, wt)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[N-1] + naive_recursive_knapsack(N-1, W-wt[N-1], val, wt),
                   naive_recursive_knapsack(N-1, W, val, wt))
          
if __name__ == "__main__":
    val = [120, 100, 60]
    wt = [30, 20, 10]
    W = 50
    N = len(val)

    # returns 220
    print(dp_knapsack(N, W, val, wt))
    print(naive_recursive_knapsack(N, W, val, wt))