import sys


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        k = int(raw_input(""))
        res = helper(k)
        print "Case #{}: {}".format(num, res)

def helper(k):
    flags = [False] * 10
    prev = 0
    cur = k
    res = False
    while prev != cur and not res:
        for c in str(cur):
            flags[int(c)] = True
        res = reduce(lambda x, y: x & y, flags)
        prev = cur
        cur += k
    if not res:
        return 'INSOMNIA'
    else:
        return prev
