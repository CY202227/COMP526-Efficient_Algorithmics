task_id = 4
growth_rate = [55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

# Don't change anything above this line
# =====================================

# generate your solution as a list
# the smallest height should be 105

#110:
queue = [(2, 8), (0, 1), (6, 9),
         (0, 7), (1, 2), (0, 5),
         (3, 4), (0, 1)]

#110:
#queue = [(0, 1), (7, 3), (0, 2),
#        (0, 1), (9, 4), (0, 3),
#       (0, 1), (5, 2), (0, 1),
#      (0, 6), (8, 2)]

# =====================================
# Don't change anything below this line

from collections import deque

solution = deque()
# add each element to the solution
for i in queue:
    solution.append(i)

import bamboo

# records your solution
bamboo.calculate_height(growth_rate, solution, task_id)
