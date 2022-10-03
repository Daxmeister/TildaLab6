
def list_reader(input_file):
    with open(input_file) as file:
        first_line = file.readline()
        first_line = first_line.strip()
        sorted_list = first_line.split(" ")
    return sorted_list

def create_list_of_keywords(input_file):
    list_of_keywords = []
    with open(input_file) as file:
        first_line = file.readline()
        list_of_keywords = file.readlines()
        [i.strip() for i in list_of_keywords]
    return list_of_keywords







def binary_search(list, search_item):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if list[mid] < search_item:
            low = mid + 1
        # If x is smaller, ignore right half
        elif list[mid] > search_item:
            high = mid - 1
        # means x is present at mid
        else:
            return list[mid]
    # If we reach here, then the element was not present
    return False


def main_med_fil(file):
    list = list_reader(file)
    #print(list)
    keywords_list = create_list_of_keywords(file)
    for keyword in keywords_list:
        keyword = keyword.strip()
        print(list, keyword, binary_search_sortofrecursive(list, keyword))


main_med_fil("Task1_file.txt")