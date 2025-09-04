import copy
import pytest

from assignment import flatten


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([
            [[[]]]
        ], []),
        ([[1], [], [2, [3, []]]], [1, 2, 3]),
        ([1, [2, [3, [4]]], 5], [1, 2, 3, 4, 5]),
        ([], []),
        ([
            ["a"],
            ["b", ["c"]]
        ], ["a", "b", "c"]),  # strings treated as scalars; only lists flattened
        ([1, (2, 3), [4, (5, 6)]], [1, (2, 3), 4, (5, 6)]),  # tuples are NOT flattened
        ([None, [True, [False]]], [None, True, False]),
        ([[[0]], [1, [2], [], [[3]]]], [0, 1, 2, 3]),
        ([["ab", ["cd"]], "ef"], ["ab", "cd", "ef"]),
    ],
)
def test_flatten_parametrized(inp, expected):
    assert flatten(inp) == expected


def test_does_not_mutate_input_and_returns_new_list():
    original = [1, [2, [3, []]], 4]
    snapshot = copy.deepcopy(original)
    out = flatten(original)
    # returns a new list
    assert out is not original
    # input remains unchanged
    assert original == snapshot


def test_only_lists_are_flattened_not_other_iterables():
    data = [1, (2, 3), {4, 5}, {"a": 1}, [6, (7, 8)], "xy"]
    # sets/dicts/tuples/strings are not flattened; only inner list is flattened
    expected = [1, (2, 3), {4, 5}, {"a": 1}, 6, (7, 8), "xy"]
    assert flatten(data) == expected


