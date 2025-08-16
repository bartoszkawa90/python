# # zad z chata 1
# logs = [
#     "[2025-03-05 08:00:00] 1001 LOGIN_FAILURE /login",
#     "[2025-03-05 08:05:10] 1002 LOGIN_SUCCESS /dashboard",
#     "[2025-03-05 08:07:42] 1001 ACCESS /admin",
#     "[2025-03-05 08:10:30] 1003 LOGIN_SUCCESS /home",
#     "[2025-03-05 08:12:00] 1004 LOGIN_FAILURE /login",
#     "[2025-03-05 08:13:20] 1004 ACCESS /admin",
#     "[2025-03-05 08:15:45] 1002 ACCESS /settings",
#     "[2025-03-05 08:20:00] 1001 LOGIN_SUCCESS /home",
#     "[2025-03-05 08:25:10] 1003 ACCESS /admin",
#     "[2025-03-05 08:30:00] 1004 LOGIN_SUCCESS /dashboard",
#     "[2025-03-05 08:35:20] 1004 ACCESS /admin"
# ]
#
# from copy import deepcopy
#
#
# def check(logs):
#     users = list(set([log.split(' ')[2] for log in logs]))
#     user_actions = {}
#     result = []
#     temp = []
#     for user in users:
#         for log in logs:
#             if log.split(' ')[2] == user:
#                 temp.append(log.split(' ')[3])
#         for i in range(len(temp)-1):
#             if temp[i] == 'LOGIN_FAILURE' and temp[i+1] == 'ACCESS':
#                 print(f'user {user}, first {temp[i]}, second {temp[i+1]}')
#                 result.append(user)
#         temp.clear()
#     print(result)
#
#
# print(check(logs))



# zad z chata 2
# from typing import List, Tuple
# tasks = [
#     (1, 3, []),         # Task 1 takes 3 units of time, has no dependencies
#     (2, 2, [1]),        # Task 2 takes 2 units, must start after Task 1
#     (3, 1, [1]),        # Task 3 takes 1 unit, must start after Task 1
#     (4, 4, [2, 3]),     # Task 4 takes 4 units, must start after Task 2 and 3
#     (5, 6, [1]),        # Task 5 takes 6 units, must start after Task 1
#     (6, 2, [3, 5]),     # Task 6 takes 2 units, must start after Task 3 and 5
#     (7, 5, [2]),        # Task 7 takes 5 units, must start after Task 2
#     (8, 3, [4, 6, 7]),  # Task 8 takes 3 units, must start after Task 4, 6, and 7
#     (9, 7, [8]),        # Task 9 takes 7 units, must start after Task 8
#     (10, 4, [8]),       # Task 10 takes 4 units, must start after Task 8
#     (11, 5, [9, 10])    # Task 11 takes 5 units, must start after Task 9 and 10
# ]
#
#
#
# def minimum_completion_time(tasks: List[Tuple[int, int, List[int]]]) -> int:
#     """Return timestamps"""
#     # queue, after which task another can start
#     queue_ids = [task[0]
#              if len(task[2]) != 0 else task[0]
#              for task in sorted(tasks, key=lambda x: x[2])]
#     queue_conditions = [max(task[2])
#              if len(task[2]) != 0 else 0
#              for task in sorted(tasks, key=lambda x: x[2])]
#     timestamps = []
#     temp = []
#     for condition in list(set(queue_conditions)):
#         for task in tasks:
#             if len(task[2]) == 0 and condition == 0:
#                 temp.append(task[1])
#                 continue
#             else:
#                 if condition in task[2]:
#                     temp.append(task[1])
#         timestamps.append(max(temp))
#         temp.clear()
#     print(timestamps)
#
#
# minimum_completion_time((tasks))



# zad 333 z chata, Static analysis of Company actions in CSV files
import csv
import numpy as np

def process_data(csv_file: str, save_path: str) -> str:
    """ """
    with open(csv_file, 'r') as file:
        opened_file = csv.reader(file)
        rows = [row for row in opened_file]
        closing_values = [float(row[-2]) for row in rows[1:]]
        average_closing = np.average(closing_values)
        min_closing = np.min(closing_values)
        max_closing = np.max(closing_values)

        # check trend of closing prices
        trend_vals = []
        for val in range(len(closing_values)-1):
            trend_vals.append(closing_values[val+1] - closing_values[val])

        trend = sum([1 if v > 0 else 0 for v in trend_vals])/len(trend_vals)

        if trend > 0.6:
            whole_trend = "Increasing"
        elif trend < 0.4:
            whole_trend = "Decreasing"
        else:
            whole_trend = "Mixed"

        end_trend = ""
        if sum(trend_vals) > 0:
            end_trend = "Increasing"
        elif sum(trend_vals) == 0:
            end_trend = "No changes"
        else:
            end_trend = "Decreasing"

        # save if required
        if save_path:
            with open(save_path, 'w') as file:
                opened = csv.writer(file, delimiter=' ', quotechar='|')
                opened.writerow(["Average closing ", average_closing])
                opened.writerow(["Min closing ", min_closing])
                opened.writerow(["Max closing ", max_closing])
                opened.writerow(["Whole trend closing ", whole_trend])
                opened.writerow(["End trend closing ", end_trend])
                file.close()

        # whole trend determines how values are changing, end trend shows if there is an increase at the end
        return whole_trend, end_trend


print(process_data(csv_file='/Users/bartoszkawa/Desktop/REPOS/GitHub/python/test.csv',
                   save_path='/Users/bartoszkawa/Desktop/REPOS/GitHub/python/result.csv'))



