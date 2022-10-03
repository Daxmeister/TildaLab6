# Uppgift 1

# Tar en lista och ett sökord som input. Returnerar föremålet om det finns, annars False.
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
    return None                             # Ifall vi aldrig hittade ett passande värde returneras None
"""

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
#print(list_reader("Task1_file.txt"))"""

# Uppgift 2

# En Class som representerar en låt. Construktorn tar en sträng från filen.
class Song():
    def __init__(self, string):
        list = string.split("<SEP>")
        [i.strip() for i in list]
        self.trackid = list[0]
        self.song_length = list[1]
        self.artist = list[2]
        self.title = list[3]
    def __lt__(self, other):
        self.artist < other.artist

    def __eq__(self, other):
        self.artist == other.artist

    def __str__(self):
        return self.title

"""ex_string = "TRMMMBB12903CB7D21<SEP>SOEYRFT12AB018936C<SEP>Kris Kross<SEP>2 Da Beat Ch'yall"
ex_object = Song(ex_string)
print(ex_object)"""

# Funktion som tar emot en fil och skapar en lista som innehåller sångobjekt från klassen Song.
def creator_of_songlistobject(file):
    with open(file) as song_file:
        song_object_list = []
        for line in song_file:
            song_object_list.append(Song(line))
    return song_object_list




def linear_search(list, artist):
    for object in list:
        if object.artist == artist:
            return True
    return False



def main(file):
    import timeit as timeit
    list_of_songobjects = creator_of_songlistobject(file)
    n = len(list_of_songobjects)
    print("Antal element =", n)
    last = list_of_songobjects[n-1]
    searched_artist = last.artist
    linjtid = timeit.timeit(stmt = lambda: linear_search(list_of_songobjects, searched_artist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    # Del 2 binärsökning börjar här
    list_of_songobjects.sort()
    bintid = timeit.timeit(stmt=lambda: binary_search(list_of_songobjects, searched_artist), number=10000)
    print("Linjärsökningen tog", round(bintid, 4), "sekunder")

main("unique_tracks_mini.txt")