import heapq

def getFattestElf():
    with open('./Day1_input') as elves_list:
        calorie_feed = elves_list.read().splitlines()
        heap = []
        elf_calories = 0
        for calorie in calorie_feed:
            if calorie == "":
                heapq.heappush(heap, -elf_calories)
                elf_calories = 0
                continue
            elf_calories += int(calorie)
        return -heapq.heappop(heap)

def getFirst3FattestElves():
    with open('./Day1_input') as elves_list:
        calorie_feed = elves_list.read().splitlines()
        heap = []
        elf_calories = 0
        for calorie in calorie_feed:
            if calorie == "":
                heapq.heappush(heap, -elf_calories)
                elf_calories = 0
                continue
            elf_calories += int(calorie)
        # heapq.heappush(heap, -elf_calories)
        
        return -(heapq.heappop(heap) + heapq.heappop(heap) + heapq.heappop(heap))

if __name__ == "__main__":
    print("Top Carrying Elf : ", getFattestElf())
    print("Top 3 Carrying Elves : ", getFirst3FattestElves())