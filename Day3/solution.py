
def findCommonItemsInSingleSacks():
    """In a Sack of 2 compartments find common items and get their priority score"""
    # ord('a')-96, ord('A')-38
    score = 0
    with open('./puzzle.txt') as sacks_list:
        sacks = sacks_list.read().splitlines()
        for sack in sacks:
            # Set Intersection
            common_items = set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])
            for item in common_items:
                if ord(item) >= 97 and ord(item) <= 122:
                    score += ord(item)-96
                else:
                    score += ord(item)-38
    return score

import functools
def findCommonItemsInGroups():
    """In a Groups of 3 Sacks find common items and get their priority score"""
    # ord('a')-96, ord('A')-38
    score = 0
    with open('./puzzle.txt') as sacks_list:
        sacks = sacks_list.read().splitlines()
        i = 0
        while((i*6)+6 <= len(sacks)):
            # 1. Map 1Group == 3Sacks -> 3Sets
            # 2. Reduce 3Sets by intersecting each group common items
            # 3. Union All common items & find score based on assigned priority
            group_1 = functools.reduce( lambda a,b: a&b , map(lambda group_sack : set(group_sack), sacks[i*6:(i*6)+3]) )
            group_2 = functools.reduce( lambda a,b: a&b , map(lambda group_sack : set(group_sack), sacks[(i*6)+3:(i*6)+6]) )
            common_items = group_1 | group_2
            i+=1
            # Set Intersection
            for item in common_items:
                if ord(item) >= 97 and ord(item) <= 122:
                    score += ord(item)-96
                else:
                    score += ord(item)-38
    return score

if __name__ == "__main__":
    print("Part1: Score as per single sacks ", findCommonItemsInSingleSacks())
    print("Part2: Score as per Groups ", findCommonItemsInGroups())