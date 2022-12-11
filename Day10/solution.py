import re

def finalRegisterValueWithInstructions(commands):
    X, cycles = 1, 0
    _register = dict( (20+i, 0) for i in range(0, 220, 40))
    Q = []
    # CRT = [ ['.']*40 for _ in range(6) ]
    for command in commands:
        if Q and Q[0][0] == cycles:
            X += Q[0][1]
            Q.pop(0)
        if command == 'noop':
            cycles += 1
        else:
            _, V = re.search(r'(addx)+ ([-]?\d+)*', command).groups()
            Q.append((cycles+2, int(V)))
            cycles += 1
            if cycles in _register:
                _register[cycles+1] = X
            cycles += 1
        print(cycles, X)
        if cycles in _register:
            _register[cycles] = X

    return sum( list(map(lambda cycle_mark : cycle_mark[0]*cycle_mark[1], _register.items())) )

def renderCRT( commands ):
    CRT = ['']
    X, cycles = 1, 0
    def render_sprite():
        nonlocal CRT
        nonlocal X
        nonlocal cycles
        sprite = [X-1, X , X+1]
        if sprite.count(cycles) > 0:
            CRT[-1] += '#'
        else:
            CRT[-1] += '.'
        cycles += 1
        if (cycles%40 == 0):
            CRT.append([''])
            # Timing Cycles with Tracer
            X += 40
    for command in commands:
        if command == 'noop':
            render_sprite( )
        else:
            _, V = re.search(r'(addx)+ ([-]?\d+)*', command).groups()
            render_sprite( )
            render_sprite( )
            X += int(V)
    return CRT

if __name__ == '__main__':
    commands = []
    with open('./puzzle.txt') as moves_input:
        commands = moves_input.read().splitlines()
        X = finalRegisterValueWithInstructions( commands )
        CRT = renderCRT( commands )
        print("Part1: ", X)
        print("Part2: ")
        print('\n'.join(_ for _ in [''.join(crt_strip) for crt_strip in CRT]))