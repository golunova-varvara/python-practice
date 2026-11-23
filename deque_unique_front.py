from collections import deque

def add_unique_to_front(queue: deque, new_items: list) -> tuple[deque, int, int]:
    """
    Add unique elements from a list to the front of a deque.

    Iterates through new_items and prepends only the elements that are not
    already present in the queue.

    Args:
        queue (deque): The initial deque to be updated.
        new_items (list): A list of new elements to add.

    Returns:
        tuple: (updated_queue, added_count, skipped_count)
    """
    added_count = 0    # counter of added elements
    skipped_count = 0  # counter of skipped elements

    for item in new_items:
        if item in queue:
            skipped_count += 1
        else:
            added_count += 1
            queue.appendleft(item)

    print(f'Added: {added_count}, skipped: {skipped_count}')

    return queue, added_count, skipped_count


# Initial queue: [4, 5, 6]
queue = deque([4, 5, 6])

# New elements: 5 (duplicate), 1 (unique), 6 (duplicate), 2 (unique)
new_items = [5, 1, 6, 2]

updated_queue, added, skipped = add_unique_to_front(queue, new_items)

# Visual check of the result
print(f"Final queue: {list(updated_queue)}")