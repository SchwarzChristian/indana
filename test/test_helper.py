from indana._helper import deepcopy

def test_deepcopy_dict():
    orig = {
        "a": 23,
        "b": {
            "a": 23,
            "b": 42,
        }
    }

    copy = deepcopy(orig)

    copy["a"] = 42
    copy["b"]["a"] = 42
    copy["b"]["b"] = 23

    assert orig["a"] == 23
    assert orig["b"]["a"] == 23
    assert orig["b"]["b"] == 42

def test_deepcopy_array():
    orig = [23, [23, 42]]

    copy = deepcopy(orig)

    copy[0] = 42
    copy[1][0] = 42
    copy[1][1] = 23

    assert orig[0] == 23
    assert orig[1][0] == 23
    assert orig[1][1] == 42

def test_deepcopy_mixed():
    orig = [23, {
        "a": 23, 
        "b": 42,
    }]

    copy = deepcopy(orig)

    copy[0] = 42
    copy[1]["a"] = 42
    copy[1]["b"] = 23

    assert orig[0] == 23
    assert orig[1]["a"] == 23
    assert orig[1]["b"] == 42
