"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    collected = []
    return cycle_check(head, collected)


def cycle_check(head, collected):
    if head is None:
        return False
    if head in collected:
        return True
    collected.append(head)
    return cycle_check(head.next, collected)
