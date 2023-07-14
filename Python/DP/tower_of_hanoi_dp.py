def tower_of_hanoi_dp(n, source, aux, dest):
    dp = [[None for _ in range(3)] for _ in range(n + 1)]

    # Base case
    dp[1][source] = [source, dest]

    # Fill in the DP table
    for i in range(2, n + 1):
        for src in range(3):
            if src == dest:
                continue

            moves = []
            for aux in range(3):
                if aux != src and aux != dest:
                    submoves = dp[i - 1][src][:]
                    submoves.append(aux)
                    moves.append(submoves)

            dp[i][src] = moves

    # Print the solution
    print(dp[n][source])


if __name__ == "__main__":
    n = 3
    source = "A"
    aux = "B"
    dest = "C"
    tower_of_hanoi_dp(n, source, aux, dest)
