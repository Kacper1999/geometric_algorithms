# this program finds a path from s to t such that
# the edge with smallest weight on this path is biggest amongst others

from lab1.dimacs import *


def load_and_print_edges(name):
    (V, L) = load_weighted_graph(name)  # load graph
    print_edges(L)


def print_edges(edges):
    for (x, y, c) in edges:  # search through edges
        print("edge between", x, "and", y, "with weight", c)


def sort_edges_descending(edges):
    print_edges(sorted(edges, key=lambda tup: tup[2], reverse=True))


def main():
    (V, L) = load_weighted_graph("g1")
    sort_edges_descending(L)


if __name__ == "__main__":
    main()
