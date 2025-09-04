"""
Assignment: Implement a simple list flattener.

Goal:
- Write a function `flatten(lst)` that takes a list which may contain nested lists
  and returns a new list with all values flattened in order.

Rules:
- Only flatten instances of `list`. Treat any non-list (e.g., int, str, tuple, dict)
  as a single item.
- Preserve the original left-to-right order.
- Do not mutate the input list; return a new list.

Examples:
- flatten([1, [2, 3], 4]) -> [1, 2, 3, 4]
- flatten([[[]]]) -> []
- flatten([1, [2, [3, [4]]], 5]) -> [1, 2, 3, 4, 5]
- flatten([1, (2, 3), [4, (5, 6)]]) -> [1, (2, 3), 4, (5, 6)]  # tuples are NOT flattened
"""


def flatten(lst):
    """
    Flatten a list with arbitrarily nested lists into a single flat list.

    Parameters:
    - lst: list
        The list to flatten. It may contain nested lists at any depth. Only
        instances of `list` are recursively flattened; other types are treated
        as atomic values.

    Returns:
    - list: a new flattened list.

    Constraints:
    - Must not mutate the input.
    - Must preserve order.
    - Only lists are recursively flattened.

    Your task:
    - Replace the NotImplementedError below with a working implementation.
    """
    raise NotImplementedError("Implement me: return a new flattened list without mutating input.")


