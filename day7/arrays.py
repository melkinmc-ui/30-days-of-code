import sys


def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    arr = input_data[1 : n + 1]

    arr_reversed = arr[::-1]

    print(" ".join(arr_reversed))


if __name__ == "__main__":
    main()