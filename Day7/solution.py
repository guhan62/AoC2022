import re
from collections import defaultdict
class LLNode:
    def __init__(self, dname, parent, size = 0):
        self.dname = dname
        self.parent = parent
        self.dir_size = size
        self.peers = defaultdict(LLNode)
    
    def addPeerDir(self, dname, node):
        if not self.peers.get(dname):
            self.peers[ dname ] = node

def parseShellHistory():
    with open('./puzzle.txt') as shell_history_file:
        shell_history = shell_history_file.read().splitlines()
        root_dir = LLNode('/', parent=None, size = 0)
        cwd = root_dir
        # LS/CD re.search('\$ ([cd|ls]+)\s*([..|.|/])*', '$ ls').groups()
        # DIR re.search('dir ([A-Za-z0-9]+)', 'dir 12').groups()
        # FILE re.search('(\d+) ([A-Za-z0-9.]+)', '12 x').groups()
        lineno = 1
        while(lineno in range(1, len(shell_history))):
            if re.search(r'\$ cd ([\.|/|A-Za-z0-9]+)', shell_history[lineno]):
                groups = re.search(r'\$ cd ([\.|/|A-Za-z0-9]+)', shell_history[lineno]).groups()
                if groups[0] == '.':
                    continue
                elif groups[0] == '..':
                    cwd = cwd.parent
                else:
                    cwd = cwd.peers[groups[0]]
                lineno+=1
            elif re.search('\$ ls', shell_history[lineno]):
                lineno += 1
                dirs, files = [], []
                # Read Contents after ls
                while(lineno in range(1,len(shell_history)) and not shell_history[lineno].startswith('$')):
                    # Get all Dirs
                    if re.search('dir ([A-Za-z0-9]+)', shell_history[lineno]):
                        groups = re.search('dir ([A-Za-z0-9]+)', shell_history[lineno]).groups()
                        dirs.append(groups[0])
                    # Get all files
                    elif re.search('(\d+) ([A-Za-z0-9.]+)', shell_history[lineno]):
                        groups = re.search('(\d+) ([A-Za-z0-9.]+)', shell_history[lineno]).groups()
                        files.append( int(groups[0]) )
                    lineno+=1

                # Walk Dirs & Files
                for dir in dirs:
                    cwd.addPeerDir(dir, LLNode(dir, cwd, 0))
                # Backtrack - parents & update the children length
                for file_size in files:
                    cwd.dir_size += file_size
                    t_cwd = cwd
                    while(t_cwd.parent):
                        t_cwd.parent.dir_size += int(file_size)
                        t_cwd = t_cwd.parent


        # Bubble Down - To find sum of all dirs
        cwd = root_dir
        print(root_dir.dname, root_dir.dir_size)
        dirs, folder_size_list, total = [], [], 0
        dirs.extend(cwd.peers.values())
        while dirs:
            dir = dirs.pop(0)
            folder_size_list.append( dir.dir_size )
            if dirs:
                dirs.extend(dir.peers.values())
        return root_dir.dir_size, folder_size_list

def findDirsWithinSize(folder_size_list, limit_size = 100000):
    total = 0
    for f_size in folder_size_list:
        if f_size <= limit_size:
            total += f_size
    return total

import heapq
def findSmallestFolderForUpdate( folder_size_list, free_space, update_space = 30000000 ):
    heap = []
    for f_size in folder_size_list:
        need_space = free_space + f_size
        if need_space >= update_space:
            heapq.heappush( heap, f_size )
    return heapq.heappop(heap)

if __name__ == '__main__':
    root_size, folder_size_list = parseShellHistory()
    print("PART 1: Find Total Dirs for all dirs <= 100000", findDirsWithinSize(folder_size_list))
    fs_size = 70000000
    free_space = fs_size - root_size
    delete_space = findSmallestFolderForUpdate(folder_size_list, free_space)
    print(f"PART 2: Delete dir:{delete_space} gives {fs_size - root_size + delete_space}" )

        