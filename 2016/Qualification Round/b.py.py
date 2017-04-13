def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        p = raw_input("")
        res = helper(p)
        print "Case #{}: {}".format(num, res)


def helper(p):
    groupHeight = 1 + p.count('-+') + p.count('+-')
    if p.endswith('-'):
        return groupHeight
    else:
        return groupHeight - 1


if __name__ == '__main__':
    main()
