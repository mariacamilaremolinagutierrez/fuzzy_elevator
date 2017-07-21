"""
Solution without fuzzy logic
"""

import numpy as np
import time

class Elevator(object):
    """
    An elevator:

    # Events
    0. Someone asks for the elevator from an outside floor
    1. Someone asks for a floor from the inside of the Elevator
    2. Stopping at a floor

    # Actions
    A. After 0 or 1 => call_a_floor: update to_go list and direction
    B. After 2 => stop_at_floor: update to_go list (pop first element) and
                                 direction
    """

    def __init__(self, n_floors, start_floor):
        """ Initializing variables. """
        self.n_floors = n_floors
        self.previous_floor = 0
        self.current_floor = start_floor
        self.direction = 1 # downward = 0, upward = 1
        self.to_go = []
        self.time_floor_to_floor = 5 #seconds

    def move_a_floor(self):
        #time.sleep(self.time_floor_to_floor)

        if self.current_floor == self.to_go[0]:
            self.stop_at_floor()

        if (self.direction == 1) and (self.current_floor != self.n_floors):
            self.update_current_floor(self.current_floor+1)
        elif (self.direction == 0) and (self.current_floor != 1):
            self.update_current_floor(self.current_floor-1)
        elif (self.direction == 1) and (self.current_floor == self.n_floors):
            self.update_current_floor(self.current_floor-1)
            self.direction = 0
        elif (self.direction == 0) and (self.current_floor == 1):
            self.update_current_floor(self.current_floor+1)
            self.direction = 1

    def call_a_floor(self, new_floor):

        # update to go
        self.insert_in_to_go(new_floor)

        # update direction
        self.update_direction()

        # status
        #self.print_status

    def stop_at_floor(self):

        # update to_go
        if len(self.to_go) >= 1:
            self.to_go = self.to_go[1:]

        # update direction
        self.update_direction()

        # status
        #self.print_status()

    def insert_in_to_go(self, new_floor):

        inserted = 0

        if new_floor in self.to_go:
            pass
        elif (new_floor > self.current_floor) and (self.direction == 1):
            # keep going up
            for i in range(len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if (f < new_floor) and (new_floor < n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
                elif (f < new_floor) and (f > n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
            if inserted == 0:
                self.to_go.append(new_floor)
        elif (new_floor < self.current_floor) and (self.direction == 0):
            # keep going down
            for i in range(len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if (f > new_floor) and (new_floor > n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
                elif (f > new_floor) and (f < n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
            if inserted == 0:
                self.to_go.append(new_floor)
        elif (new_floor > self.current_floor) and (self.direction == 0):
            # go down first and when direction changes visit new in order
            direction_change_index = 0

            for i in range(len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if n > f:
                    direction_change_index = i + 1
                    break

            for i in range(direction_change_index, len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if (f < new_floor) and (new_floor < n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
                elif (f < new_floor) and (f > n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
            if inserted == 0:
                self.to_go.append(new_floor)
        else: #(new_floor < self.current_floor) and (self.direction == 1):
            # go up first and when direction changes visit new in order
            direction_change_index = 0

            for i in range(len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if n < f:
                    direction_change_index = i + 1
                    break

            for i in range(direction_change_index, len(self.to_go) - 1):
                f = self.to_go[i]
                n = self.to_go[i+1]

                if (f > new_floor) and (new_floor > n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
                elif (f > new_floor) and (f < n):
                    self.to_go.insert(i+1, new_floor)
                    inserted = 1
                    break
            if inserted == 0:
                self.to_go.append(new_floor)

    def update_direction(self):

        if len(self.to_go) >= 1:
            next_f = self.to_go[0]

            if next_f > self.current_floor:
                self.direction = 1
            else:
                self.direction = 0

    def update_current_floor(self, new_value):
        self.previous_floor = self.current_floor
        self.current_floor = new_value

    def has_floors_to_go(self):
        if len(self.to_go) != 0:
            return True
        else:
            return False

    def print_status(self):
        arrow = 'v'
        if self.direction == 1:
            arrow = '^'
        print('STATUS:', self.previous_floor, arrow, self.current_floor,
              self.to_go)


def main():
    # Elevator attributes
    n_floors = 6 # 1, 2, 3, 4, 5, 6
    current_floor = 1
    direction = 1 # downward = 0, upward = 1
    random_numbers = np.random.rand(10)*n_floors + 1.0
    random_calls = [int(num) for num in random_numbers]

    print('Floors to go:', random_calls)

    elevator = Elevator(n_floors=n_floors, start_floor=current_floor)
    elevator.print_status()

    while True:

        elevator.print_status()

        # call a floor
        if (len(random_calls) != 0) and (np.random.rand(1)[0] > 0.2):
            elevator.call_a_floor(random_calls[0])
            random_calls.pop(0)
            #print('Floors to go:', random_calls)

        # move
        if elevator.has_floors_to_go():
            elevator.move_a_floor()
        else:
            time.sleep(1)

        # break loop
        if (len(random_calls) == 0) and (not elevator.has_floors_to_go()):
            break



if __name__ == '__main__':
    main()
