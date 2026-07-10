def inn_check_digit(base8: str) -> int:
    weights = [37, 29, 23, 19, 17, 13, 7, 3]

    s = sum(int(d) * w for d, w in zip(base8, weights))

    q = s / 11
    k = int(9 - (q - int(q)) * 9)

    return k

base = "84114374"
print(base + str(inn_check_digit(base)))