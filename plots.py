from typing import *
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import functions

sys.setrecursionlimit(10**9)


def time_function(f) -> float:
    total_time: float = 0.0

    for _ in range(4):
        start_time: float = time.perf_counter()
        f()
        end_time: float = time.perf_counter()
        total_time += end_time - start_time

    return total_time / 4


def n_values(n_max: int) -> List[int]:
    return [int(x) for x in np.linspace(1, n_max, 15)]


def make_descending_list(n: int) -> functions.LinkedList:
    if n == 0:
        return functions.empty
    return functions.link(n, make_descending_list(n - 1))


def plot_range() -> None:
    n_max: int = 10000
    x_coords: List[int] = n_values(n_max)
    y_coords: List[float] = []

    for n in x_coords:
        y_coords.append(time_function(lambda: functions.range(n)))

    plt.plot(np.array(x_coords), np.array(y_coords), label="range")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.title("Worst-Case Time for range")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_occurs() -> None:
    n_max: int = 10000
    x_coords: List[int] = n_values(n_max)
    y_coords: List[float] = []

    for n in x_coords:
        nums = functions.range(n)
        y_coords.append(time_function(lambda: functions.occurs(-1, nums)))

    plt.plot(np.array(x_coords), np.array(y_coords), label="occurs")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.title("Worst-Case Time for occurs")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_has_dup() -> None:
    n_max: int = 3000
    x_coords: List[int] = n_values(n_max)
    y_coords: List[float] = []

    for n in x_coords:
        nums = functions.range(n)
        y_coords.append(time_function(lambda: functions.has_dup(nums)))

    plt.plot(np.array(x_coords), np.array(y_coords), label="has_dup")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.title("Worst-Case Time for has_dup")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_insertion_sort() -> None:
    n_max: int = 3000
    x_coords: List[int] = n_values(n_max)
    y_coords: List[float] = []

    for n in x_coords:
        nums = make_descending_list(n)
        y_coords.append(time_function(lambda: functions.insertion_sort(nums)))

    plt.plot(np.array(x_coords), np.array(y_coords), label="insertion_sort")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.title("Worst-Case Time for insertion_sort")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_range()
    plot_occurs()
    plot_has_dup()
    plot_insertion_sort()