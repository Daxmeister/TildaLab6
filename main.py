# Uppgift 1

# Tar en lista och ett sökord som input. Returnerar föremålet om det finns, annars False.
def binary_search(list, search_item):
    low = 0
    high = len(list) - 1
    midpointer = 0
    while low <= high:
        midpointer = (high + low) // 2
        if list[midpointer] < search_item:
            low = midpointer + 1
        elif list[midpointer] > search_item:
            high = midpointer - 1
        else:
            return list[midpointer]
    return False


# Indata är en fil på angivet format, returnerar filen som en lista.
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

def main_med_fil(file):
    list = list_reader(file)
    #print(list)
    keywords_list = create_list_of_keywords(file)
    for keyword in keywords_list:
        keyword = keyword.strip()
        print(list, keyword, binary_search(list, keyword))

def main(input_file):
    #indata = open(input_file)
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main_med_fil("Task1_file.txt")
#print(list_reader("Task1_file.txt"))