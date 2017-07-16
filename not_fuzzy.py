'''
Solution without fuzzy logic
'''

import numpy as np

# Elevator attributes
n_floors = 6 # 1, 2, 3, 4, 5, 6
current_floor = 0
direction = 1 # downward = 0, upward = 1
to_go = []

# Events
# 1. Someone asks for the elevator from an outside floor
# 2. Someone asks for a floor from the inside of the Elevator

# Actions
# 1. After any event => update to_go list
# 2. After passing a floor => update current_floor
# 3. After stopping at a floor => update to_go list and direction

print(n_floors)
