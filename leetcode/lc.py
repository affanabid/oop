def add_digit(digits):
    pointer = len(digits) - 1
    while pointer >= 0:
        digit = digits[pointer] + 1
        if digit > 9:
            digits[pointer] = 0
            pointer -= 1
        else:
            digits[pointer] = digit
            break
    if pointer == -1:
        digits.insert(0, 1)
    return digits

d = [9, 9, 8]
print(add_digit(d))