"""
1. Robot Inheritance

Create two new classes which inherit from the Robot class. The first class is the DriveBot class which should use the Robot constructor.
The speed of the DriveBot will be represented by the motor_speed. You can pass in motor_speed as a parameter in the superclass constructor.
The next class is the WalkBot class. This class should also use the Robot constructor, but the speed is represented by steps_per_minute
which you can pass into the superclass constructor. Additionally, the WalkBot constructor should include another parameter for step_length.
This should default to 5 if not provided and should be assigned to an instance variable called step_length.
"""
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

# Create the DriveBot class here!
class DriveBot(Robot):
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

# Create the WalkBot class here!
class WalkBot(Robot):
    def __init__(self, steps_per_minute = 0, step_length = 5, direction = 180, sensor_range = 10):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

# Uncomment the robot instantiation!
robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 10, 90, 15)

# Use these print statements to test your code!
print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)


"""
2. Using The Superclass

Within the WalkBot class, override the adjust_sensor method to set the obstacle_found instance variable
to False and set the step_length to 5 in addition to the the original logic from the superclass.
"""
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, step_length = 5, direction = 180, sensor_range = 10):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    # Override the adjust_sensor method here!
    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5
        

robot_walk = WalkBot(60, 15, 90, 10)
robot_walk.obstacle_found = True
print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)
# Call the overridden adjust_sensor method here!
robot_walk.adjust_sensor(5)

print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)


"""
3. Conditional Superclass Logic

Create the method avoid_obstacles within the WalkBot class which overrides the same method from the Robot class.
This method should call the superclass avoid_obstacles method if obstacle_found is True and the speed is less
than or equal to 60, otherwise rotate the robot by 90 degrees (adding 90 to the current direction) and set
obstacle_found to False.

The direction should not be able to go above 360 degrees (use modulus in a similar way as the superclass method).
In either case, the speed and step_length of the WalkBot should be halved to ensure that the robot does not
fall over when turning to avoid the obstacle.
"""
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)


class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, step_length = 5, direction = 180, sensor_range = 10):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    # Override the avoid_obstacles method here!
    def avoid_obstacles(self):
        if self.obstacle_found:
            if self.speed <= 60:
               super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
        self.speed /= 2
        self.step_length /= 2


robot_1 = WalkBot(150, 10, 0, 10)
robot_1.obstacle_found = True
robot_1.avoid_obstacles()

print(robot_1.direction)
print(robot_1.speed)
print(robot_1.step_length)

robot_2 = WalkBot(60, 40, 0, 20)
robot_2.obstacle_found = True
robot_2.avoid_obstacles()

print(robot_2.direction)
print(robot_2.speed)
print(robot_2.step_length)


"""
4. Overriding Dunder Methods

Within the Robot class, override the + and - operations to increase or decrease the speed of the robot.
For the DriveBot class, the + and - operations should also increase and decrease the sensor_range of the robot.
For the WalkBot class, those operations should increase or decrease the step_length by half of the amount added.
This will change the distance that the robot travels per step based on the change in speed from the operations.
"""
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False
  
    # Override the + and - operations here!
    def __add__(self, num):
        self.speed += num
    
    def __sub__(self, num):
        self.speed -= num

class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)
    
    # Override the + and - operations here while using those dunder methods from the superclass!
    def __add__(self, num):
        super().__add__(num)
        self.sensor_range += num
    
    def __sub__(self, num):
        super().__sub__(num)
        self.sensor_range -= num

class WalkBot(Robot):

    def __init__(self, steps_per_minute = 0, step_length = 5, direction = 180, sensor_range = 10):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if(self.obstacle_found):
            if(self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    # Override the + and - operations here while using those dunder methods from the superclass!
    def __add__(self, num):
        super().__add__(num)
        self.step_length += num / 2
    
    def __sub__(self, num):
        super().__sub__(num)
        self.step_length -= num / 2

robot_1 = DriveBot()
robot_2 = WalkBot()

# Uncomment these lines when you are ready to test your code!
robot_1 + 20
robot_1 - 10
robot_2 + 10
robot_2 - 5

print(robot_1.speed)
print(robot_1.sensor_range)
print(robot_2.speed)
print(robot_2.step_length)


"""
5. Prevent A Robot Takeover

Update the WalkBot class to keep track of how many WalkBot objects are created.
If the total number of robots is 10 or above and there are at least 5 WalkBot objects created then set all_disabled to True for all robots.
Use a class variable called walk_bot_count within the WalkBot class.
"""
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):
    walkbot_count = 0

    def __init__(self, steps_per_minute = 0, step_length = 5, direction = 180, sensor_range = 10):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length
        WalkBot.walkbot_count += 1
        if Robot.robot_count >= 10 and WalkBot.walkbot_count >= 5:
            Robot.all_disabled = True

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if(self.obstacle_found):
            if(self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    def __add__(self, value):
        super().__add__(value)
        self.step_length += value / 2

    def __sub__(self, value):
        super().__sub__(value)
        self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)