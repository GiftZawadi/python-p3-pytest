def return_not_none():
    """This function (for testing purposes) returns a non-None value."""
    return "Value"

def test_return_not_none():
    """in not_none_functions, function "return_not_none" returns a value that is not None."""
    # Assert the returned value is not None using "is not"
    assert return_not_none() is not None
