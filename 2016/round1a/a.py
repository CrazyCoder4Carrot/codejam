def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        S = raw_input("")
        res = helper(S)
        print "Case #{}: {}".format(num, res)


def helper(S):
    temp = list(S)
    res = [temp[0]]
    for i in range(1, len(temp)):
        if temp[i] >= res[0]:
            res = [temp[i]] + res
        else:
            res = res + [temp[i]]
    return ''.join(res)
if __name__ == '__main__':
    main()
