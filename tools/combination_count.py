# tool: combination_count
# description: Count combinations of n items taken r at a time
# author: @Wkhanex
# example: combination_count "5" "3" -> "10"

import math


def run(*args) -> str:
    """Return the exact binomial coefficient for nonnegative integers."""
    if len(args) != 2:
        raise ValueError("expected two arguments: n and r")
    n, r = int(args[0]), int(args[1])
    if n < 0 or r < 0:
        raise ValueError("n and r must be nonnegative integers")
    return str(math.comb(n, r))
