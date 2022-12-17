
class Tree():

    def __init__(self, pos=(0,0)):
        self.pos = pos

    @staticmethod
    def getGrid(input):
        grid = [list(line) for line in input.splitlines()]
        
        # post-condition
        for i, line in enumerate(grid):
            if i+1 == len(grid):
                break
            if len(line) != len(grid[i+1]):
                raise Exception("Invalid Grid format")

        return grid

    @staticmethod
    def printGrid(grid):
        for line in grid:
            print(line)

    def printTree(self, grid):
        x, y = self.pos
        print(grid[x][y])

    def getTree(self, grid):
        x, y = self.pos
        return grid[x][y]

    def setPosition(self, pos):
        self.pos = pos

    def getPosition(self):
        return self.pos

    def isVisible(self, grid, col):
        x, y = self.pos
        lenX = len(grid[0])
        lenY = len(grid)
        if x == 0 or y == 0 or \
            x == lenX-1 or y == lenY-1:
            return True
        else:
            highest_top = max(col[:x])
            highest_bottom = max(col[x+1:])
            highest_left = max(grid[x][:y])
            highest_right = max(grid[x][y+1:])
            pass
            return highest_top < grid[x][y] or \
                highest_bottom < grid[x][y] or \
                highest_left < grid[x][y] or \
                highest_right < grid[x][y]

    def countTreesVisibleInGrid(self, grid):
        lenX = len(grid[0])
        lenY = len(grid)
        count = 0

        for i in range(lenY):
            col = [line[i] for line in grid]
            for j in range(lenX):
                self.setPosition((j,i))
                if self.isVisible(grid, col):
                    count += 1
        return count

    def getScenicScore(self, grid, col):
        x, y = self.getPosition()
        treehouse = self.getTree(grid)
        view_top = col[:x][::-1]
        view_bottom = col[x+1:]
        view_left = grid[x][:y][::-1]
        view_right = grid[x][y+1:]
        scenicScore = 1
        for views in [view_top, view_bottom, view_left, view_right]:
            for i, tree in enumerate(views):
                if treehouse <= tree:
                    scenicScore  *= (i+1) # i start at 0
                    break
                if i+1 == len(views):
                    scenicScore  *= (i+1) # end of grid is reached
            
        return scenicScore

    def gethighestScenicScore(self, grid):
        lenX = len(grid[0])
        lenY = len(grid)
        highestScenicScore = 0

        for i in range(lenY):
            col = [line[i] for line in grid]
            for j in range(lenX):
                self.setPosition((j,i))
                if self.isVisible(grid, col):
                    scenicScore = self.getScenicScore(grid, col)
                    if scenicScore > highestScenicScore:
                        highestScenicScore = scenicScore
        return highestScenicScore


def main():
    with open('input.txt') as file:
        input = file.read()
    file.close()    

    grid = Tree.getGrid(input)
    # Tree.printGrid(grid)

    u = Tree()


    print("Visible trees in grid: ", u.countTreesVisibleInGrid(grid))

    print("Highets scenic score: ", u.gethighestScenicScore(grid))




if __name__ == '__main__':
    main()
    