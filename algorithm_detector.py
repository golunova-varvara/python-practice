def detect_algorithm_type(description):
    """
    Detect the type of algorithm based on the text description.

    Args:
        description (str): the text description of the algorithm.

    Returns:
        str: the type of algorithm ("Cyclic", "Branched", "Linear", "Not detected")
        or an error message "Error: description must be a string".
    """

    if not isinstance(description, str):
        return "Error: description must be a string"

    desc_lower = description.lower()

    cycle_markers = ["repeat", "every time", "cycle", "loop", "several times", "for", "while"]
    if any(marker in desc_lower for marker in cycle_markers):
        return "Cyclic"

    branch_markers = ["condition", "choice", "if", "else"]
    if any(marker in desc_lower for marker in branch_markers):
        return "Branched"

    linear_markers = ["first", "next", "then", "after"]
    if any(marker in desc_lower for marker in linear_markers):
        return "Linear"

    return "Not detected"


# Testing
print(detect_algorithm_type("You need to repeat the action 10 times"))
print(detect_algorithm_type("Check the condition and make a choice"))
print(detect_algorithm_type("First add, then subtract"))

# Invalid data
print(detect_algorithm_type(1))
print(detect_algorithm_type("Algorithm"))