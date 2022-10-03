def binary_search_recursive(list, search_item):
    if len(list) == 0:
        return None
    midpoint = len(list) // 2
    if list[midpoint] == search_item:
        return list[midpoint]
    elif search_item > list[midpoint]:
        binary_search(list[midpoint:], search_item)
    elif search_item < list[midpoint]:
        binary_search(list[:midpoint], search_item)


def binary_search_sortofrecursive(list, search_item):
    if len(list) == 0:
        return None
    while len(list) > 1:
        midpoint = len(list) // 2
        if list[midpoint] == search_item:
            return list[midpoint]
        elif search_item > list[midpoint]:
            list = list[midpoint:]
        elif search_item < list[midpoint]:
            list = list[:midpoint]
    return None

# Funktion som läser in filen till en lista med strängar för varje rad.
def readfile(file):
    with open(file) as song_file:
        song_list = song_file.readlines()
        [i.strip() for i in song_list]
    return song_list