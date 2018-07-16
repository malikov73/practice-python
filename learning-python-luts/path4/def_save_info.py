"""
Saving info with help nesting function
"""


def tester(start):
    def nester(label):
        print(label, nester.state)
        nester.state += 1
    nester.state = 0
    return nester
