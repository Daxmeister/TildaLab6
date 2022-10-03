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
    return None


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