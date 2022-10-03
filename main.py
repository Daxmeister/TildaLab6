# Uppgift 1

# Tar en lista och ett sökord som input. Returnerar föremålet om det finns, annars False.
def binary_search(list, search_item):
    if len(list) == 0
        return False
    midpoint = len(list) // 2
    if midpoint == search_item:
        return midpoint
    else if search_item > midpoint:
        binary_search(list[midpoint:])
    else if search_item < midpoint:
        binary_search(list[:midpoint])

# Indata är en fil på angivet format, returnerar filen som en lista.
def list_reader(input_file):
    with open(input_file) as file:
        first_line = file.readline()
        sorted_list = first_line.split(" ")
    return sorted_list


def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()