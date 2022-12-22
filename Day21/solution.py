import re

class TreeNode:
    def __init__(self, value = None, nodeName = None, lchild = None, op=None, rchild=None) -> None:
        self.nodeName = nodeName
        self.value = value
        self.op = op
        self.lchild = lchild
        self.rchild = rchild
    
    def __str__(self) -> str:
        sself = self
        tree_str = ""
        def DFS(sself, levels):
            nonlocal tree_str
            if not sself:
                return
            tree_str += f"{'-'*levels} {sself.nodeName} {sself.op} {sself.value}\n"
            DFS(sself.lchild, levels + 1)
            DFS(sself.rchild, levels + 1)
        DFS(sself, 0)
        return tree_str

def get_monkey_outcome(l, op, r):
    return int(eval(f"{l} {op} {r}"))

def equate_monkey_outcome(l, op, r):
    if not 'humn' in l:
        return f"({int(eval(l))} {op} {r} )"
    if not 'humn' in r:
        return f"({l} {op} {int(eval(r))} )"
    return f"({l} {op} {r})"

def part_1( jobs: TreeNode ):
    def calculate_node(jobs: TreeNode):
        if not jobs:
            return 
        calculate_node(jobs.lchild)
        if not jobs.value:
            if not jobs.lchild.value:
                calculate_node( jobs.lchild )
            if not jobs.rchild.value:
                calculate_node( jobs.rchild )
            jobs.value = get_monkey_outcome(
                jobs.lchild.value,
                jobs.op,
                jobs.rchild.value
            )
        calculate_node(jobs.rchild)
    calculate_node(jobs)
    return get_monkey_outcome(
        jobs.lchild.value, jobs.op, jobs.rchild.value
    )

def part_2( jobs: TreeNode ):
    def calculate_node(jobs: TreeNode):
        if not jobs:
            return 
        calculate_node(jobs.lchild)

        if jobs.nodeName == 'humn':
            jobs.value = 'humn'
        elif jobs.rchild and jobs.rchild.nodeName == 'humn':
            jobs.rchild.value = 'humn'
        elif jobs.lchild and jobs.lchild.nodeName == 'humn':
            jobs.lchild.value = 'humn'

        if not jobs.value:
            if not jobs.lchild.value:
                calculate_node( jobs.lchild )
            if not jobs.rchild.value:
                calculate_node( jobs.rchild )
            jobs.value = equate_monkey_outcome(
                jobs.lchild.value,
                jobs.op,
                jobs.rchild.value
            )
        calculate_node(jobs.rchild)
    calculate_node( jobs )
    X = int( eval( jobs.lchild.value if not 'humn' in jobs.lchild.value else jobs.rchild.value ) )
    return f"{X} = { jobs.lchild.value if 'humn' in jobs.lchild.value else jobs.rchild.value }"

if __name__ == '__main__':
    with open('./puzzle.txt') as monke:
        monkey_jobs_data = monke.read().splitlines()
        monkey_jobs = {}
        # Parse & Read Data -> and store in a Job Dict
        for monkey_job in monkey_jobs_data:
            monkey_job_parsed = re.search(r"(\w+): (\d+)|(\w+): (\w+) ([\*|\+\-\/]?) (\w+)", monkey_job).groups()
            if not monkey_job_parsed[0]:
                monkey_jobs[ monkey_job_parsed[2] ] = dict(
                    l=monkey_job_parsed[3], r=monkey_job_parsed[5],
                    op=monkey_job_parsed[4],value=None, 
                    nodeName = monkey_job_parsed[2] )
            else:
                monkey_jobs[ monkey_job_parsed[0] ] = dict(value=monkey_job_parsed[1], l=None, op=None, r=None, nodeName = monkey_job_parsed[0])
        def build_monkey_tree( curr_node ):
            if monkey_jobs[ curr_node ]['value']:
                return TreeNode(
                    value=monkey_jobs[ curr_node ]['value'], 
                    nodeName=monkey_jobs[ curr_node ]['nodeName']
                )
            else:
                return TreeNode(
                    lchild=build_monkey_tree( monkey_jobs[ curr_node ]['l'],  ),
                    op=monkey_jobs[curr_node]['op'],
                    rchild=build_monkey_tree( monkey_jobs[ curr_node ]['r'] ),
                    nodeName=monkey_jobs[ curr_node ]['nodeName']
                )
        # Parse Jobs & Build Job Tree
        jobs = TreeNode( 
            lchild=build_monkey_tree( monkey_jobs['root']['l'] ),
            op=monkey_jobs['root']['op'],
            rchild=build_monkey_tree( monkey_jobs['root']['r'] ),
            nodeName='root'
        )
        print("PART 1: ", part_1(jobs))
        jobs = TreeNode( 
            lchild=build_monkey_tree( monkey_jobs['root']['l'] ),
            op=monkey_jobs['root']['op'],
            rchild=build_monkey_tree( monkey_jobs['root']['r'] ),
            nodeName='root'
        )
        # Cheated: Run the Equation with Solve for X Online :)
        # https://calculator-online.net/solve-for-x-calculator/
        # Plus Cheated with Eval in Python3
        print("PART 2: ", part_2(jobs))
