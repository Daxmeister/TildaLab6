
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
    # Skapar tre pekare, vi kommer söka mellan low och high.
    low = 0
    high = len(list) - 1
    midpointer = 0
    while low <= high:
        midpointer = (high + low) // 2 # Hittar mitten på den delen av listan vi undersöker.
        if list[midpointer] < search_item:  # Om värdet som finns i mitten inte passar
            low = midpointer + 1            # kommer vi sätta nya gränser som vi undersöker.
        elif list[midpointer] > search_item:
            high = midpointer - 1
        else:
            return list[midpointer]
    return None


def main_med_fil(file):
    list = list_reader(file)
    #print(list)
    keywords_list = create_list_of_keywords(file)
    for keyword in keywords_list:
        keyword = keyword.strip()
        print(list, keyword, binary_search_sortofrecursive(list, keyword))


main_med_fil("Task1_file.txt")