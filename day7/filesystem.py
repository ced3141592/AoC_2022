
class Tree():

    def __init__(self, dir=None, name=None, value=None, children=None, parent=None):
        self.dir = dir
        self.children = children
        self.name = name
        self.value = value
        self.parent = parent
        self.valueWithSubdirs = 0

    @staticmethod
    def isNode(node):
        if isinstance(node, Tree):
            return isinstance(node.children, list)
        else:
            return False

    @staticmethod
    def isLeaf(leaf):
        if isinstance(leaf, Tree):
            return leaf.children == None
        else:
            return False

    def setChild(self, data):
        self.children.append(data)
        if Tree.isNode(data):
            data.parent = self.dir

    def hasChild(self):
        if self.children:
            return True
        else:
            return False

    def cd(self, dir):
        if Tree.isNode(dir):
            return dir
        else:
            for child in self.children:
                if Tree.isNode(child):
                    if child.dir == dir:
                        return child
        
        raise Exception("unable to cd into " + dir)

    def mkdir(self, dir):
        if Tree.isNode(self):
            self.children.append(Tree(dir=dir, children=[], value=0, parent=self))
            return self
        else:
            raise Exception("To create dir must point to directory, not file")

    def addLeaf(self, name, value):
        if self.dir == 'a':
            pass
        if Tree.isNode(self):
            self.children.append(Tree(dir=self.dir, name=name, value=value, children=None, parent=self))
            self.value += int(value)
            self.setvalueWithSubdirs(int(value))
        else:
            raise Exception("Cannot add Leaf to Leaf")

    def setvalueWithSubdirs(self, value):
        self.valueWithSubdirs += value
        if self.hasParent():
            self.parent.setvalueWithSubdirs(value)
    
    @staticmethod
    def hasDir(children :list, dir):
        if children != None and len(children) > 0:
            for child in children:
                if child.dir == dir:
                    return True
        return False
    

    def hasParent(self):
        return isinstance(self.parent, Tree)

    def printTree(self, depth):
        print("|", end='')
        for i in range(depth):
            print("  |", end='')
        if Tree.isLeaf(self):
            print(f"__ {self.name}  {self.value}")
        else:
            print(f"__ {self.dir}  {self.value}  {self.valueWithSubdirs}")
            for child in self.children:
                child.printTree(depth+1)

    def getallDirSizeWithSubdirsLimit(self, limit, allDirsValue):
        if Tree.isNode(self):    
            for child in self.children:
                if Tree.isNode(child):
                    if child.valueWithSubdirs <= limit:
                        allDirsValue.append(child.valueWithSubdirs)
                    child.getallDirSizeWithSubdirsLimit(limit, allDirsValue)
        return allDirsValue

    def toJson(self, dict):

        dict[self.dir] = []
        if Tree.isLeaf(self):
            dict[self.dir].append(f"{self.name} {self.value}")
        else:
            dict[self.dir].append({})
            for child in self.children:
                child.toJson(dict[self.dir][-1])

        return dict

            

def isCmd(line):
    return '$' in line and ' ' in line
   
def parse_browse_to_tree(input):
    tree = Tree(dir='/', children=[], value=0, parent=None)
    cd = tree
    lsFlag = False

    for line in input:
        if len(line) > 0:
            if isCmd(line):
                lsFlag = False
                cmd = line.split(' ')
                if cmd[1] == 'cd':
                    if cmd[2] == '..':
                        if cd.hasParent:
                            cd = cd.parent
                        else:
                            print("WARN: Tried to cd .. lower than root. cd set to '/' ")
                            cd = tree
                    elif cmd[2] == '/':
                        cd = tree
                    else:
                        if Tree.hasDir(cd.children, cmd[2]):
                            cd = cd.cd(cmd[2])
                        else:
                            dir = cd.mkdir(cmd[2])
                            cd = cd.cd(dir)

                elif cmd[1] == 'ls': # next output will be content of cwd. Create container for this
                    lsFlag = True
            else:
                if ' ' in line:
                    line = line.split(' ')
                    if line[0] == 'dir': 
                        if lsFlag:
                            cd.mkdir(line[1])

                    elif line[0].isnumeric(): # output line is a file (or Leaf). Format '<size> <name>'
                        cd.addLeaf(line[1], line[0])

    return tree


def main():
    with open("input.txt") as input:
        browse = [line.rstrip() for line in input]

        filesystem = parse_browse_to_tree(browse)

        filesystem.printTree(0)

        print("\n")

        allDirsValue100000 = filesystem.getallDirSizeWithSubdirsLimit(100000, [])

        # print(allDirsValue100000)
        print(sum(allDirsValue100000))

if __name__ == '__main__':
    main()

