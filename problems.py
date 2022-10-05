from datetime import datetime

def getAssignments(problems_src):
    assignments = {}

    with open(problems_src, "r") as assign_file:
        for l in assign_file.readlines():
            items = l.split()

            # strip off the colon
            id = items[0][:-1]

            deadline = datetime.strptime(items[-1] + " 23:55:00", "%Y-%m-%d  %H:%M:%S")

            assignments[id] = (items[1:-1], deadline)

    return assignments
