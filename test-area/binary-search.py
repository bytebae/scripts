def binary_search(container, term, lpos, rpos):
    while lpos <= rpos:
        mid = (lpos + rpos)/2
        if container[mid] == term:
            return mid
        elif container[mid] < term:
            lpos = mid + 1
        else:
            rpos = mid - 1
    return -1
