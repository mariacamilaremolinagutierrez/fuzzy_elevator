"""
Solution without fuzzy logic
"""

import numpy as np

class Elevator(object):
    """
    An elevator:

    # Events
    0. Someone asks for the elevator from an outside floor
    1. Someone asks for a floor from the inside of the Elevator
    2. Passing by a floor and not stopping on it
    3. Stopping at a floor

    # Actions
    A. After 0 or 1 => update to_go list and direction
    B. After 2 => update current_floor
    C. After 3 => update direction (based on second element) and
                  to_go list (pop first element)
    """

    def __init__(self, n_floors, start_floor):
        """ Initializing variables. """
        self.n_floors = n_floors
        self.current_floor = start_floor
        self.direction = 1 # downward = 0, upward = 1
        self.to_go = []

    def process_event(self, event_type, event_params):
        """Responds to any type of event."""

        # Action A
        if event_type == 0 or event_type == 1:
            perform_action_A(event_params)

        # Action B
        elif event_type == 2:
            perform_action_B(event_params)

        # Action C
        elif event_type == 3:
            perform_action_C(event_params)

    def perform_action_A(self, event_params):
        # event_params = [new_floor]

        # update to go
        new_floor = event_params[0]
        self.insert_in_to_go(new_floor)

        # update direction
        self.update_direction()

    def perform_action_B(self, event_params):
        # event_params = [passed_floor]

        # update current floor
        passed_floor = event_params[0]
        self.current_floor = passed_floor

    def perform_action_C(self, event_params):
        # event_params = []

        # update direction
        if len(to_go) >= 2:
            self.update_direction()

        # update to_go
        if len(to_go) >= 1:
            self.to_go = self.to_go[1:]

    def insert_in_to_go(new_floor):

        inserted = 0

        if new_floor is in self.to_go:
            pass
        elif (new_floor > self.current_floor) and (direction == 1):
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
        elif (new_floor < self.current_floor) and (direction == 0):
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
        elif (new_floor > self.current_floor) and (direction == 0):
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
        else: #(new_floor < self.current_floor) and (direction == 1):
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

    def update_direction():
        current_f = self.to_go[0]
        next_f = self.to_go[1]

        if next_f > current_f:
            self.direction = 1
        else:
            self.direction = 0




def main():
    # Elevator attributes
    n_floors = 6 # 1, 2, 3, 4, 5, 6
    current_floor = 0
    direction = 1 # downward = 0, upward = 1
    to_go = []


if __name__ == '__main__':
    main()
