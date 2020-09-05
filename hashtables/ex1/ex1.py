def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(0, length):
        difference = limit - weights[i]

        if difference in cache:
            w = cache[difference]
            total = (i, w)
            return total
        else:
            cache[weights[i]] = i

    return None
