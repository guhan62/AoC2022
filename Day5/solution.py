import re
from collections import defaultdict
def puzzleStackParser(fname = './sample.txt'):
    puzzle_lines = []
    stacker = defaultdict(list)
    with open(fname) as commands_list:
        commands = commands_list.read().splitlines()
        for command in commands:
            if command.startswith('move'):
                break
            else:
                puzzle_lines.append( command )
    puzzle_lines = puzzle_lines[:-1]
    puzzle_len = len(puzzle_lines)
    for idx, ch in enumerate(puzzle_lines[-1]):
        if ch != ' ':
            crate_level = puzzle_len - 2
            while( crate_level >= 0 ):
                if puzzle_lines[crate_level][idx] != ' ':
                    stacker[ch].append(puzzle_lines[crate_level][idx])
                crate_level -= 1
    return stacker

def craneSimulator(fname = './sample.txt'):
    """Simulate Final Stacks after Crane Commands (move crate 1 by 1)"""
    _stacker = puzzleStackParser(fname)
    with open(fname) as commands_list:
        commands = commands_list.read().splitlines()
        for command in commands:
            if command.startswith('move'):
                count, from_stack, to_stack = re.search(r"move (\d+) from (\d+) to (\d+)", command).groups()
                count = int(count)
                while count > 0:
                    _stacker[ to_stack ].append( _stacker[from_stack].pop(-1) )
                    count -= 1
    return "".join(map(lambda stacks: stacks[-1] if stacks else "", _stacker.values()))

def modernCraneSimulator(fname = './sample.txt'):
    """Simulate Final Stacks after Crane Commands (move crates by stack)"""
    _stacker = puzzleStackParser(fname)
    with open(fname) as commands_list:
        commands = commands_list.read().splitlines()
        for command in commands:
            if command.startswith('move'):
                count, from_stack, to_stack = re.search(r"move (\d+) from (\d+) to (\d+)", command).groups()
                count = int(count)
                popped_stack = []
                while count > 0:
                    popped_stack.append( _stacker[from_stack].pop(-1) )
                    count -= 1
                while popped_stack:
                    _stacker[to_stack].append( popped_stack.pop(-1) )
    return "".join(map(lambda stacks: stacks[-1] if stacks else "", _stacker.values()))

if __name__ == "__main__":
    # stacker = {
    #     '1': ['Z', 'N'],
    #     '2': ['M', 'C', 'D'],
    #     '3': ['P']
    # }
    # stacker = {
    #     '1': ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
    #     '2': ['D','N','T','S','B','Z'],
    #     '3': ['M','H','Q','R','F','C','T','G'],
    #     '4': ['G','R','Z'],
    #     '5': ['Z', 'N', 'R', 'H'],
    #     '6': ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
    #     '7': ['W','D','Z','R','C','G','M'],
    #     '8': ['S','J','F','L','H','W','Z','Q'],
    #     '9': ['S','Q','P','W','N']
    # }
    print("Part1  ", craneSimulator(fname = './puzzle.txt'))
    print("Part2  ", modernCraneSimulator(fname = './puzzle.txt'))