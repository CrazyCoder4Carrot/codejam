def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        room = int(raw_input())
        parties = map(int, raw_input("").split())
        partycnt = []
        for i in range(len(parties)):
            partycnt.append((parties[i], chr(ord('A') + i)))
        partycnt.sort(key=lambda x: x[0], reverse=True)
        res = helper(room, partycnt, sum(parties))
        print "Case #{}: {}".format(num, res)


def helper(room, parties, total):
    res = []
    while parties:
        senators = parties[0][0]
        name = parties[0][1]
        if len(parties) == 2 and senators == parties[1][0]:
            res.append(name + parties[1][1])
            parties[0] = (senators - 1, name)
            parties[1] = (senators - 1, parties[1][1])
        else:
            res.append(name)
            parties[0] = (senators - 1, name)
        parties = filter(lambda x: x[0] != 0, parties)
        parties.sort(key=lambda x: x[0], reverse=True)
    return ' '.join(res)


if __name__ == '__main__':
    main()
