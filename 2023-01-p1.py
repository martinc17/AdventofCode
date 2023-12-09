total = 0
with open(r"data\2023-01.p1_input.txt", "r") as f:
    for x in f:
        numbers = dict([(pos, char) for pos, char in enumerate(x) if char.isdigit()])
        first_dig = numbers.get(min(numbers))
        last_dig = numbers.get(max(numbers))
        calib_value = int(first_dig + last_dig)
        total += calib_value
print(total)