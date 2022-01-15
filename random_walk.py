from random import choice

class RandomWalk:
    """A class to generate random walks"""
    
    def __init__(self, num_of_points = 5000):
        """Initialize the attributes"""
        self.num_points = num_of_points
        
        #All walks start at (0,0)
        self.x_values =[0]
        self.y_values =[0]
        
    def fill_walk(self):
        """Calculate all the points in the walk"""
        
        #Keep taking steps until the walk reaches a desired length
        while len(self.x_values) < self.num_points:
            #Decide the direction to go and how far in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance   
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance   
            
            if x_step == 0 and y_step == 0:
                continue
            
            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)