class FileObject:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def calc_size(self):
        return self.size

    def __repr__(self):
        return f"{self.name}: {self.size}"

class DirObject:
    def __init__(self, name, objects=None):
        self.name = name
        if objects == None:
            self.objects = []
        else:
            self.objects = objects
    
    def add(self, obj):
        self.objects.append(obj)

    def calc_size(self):
        total = 0
        for obj in self.objects:
            total += obj.calc_size()
        return total

    def find(self, path):
        dirs = path.split('/')
        result = self
        for dir in dirs:
            if dir != '':
                for obj in result.objects:
                    if dir == obj.name:
                        result = obj
                        break
        return result
    
    def contains(self, name):
        for obj in self.objects:
            if obj.name == name:
                return True
        return False

    def __repr__(self):
        output = f"{self.name} (dir)"
        for obj in self.objects:
            output += f"\n  {obj}"
        return output


filesystem = DirObject("root")
currentPath = "root"

def cd(cmd):
    global currentPath
    _, _, dir = cmd.split(" ")
    if dir == "..":
        currentPath = currentPath[:currentPath.rindex("/")]
    else:
        currentDir = filesystem.find(currentPath)
        if not currentDir.contains(dir):
            currentDir.add(DirObject(dir))
        currentPath = currentPath + "/" + dir

def readInput():
    global currentPath
    with open("day7/input.txt") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line=line.strip()
            args = line.split(" ")
            if line.startswith("$ cd"):
                cd(line)
            elif line.startswith("$ ls"):
                continue
            elif line.startswith("dir"):
                filesystem.find(currentPath).add(DirObject(args[1]))
            elif args[0].isdigit():
                filesystem.find(currentPath).add(FileObject(args[1], int(args[0])))

def find_dirs(directory):
    dirs = []
    for obj in directory.objects:
        if isinstance(obj, DirObject):
            dirs.append(obj)
            dirs += find_dirs(obj)
    return dirs
        

def part1():
    readInput()
    TARGET_SIZE = 100000
    dirs = find_dirs(filesystem)
    total = 0
    for dir in dirs:
        size = dir.calc_size()
        if size <= TARGET_SIZE:
            total += size
    print(total)

def calc_size(dir):
    return dir.calc_size()

def part2():
    readInput()
    used_space = filesystem.calc_size()
    needed_space = 30_000_000 - (70_000_000 - used_space)
    dirs = find_dirs(filesystem)
    dirs.sort(key=calc_size)
    for dir in dirs:
        dir_size = dir.calc_size()
        if dir_size >= needed_space:
            print(dir.name, dir_size)
            break

# part1()
part2()