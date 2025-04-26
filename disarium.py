def is_disarium(num):
    return num == sum(int(digit) ** (i + 1) for i, digit in enumerate(str(num)))

def first_n_disarium(n):
    disarium_nums = []
    num = 0
    while len(disarium_nums) < n:
        num += 1
        if is_disarium(num):
            disarium_nums.append(num)
    return disarium_nums

def disarium_between(a, b):
    return [num for num in range(a, b + 1) if is_disarium(num)]
n = 5
print("First", n, "disarium numbers:")
