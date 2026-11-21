def add_task(stack, task):
    """
    Add a new task to the stack.

    Args:
        stack (list): list of tasks (stack)
        task (str): a new task

    Returns:
        list: updated stack of tasks
    """
    stack.append(task)
    return stack


def complete_task(stack):
    """
    Remove and return the last added task.

    Args:
        stack (list): list of tasks (stack)

    Returns:
        str: the last added task or an error message
    """
    if not stack:
        return "There are no tasks to complete"
    return stack.pop()


def show_tasks(stack):
    """
    Print all current tasks in the stack (from last to first).

    Args:
        stack (list): list of tasks (stack)
    """
    if not stack:
        print("The task list is empty")
        return

    for i in range(len(stack) - 1, -1, -1):
        print(f"- {stack[i]}")


tasks_stack = []

# Add 3 tasks
add_task(tasks_stack, "Go to the supermarket")
add_task(tasks_stack, "Buy groceries")
add_task(tasks_stack, "Put away groceries")

# Show the list
print("Current tasks:")
show_tasks(tasks_stack)
print()

# Complete 2 tasks
print(f"Completed: {complete_task(tasks_stack)}")
print(f"Completed: {complete_task(tasks_stack)}")
print()

# Show the list again
print("Remaining tasks:")
show_tasks(tasks_stack)