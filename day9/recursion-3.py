#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    # Caso base: si n es 1 o menor, retornamos 1
    if n <= 1:
        return 1
    # Llamada recursiva: n * factorial(n - 1)
    return n * factorial(n - 1)


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        result = factorial(n)
        print(result)
