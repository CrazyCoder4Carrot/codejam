def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        b, m = map(int, raw_input("").split())
        matrix, res = helper(b, m)
        print "Case #{}: {}".format(num, res)
        if matrix:
            for row in matrix:
                print ''.join(map(str, row))


def helper(b, m):
    if m > (1 << (b - 2)):
        return [], 'IMPOSSIBLE'
    matrix = [[0 for _ in range(b)] for _ in range(b)]
    for i in range(1, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            matrix[i][j] = 1
    if m == (1 << (b - 2)):
        matrix[0] = [0] + [1] * (b - 1)
    else:
        index = b - 2
        for i in bin(m)[2:][::-1]:
            matrix[0][index] = int(i)
            index -= 1
    return matrix, 'POSSIBLE'


if __name__ == '__main__':
    main()
