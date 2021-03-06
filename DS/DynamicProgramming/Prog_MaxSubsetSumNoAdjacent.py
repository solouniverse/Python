# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    # Two base cases
    # maxSums[0]=array[0] already initialized above by copy/slicing.
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]


# O(n) time | O(1) space
def maxSubsetSumNoAdjacent2(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
