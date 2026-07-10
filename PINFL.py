def calculate_pinfl_check_digit(pinfl13):
    """
    pinfl13 - первые 13 цифр ПИНФЛ в виде строки
    """
    if len(pinfl13) != 13 or not pinfl13.isdigit():
        raise ValueError("Необходимо передать ровно 13 цифр")

    weights = [7, 3, 1] * 5  # 15 элементов
    weights = weights[:13]   # берем первые 13

    total = sum(int(digit) * weight
                for digit, weight in zip(pinfl13, weights))

    return total % 10


# Пример
pinfl13 = "5150900456545"
check_digit = calculate_pinfl_check_digit(pinfl13)

print(f"Контрольная цифра: {check_digit}")
print(f"Полный ПИНФЛ: {pinfl13}{check_digit}")