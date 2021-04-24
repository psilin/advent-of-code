
def read():
    numbers = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            numbers.append(int(line))

    numbers.sort()
    return numbers


def two_pointers(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            print(numbers[l], numbers[r], numbers[l] * numbers[r])
            return True, numbers[l], numbers[r]
        elif numbers[l] + numbers[r] < target:
            l = l + 1
        elif numbers[l] + numbers[r] > target:
            r = r - 1
    return False, None, None


def three_pointers(numbers, target):
    while len(numbers) >= 3:
        trgt = numbers.pop()
        if target - trgt <= 0:
            continue

        res, one, two = two_pointers(numbers, target - trgt)
        if res is True:
            print(one, two, trgt, one * two * trgt)
            return


if __name__ == '__main__':
    nums = read()
    two_pointers(nums, 2020)
    three_pointers(nums, 2020)
