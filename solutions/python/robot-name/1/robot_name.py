import random
import string


class Robot:

    name_set = set()

    def __init__(self):
        self.name = self.new_name()

    def reset(self):
        new_name = self.new_name()
        if self.name in Robot.name_set:
            Robot.name_set.remove(self.name)
        self.name = new_name

    def new_name(self):
        retry_times = 1000
        for _ in range(retry_times):
            name = self.random_name()
            if name not in Robot.name_set:
                Robot.name_set.add(name)
                return name
        raise Exception(f"Failed to generate new name after {retry_times} retries")

    def random_name(self):
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        digits = ''.join(random.choice(string.digits) for _ in range(3))
        return letters + digits


if __name__ == '__main__':
    robot1 = Robot()
    robot2 = Robot()
    print(robot1.name)
    print(robot2.name)
