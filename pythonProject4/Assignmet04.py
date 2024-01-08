# Queens College
# Discrete Structures (CSCI 220)
# Winter 2024
# Assignment #4: Permutations and Combinations
# Maheli Tisha
# Collaborated with Class


import inspect
import pandas as pd
from itertools import product
from math import factorial, perm, comb
import texttable


def print_table(title, headers, data, alignments):
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows([headers] + data, True)
    print(title)
    print(tt.draw())
    print()


def c(n, r):
    return comb(n, r)


def p(n, r):
    return perm(n, r)


def c2(n, r):
    return 0 if r > n else fact(n) / (fact(r) * fact(n - r))


def p2(n, r):
    return 0 if r > n else fact(n) / fact(n - r)


def fact(n):
    return 0 if n < 0 else factorial(n)


# [1] Create a function print_table(name, func, n) that prints a
# (n+1) x (n+1) table for the function f(i, j) where both i and j iterate over 0 thru n inclusive.
#
# Print the name of the table
# Add column headings
# Use Python's rjust() function to right-justify your columns so your table looks neat.
# Print a blank line after the table


# [2] From your main function, call print_table using "Permutations" and the built-in math.perm


def functions(f, c, n, t):
    headers = [f"{c}(n, {r})" for r in range(n + 1)]
    data = [[f(i, j) for j in range(n + 1)] for i in range(n + 1)]
    alignments = ["r"] * (n + 1)
    print_table(t, headers, data, alignments)


# [3] From your main function, call print_table using "Permutations" and your own my_perm


# [4] From your main function, call print_table using "Combinations" and the built-in math.comb


# [5] From your main function, call print_table using "Combinations" and your own my_comb


# [6] In the standard game of poker, one is dealt a "hand" of five cards which is classified into one of several categories. For example, "Four of a Kind" means four cards of one rank and one card of another rank. "Full House'' means three cards of one rank, and two cards of another rank. We want to compute the number of possible ways to get a given hand. Then, use this function to compare your calculated answer with the known correct answer and then call it for all standard hands.


def q6():
    hands = [["royal flush", 4, c(4, 1)],
             ["straight flush", 36, c(10, 1) * c(4, 1) - c(4, 1)],
             ["four of a kind",624 , c(13, 1) * c(4, 4) - c(12, 1) * c(4,1)],
             ["full house", 3744, c(13, 1) * c(4, 3) * c(12, 1) * c(4, 2)],
             ["two pairs", 3744, c(13, 1) * c(4, 3) * c(12, 1) * c(4, 2)],
             ["flush", 5108, c(4, 1) * c(13, 5) - c(10, 1) * c(4, 1)],
             ["straight", 3744, c(13, 1) * c(4, 3) * c(12, 1) * c(4, 2)],
             ["three of a kind", 3744, c(13, 1) * c(4, 3) * c(12, 1) * c(4, 2)],
             ["one pair", 5108, c(4, 1) * c(13, 5) - c(10, 1) * c(4, 1)],
             ["no pair", , ]
             ]
    for hand in hands:
        print(hand[0], hand[1], hand[2], hand[1] == hand[2])


def main():
    n = 10
    functions(p, "P", n, "Permutations using built in perm")
    functions(p2, "P", n, "Permutations using our perm functions")
    functions(c, "C", n, "combination using built in perm")
    functions(c2, "C", n, "combination using our perm functions")


if __name__ == "__main__":
    main()

