import collections


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        N = int(raw_input(""))
        matrix = []
        for i in range(2 * N - 1):
            row = map(int, raw_input().split())
            matrix.append(row)
        res = helper(matrix)
        print "Case #{}: {}".format(num, res)


def helper(matrix):
    dict = collections.defaultdict(int)
    res = []
    for row in matrix:
        for num in row:
            dict[num] += 1
    for key in dict:
        if dict[key] != 0 and dict[key] % 2 != 0:
            res.append(key)
    res.sort()
    return ' '.join(map(str, res))


if __name__ == '__main__':
    main()
