"""A list processing utility to practice unit testing."""


def unique(lst):
    """Return a list containing only the first occurence of each distinct
       element in a list.  That is, all duplicates are omitted.

    Args:
        lst: a list of elements (not modified)
    Returns:
        a new list containing the first occurence of each distinct
        element in the `lst` argument.

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","c","a"])
    ['b', 'a', 'c']
    """
    if not isinstance(lst, list):
        raise TypeError('lst must be a list')
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
