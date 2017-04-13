def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        n, j = map(int, raw_input("").split())
        res, arr = helper(n, j)
        print "Case #{}:".format(num)
        for i in range(len(res)):
            print "{} {}".format(res[i], ' '.join(map(str, arr[i])))


def helper(n, j):
    flag = False
    if n > 16:
        n = n / 2
        flag = True
    low = (1 << (n - 1)) + 1
    high = 1 << n
    nums = []
    divisorslist = []
    for i in range(low, high, 2):
        if j <= 0:
            break
        divisors = []
        for base in range(2, 11):
            num = int(bin(i)[2:], base)
            divisors.append(get_divisor(num))
        if None not in divisors:
            if flag:
                nums.append(bin(i)[2:] + bin(i)[2:])
            else:
                nums.append(bin(i)[2:])
            divisorslist.append(divisors)
            j -= 1
    return nums, divisorslist


def get_divisor(n):
    for i in range(2, min(n, 1000)):
        if n % i == 0:
            return i
    return None


if __name__ == '__main__':
    main()
