def main():
    print("Type two numbers for x and y")

    x = int(input("x > "))
    y = int(input("y > "))

    print("%d + %d = %d" % (x, y, add(x, y)))
    print("%d - %d = %d" % (x, y, minus(x, y)))
    print("%d * %d = %d" % (x, y, times(x, y)))
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def times(a, b):
    return a * b


def divide(x, y):
    if y == 0:
        print("Error: cannot divide by zero.")
        return 0
    else:
        return x / y


if __name__ == "__main__":
    main()
