from collections import Counter

def findStreamStart(end_char = 4):
    with open('./puzzle.txt') as tc_feed:
        test_cases = tc_feed.read().splitlines()
        # test_cases = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
        results = []
        for tc in test_cases:
            i = 0
            while(i+(end_char-1) < len(tc)):
                store = Counter(tc[i:(i+end_char-1)+1])
                if len(store) == end_char:
                    break
                i+=1
            results.append(i+end_char)
        return results
if __name__ == '__main__':
    print("Part1: Find Start of Stream with start_range 4 characters", findStreamStart(4))
    print("Part1: Find Start of Stream with start_range 13 characters", findStreamStart(14))