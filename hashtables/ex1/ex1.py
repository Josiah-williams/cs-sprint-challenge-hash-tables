weight = [4, 6, 10, 15, 16]


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # empty dict
    cache = {}

    # go over the length of the weights
    for index in range(length):

        # calculating: by substracting the value at the current index
        need = limit - weights[index]
        
        # check the cache
        if need in cache:
            # if the need value is in the cache
            # extract it from cache and
            # assign it to a new variable
            subtract = cache[need]

            new_list = [index, subtract]
            new_list.sort(reverse = True)
            return new_list
        else:
            cache[weights[index]] = index

        
        
    return None

