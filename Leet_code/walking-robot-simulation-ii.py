class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.perimeter = (self.width + self.height) * 2
        self.x = 0
        self.y = 0
        self.cardinalDir = ["East", "North", "West", "South"]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.currentDir = 0

    def step(self, num: int) -> None:
        num %= self.perimeter

        if num == 0 and self.x == 0 and self.y == 0: # This is for an edge case when the robot walk full length of the perimeter and stands on the origin it should face south
            self.currentDir = 3

        for _ in range(num):
            dx, dy = self.x + self.directions[self.currentDir][0], self.y + self.directions[self.currentDir][1]

            if not (0 <= dx <= self.width and 0 <= dy <= self.height): #check if the robot is out of bounds
                self.currentDir = (self.currentDir + 1) % 4  # Turn the robot 90 degrees
                dx, dy = self.x + self.directions[self.currentDir][0], self.y + self.directions[self.currentDir][1]
                #update dx and dy for the next direction

            self.x, self.y = dx, dy

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        
    def getDir(self) -> str:
        return self.cardinalDir[self.currentDir]
        



