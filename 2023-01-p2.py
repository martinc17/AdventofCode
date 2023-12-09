word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


total = 0
lines = 0
with open(r"data\2023-01.p1_input.txt", "r") as f:
    for e in f:
        for w, d in word_to_digit.items():
            for i in range(e.count(w)):
                index = e.find(w)
                if index == -1:
                    pass
                else:
                    e = e[0 : index + 1] + d + e[index + len(w) - 1 :]
        numbers = dict([(pos, char) for pos, char in enumerate(e) if char.isdigit()])
        first_dig = numbers.get(min(numbers))
        last_dig = numbers.get(max(numbers))
        calib_value = int(first_dig + last_dig)
        total += calib_value

print(total)
