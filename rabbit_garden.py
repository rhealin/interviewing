def eaten_carrots(garden):
    """
    Takes a garden matrix and returns the number of carrots the rabbit eats.
    On a given turn, the rabbit will eat the carrots available on the square that 
    it is on, and then move up, down, left, or right, choosing the the square that 
    has the most carrots. If there are no carrots left on any of the adjacent squares,
    the rabbit will go to sleep.

    >>> eaten_carrots([[5, 7, 8, 6, 3],
    ...         [0, 0, 7, 0, 4], 
    ...         [4, 6, 3, 4, 9],
    ...         [3, 1, 0, 5, 8]])
    27

    >>> eaten_carrots([[5, 7, 8, 6, 3],
    ...         [0, 0, 7, 0, 4], 
    ...         [4, 6, 3, 4, 9]])
    27

    >>> eaten_carrots([[5, 7, 8, 6],
    ...         [0, 0, 9, 0], 
    ...         [4, 6, 3, 4]])
    29

    >>> eaten_carrots([[1]])
    1
    """
    carrot_count = 0
    width, height = len(garden[0]), len(garden)
    
    current_r = [height//2]
    current_c = [width//2]

    # even widths -> two potential center columns
    if width % 2 == 0:
        current_c.append(width//2-1)
    # even heights -> two potential center rows
    if height % 2 == 0:
        current_r.append(height//2-1)

    # rabbit starts in the square closest to the center with the highest carrot count
    if len(current_r) > 1 or len(current_c) > 1:
        new_current_r, new_current_c = None, None
        max_carrots = 0

        for r in current_r:
            for c in current_c:
                if garden[r][c] > max_carrots:
                    max_carrots = garden[r][c]
                    new_current_r, new_current_c = r, c

        current_r = new_current_r
        current_c = new_current_c
    else:
        current_r, current_c = current_r[0], current_c[0]

    # continue eating until no more carrots left in adjacent squares
    while True:
        carrot_count += garden[current_r][current_c]
        garden[current_r][current_c] = 0
        
        all_neighbors = [(garden[r][c], r, c) for (r, c) in neighbors(current_r, current_c, garden)]
        current_r, current_c = None, None
        max_carrots = 0

        for neighbor in all_neighbors:
            if neighbor[0] > max_carrots:
                max_carrots = neighbor[0]
                current_r, current_c = neighbor[1:]
        
        # no more carrots left in adjacent squares
        if max_carrots == 0:
            return carrot_count


def neighbors(r, c, garden):
    """Return a list of the coordinates of all the neighbors of a given coordinate.
    """
    all_neighbors = []
    width, height = len(garden[0]), len(garden)

    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (0 <= r+x < height) and (0 <= c+y < width):
            all_neighbors.append((r+x, c+y))

    return all_neighbors    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
