class Robot:

    def __init__(self, name, x_cor, y_cor, direction) -> None:
        self.__name = name
        self.__xc = x_cor
        self.__yc = y_cor
        self.__dir = direction

    # @property
    def getRobotName(self):
        return self.__name
    
    # @name.setter
    def setRobotName(self, new_name):
        self.__name = new_name

    def getRowNumber(self):
        return self.__xc
    
    def setRowNumber(self, new_x_cor):
        self.__xc == new_x_cor

    def getColumnNumber(self):
        return self.__yc
    
    def setColumnNumber(self, new_y_cor):
        self.__yc == new_y_cor

    def getDirection(self):
        return self.__dir
    
    def voidSetDirection(self, new_direction):
        self.__dir = new_direction

    def setRobot(self, name, x_cor, y_cor, direction):
        self.position = [x_cor, y_cor]
        self.direction = direction
    # def canStep(self):

robot = Robot('x',1, 2, 'south')
print(robot.setRobotName('y'))
print(robot.getRobotName())