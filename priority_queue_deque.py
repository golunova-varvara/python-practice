from collections import deque

queue = deque()


def add_to_priority_queue(queue, player):
    """
    Add a player to the front of the priority queue.

    Args:
        queue (deque): double-ended queue of players
        player (str): player identifier to add
    """
    queue.appendleft(player)


def process_priority(queue):
    """
    Remove and return the first player from the priority queue.

    Args:
        queue (deque): double-ended queue of players

    Returns:
        str or None: the first player in the queue, or None if empty
    """
    if not queue:
        return None
    return queue.popleft()


def get_priority_queue_size(queue):
    """
    Return the number of players in the priority queue.

    Args:
        queue (deque): double-ended queue of players

    Returns:
        int: current size of the queue
    """
    return len(queue)


# Testing
add_to_priority_queue(queue, "VIP1")
add_to_priority_queue(queue, "VIP2")
print(queue)  # Output: deque(['VIP2', 'VIP1'])

result = process_priority(queue)
print(result)  # Output: 'VIP2'