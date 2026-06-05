import functions
import time
import matplotlib.pyplot as plt


# Returns 15 evenly-spaced N values from 1 to n_max inclusive.
def make_n_values(n_max: int) -> list[int]:
    return [round(1 + i * (n_max - 1) / 14) for i in range(15)]


# Returns the average runtime in seconds of has_dup on
# a worst-case linked list of size n.
def time_has_dup(n: int) -> float:
    total = 0.0

    for trial in range(4):
        nums = functions.range(n)

        start_time = time.perf_counter()
        functions.has_dup(nums)
        end_time = time.perf_counter()

        total += end_time - start_time
        print(f"  trial {trial + 1}/4 for n={n} done")

    return total / 4


# Creates and displays a graph of the worst-case runtime
# of has_dup as a function of N.
def main() -> None:
    # Adjust n_max until the largest input takes about 1.5–3 seconds.
    n_max = 2000

    x_values = make_n_values(n_max)
    y_values = []

    for n in x_values:
        print(f"Timing n={n}...")
        seconds = time_has_dup(n)
        y_values.append(seconds)
        print(f"Average for n={n}: {seconds:.6f} seconds")

    plt.plot(x_values, y_values, marker="o", label="has_dup")
    plt.title("Worst-Case Time Complexity of has_dup")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.legend()
    plt.savefig("worst_case_has_dup.png")
    plt.show()


if __name__ == "__main__":
    main()

