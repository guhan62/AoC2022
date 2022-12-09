
def findVisibleTrees():
    with open('./puzzle.txt') as tc_feed:
        tree_grid_file = tc_feed.read().splitlines()
        r,c = len(tree_grid_file), len(tree_grid_file[0])
        tree_grid, result = [], 0
        for i in range(r):
            tree_grid.append( list(map(lambda tree_height: int(tree_height) , tree_grid_file[i])) )
        visible_trees = set()
        if r == 1 or c == 1:
            return max(r,c)
        # Edges UP: 0,j DOWN: r-1,j
        # Edges L: i,0 R: i,c-1
        # From Left, Right Visible Trees
        for i in range(1,r-1):
            for j in range(1,c-1):
                # print(tree_grid[i][j], f"U:{tree_grid[0][j]} D:{tree_grid[r-1][j]} L:{tree_grid[i][0]} R:{tree_grid[i][c-1]}")
                # print(tree_grid[i][j], f"U:{tree_grid[i][0]} L:{tree_grid[i][c-1]} L->T:{tree_grid[i][1:j]} T->R:{tree_grid[i][j+1:c-1]}")
                # From Left
                if tree_grid[i][j] > tree_grid[i][0] and tree_grid[i][j] > max(tree_grid[i][1:j], default=0):
                    visible_trees.add((i,j))
                # From Right
                elif tree_grid[i][j] > tree_grid[i][c-1] and tree_grid[i][j] > max(tree_grid[i][j+1:c-1], default=0):
                    visible_trees.add((i,j))
        # From Top, Bottom
        tree_grid_t = list(map(list, zip(*tree_grid)))
        r_t, c_t = len(tree_grid_t), len(tree_grid_t[0])
        # From Left, Right Visible Trees
        for i in range(1,r_t-1):
            for j in range(1,c_t-1):
                # From Top
                # print(tree_grid_t[i][j], f"U:{tree_grid_t[i][0]} D:{tree_grid_t[i][c_t-1]} U->T:{tree_grid_t[i][1:j]} D->T:{tree_grid_t[i][j+1:c_t-1]}")
                if tree_grid_t[i][j] > tree_grid_t[i][0] and tree_grid_t[i][j] > max(tree_grid_t[i][1:j], default=0):
                    visible_trees.add((j,i))
                # From Bottom
                elif tree_grid_t[i][j] > tree_grid_t[i][c_t-1] and tree_grid_t[i][j] > max(tree_grid_t[i][j+1:c_t-1], default=0):
                    visible_trees.add((j,i))
        result += (r*2) + (c-2)*2
        result += len(visible_trees)
        return result

def findScenenicSpot():
    def find_trees_visible_from_spot(tree_height, tree_lane):
        visible_trees = 0
        # print(tree_lane)
        for v_tree_height in tree_lane:
            visible_trees += 1
            if v_tree_height >= tree_height:
                break
        return visible_trees

    with open('./puzzle.txt') as tc_feed:
        scenic_score = 0
        tree_grid_file = tc_feed.read().splitlines()
        r,c = len(tree_grid_file), len(tree_grid_file[0])
        tree_grid = []
        for i in range(r):
            tree_grid.append( list(map(lambda tree_height: int(tree_height) , tree_grid_file[i])) )
        tree_grid_t = list(map(list, zip(*tree_grid)))

        for i in range(r):
            for j in range(c):
                # Tree to left Edge
                l_score = find_trees_visible_from_spot(tree_grid[i][j], tree_grid[i][:j][::-1])
                r_score = find_trees_visible_from_spot(tree_grid[i][j], tree_grid[i][j+1:])
                # Tree to Top Edge
                u_score = find_trees_visible_from_spot(tree_grid_t[j][i], tree_grid_t[j][:i][::-1])
                d_score = find_trees_visible_from_spot(tree_grid_t[j][i], tree_grid_t[j][i+1:])
                score = l_score * r_score * u_score * d_score
                # print(f"{tree_grid[i][j]} --- {l_score}+{r_score}+{u_score}+{d_score}={score}")
                scenic_score = max(score, scenic_score)
        return scenic_score
        
if __name__ == '__main__':
    print("Part1: Find Visible Trees", findVisibleTrees())
    print("Part2: Find Sceneic Trees",findScenenicSpot() )