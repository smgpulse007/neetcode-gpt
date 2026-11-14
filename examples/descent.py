"""Display the original scalar gradient-descent exercise on f(x) = x squared."""
from foundations import Solution


def main():
    solver = Solution()
    print("Scalar gradient descent: f(x) = x^2, learning rate = 0.1")
    print("Each row calls the original exercise from its initial value.\n")
    print(f"{'iterations':>10}  {'start +5':>12}  {'start -5':>12}")
    for iterations in (0, 1, 5, 10, 25, 50):
        positive = solver.get_minimizer(iterations, 0.1, 5)
        negative = solver.get_minimizer(iterations, 0.1, -5)
        print(f"{iterations:>10}  {positive:>12.5f}  {negative:>12.5f}")
    print("\nReturned values are rounded to five decimal places by the exercise.")
    print("This repository currently contains no GPT training or generation code.")


if __name__ == "__main__":
    main()
