"""A tiny Python sample to play with.

Run it with:
    python hello.py
"""


def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main():
    # A list of names to greet
    names = ["Alice", "Bob", "Carol"]

    for name in names:
        print(greet(name))

    # Simple arithmetic with a list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [n * n for n in numbers]
    print(f"numbers: {numbers}")
    print(f"squares: {squares}")
    print(f"total:   {sum(squares)}")


if __name__ == "__main__":
    main()
