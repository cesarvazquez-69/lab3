import functions
import time
import matplotlib.pyplot as plt


# Returns 15 evenly-spaced N values from 1 to n_max inclusive.
def make_n_values(n_max: int) -> list[int]:
    return [round(1 + i * (n_max - 1) / 14) for i in range(15)]


# Returns a descending linked list from n down to 1.
def make_descending_list(n: int) -> functions.LinkedList:
    if n == 0:
        return functions.Empty()
    return functions.Link(n, make_descending_list(n - 1))


# Returns the average runtime of a function across 4 trials.
def average_time(f) -> float:
    total = 0.0

    for trial in range(4):
        start_time = time.perf_counter()
        f()
        end_time = time.perf_counter()

        total += end_time - start_time

    return total / 4


# Creates and saves the worst-case runtime graph for range.
def plot_range() -> None:
    n_max = 10000
    x_values = make_n_values(n_max)
    y_values = []

    for n in x_values:
        print(f"Timing range n={n}...")
        y_values.append(average_time(lambda: functions.range(n)))

    plt.plot(x_values, y_values, marker="o", label="range")
    plt.title("Worst-Case Time Complexity of range")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.legend()
    plt.savefig("worst_case_range.png")
    plt.clf()


# Creates and saves the worst-case runtime graph for occurs.
def plot_occurs() -> None:
    n_max = 10000
    x_values = make_n_values(n_max)
    y_values = []

    for n in x_values:
        nums = functions.range(n)
        print(f"Timing occurs n={n}...")
        y_values.append(average_time(lambda: functions.occurs(-1, nums)))

    plt.plot(x_values, y_values, marker="o", label="occurs")
    plt.title("Worst-Case Time Complexity of occurs")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.legend()
    plt.savefig("worst_case_occurs.png")
    plt.clf()


# Creates and saves the worst-case runtime graph for has_dup.
def plot_has_dup() -> None:
    n_max = 2000
    x_values = make_n_values(n_max)
    y_values = []

    for n in x_values:
        nums = functions.range(n)
        print(f"Timing has_dup n={n}...")
        y_values.append(average_time(lambda: functions.has_dup(nums)))

    plt.plot(x_values, y_values, marker="o", label="has_dup")
    plt.title("Worst-Case Time Complexity of has_dup")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.legend()
    plt.savefig("worst_case_has_dup.png")
    plt.clf()


# Creates and saves the worst-case runtime graph for insertion_sort.
def plot_insertion_sort() -> None:
    n_max = 2000
    x_values = make_n_values(n_max)
    y_values = []

    for n in x_values:
        nums = make_descending_list(n)
        print(f"Timing insertion_sort n={n}...")
        y_values.append(average_time(lambda: functions.insertion_sort(nums)))

    plt.plot(x_values, y_values, marker="o", label="insertion_sort")
    plt.title("Worst-Case Time Complexity of insertion_sort")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.legend()
    plt.savefig("worst_case_insertion_sort.png")
    plt.clf()


# Generates all four required graphs.
def main() -> None:
    plot_range()
    plot_occurs()
    plot_has_dup()
    plot_insertion_sort()


if __name__ == "__main__":
    main()