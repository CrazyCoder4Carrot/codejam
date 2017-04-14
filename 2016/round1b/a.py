# "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
import collections


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        string = raw_input("")
        res = helper(string)
        print "Case #{}: {}".format(num, res)


def helper(string):
    list = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
            "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    uniquec = ['Z', 'W', 'X', 'G', 'S', 'V', 'T', 'F', 'O', 'I']
    uniquen = [0, 2, 6, 8, 7, 5, 3, 4, 1, 9]
    res = []
    dict = collections.defaultdict(int)
    for c in string:
        dict[c] += 1
    for i in range(len(uniquec)):
        c = uniquec[i]
        n = uniquen[i]
        cnt = dict[c]
        if dict[c] == 0:
            continue
        res += [n] * dict[c]
        for char in list[n]:
            dict[char] -= cnt
    return ''.join(map(str, sorted(res)))


if __name__ == '__main__':
    main()
