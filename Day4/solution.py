
def findEmbeddedAssignedPairs():
    """"""
    total = 0
    with open('./puzzle.txt') as pairs_list:
        pairs = pairs_list.read().splitlines()
        for pair in pairs:
            pair_1, pair_2 = pair.split(',')
            a,b = pair_1.split('-')
            c,d = pair_2.split('-')
            if(int(a) >= int(c)) and ((int(b) <= int(d))):
                total += 1
            elif (int(c) >= int(a)) and ((int(d) <= int(b))):
                total += 1
    return total

def findOverlapRanges():
    """"""
    total = 0
    with open('./puzzle.txt') as pairs_list:
        pairs = pairs_list.read().splitlines()
        for pair in pairs:
            pair_1, pair_2 = pair.split(',')
            a,b = pair_1.split('-')
            c,d = pair_2.split('-')
            # 4-6,5-8 (A partially in B)
            if (int(a) <= int(d)) and (int(b) >= int(c)):
                total += 1
            # 3-8,2-4 (B partially in A)
            elif (int(c) <= int(a)) and (int(d) >= int(a)):
                total += 1
    return total


if __name__ == "__main__":
    print("Part1  ", findEmbeddedAssignedPairs())
    print("Part2  ", findOverlapRanges())