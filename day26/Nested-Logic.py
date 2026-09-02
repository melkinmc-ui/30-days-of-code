import sys

def calculate_fine():
    # Leer fecha de devolucion (actual return date)
    d1, m1, y1 = map(int, input().split())
    # Leer fecha limite (due date)
    d2, m2, y2 = map(int, input().split())

    fine = 0

    if y1 > y2:
        fine = 10000
    elif y1 == y2:
        if m1 > m2:
            fine = 500 * (m1 - m2)
        elif m1 == m2 and d1 > d2:
            fine = 15 * (d1 - d2)

    print(fine)

if __name__ == '__main__':
    calculate_fine()