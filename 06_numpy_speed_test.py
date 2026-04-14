# Assignment Date: 20/02/2026
# Assignment Name: NumPy Speed Test
# Description: Compare Python lists vs NumPy arrays with 1M numbers, measure
# execution time, write 3 observations.

import time
import numpy as np

SIZE = 1_000_000


def list_benchmark() -> float:
    a = list(range(SIZE))
    b = list(range(SIZE))

    start = time.time()
    _ = [x + y for x, y in zip(a, b)]
    return time.time() - start


def numpy_benchmark() -> float:
    a = np.arange(SIZE)
    b = np.arange(SIZE)

    start = time.time()
    _ = a + b
    return time.time() - start


def main() -> None:
    list_time = list_benchmark()
    numpy_time = numpy_benchmark()

    print(f"Python list add time : {list_time:.4f} seconds")
    print(f"NumPy array add time : {numpy_time:.4f} seconds")
    print(f"Speed-up             : {list_time / numpy_time:.2f}x faster with NumPy")

    print("\n--- 3 Observations ---")
    print(
        "1. NumPy is significantly faster because the add operation is "
        "vectorised in optimised C code rather than Python bytecode."
    )
    print(
        "2. Python lists store pointers to objects, so every addition involves "
        "dynamic type checks; NumPy stores fixed-type numbers in contiguous "
        "memory which is cache-friendly."
    )
    print(
        "3. For large numerical datasets, using NumPy reduces both runtime and "
        "memory consumption, which is essential for ML workloads."
    )


if __name__ == "__main__":
    main()
