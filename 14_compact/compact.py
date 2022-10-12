def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst1 = []
    for item in lst:
        if item:
            lst1.append(item)
    
    return lst1
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))