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

# Uppgift 2 -----------------------------------------------------------------------------------------------------------

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
        return self.artist < other.artist

    def __le__(self, other):
        return self.artist <= other.artist

    def __eq__(self, other):
        return self.artist == other.artist

    def __gt__(self, other):
        return self.artist > other.artist

    def __ge__(self, other):
        return self.artist >= other.artist

    def __str__(self):
        return self.artist

    def __repr__(self):
        return str ("Object " + self.artist)

    def __hash__(self):
        return hash(self.artist)


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

# Tar lista med object och str på artist som sökes och returnerar str eller None
def linear_search(list, artist):
    for object in list:
        if object.artist == artist:
            return object.artist
    return None


# Skapar en dictionary med key artistnamn och value objektet som tillhör.
def create_dictionary(list_with_objects):
    dictionary = {}
    for object in list_with_objects:
        dictionary[object.artist] = object
    return dictionary

def dictionary_search(dictionary, artist_name):
    if artist_name in dictionary:
        return artist_name
    else:
        return None

# Jämför olika sökstrategier
def main_compare_searches(file):
    # Setup
    import timeit as timeit
    list_of_songobjects = creator_of_songlistobject(file)
    list_of_songobjects = list_of_songobjects[0:250000]       # Denna rad kan användas för att korta ned listan
    n = len(list_of_songobjects)
    print("Antal element =", n)
    last = list_of_songobjects[n-1]
    searched_artist = last.artist

    # Del 1
    linjtid = timeit.timeit(stmt = lambda: linear_search(list_of_songobjects, searched_artist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    # Del 2 binärsökning börjar här. Notera att vi matar in ett object som sökes.
    list_of_songobjects.sort()
    bintid = timeit.timeit(stmt=lambda: binary_search(list_of_songobjects, last), number=10000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    # Del 3
    hash_table = create_dictionary(list_of_songobjects)
    bintid = timeit.timeit(stmt=lambda: dictionary_search(hash_table, searched_artist), number=10000)
    print("Hashsökningen tog", round(bintid, 4), "sekunder")


#main_compare_searches("unique_tracks.txt")

# Del 3 (Sortering) --------------------------------------------------------------------------------------------------

# Tar in en lista och sortrar. Kod hämtad från föreläsning.
def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i + 1, n):
            if data[j] < data[minst]:
                minst = j
        data[minst], data[i] = data[i], data[minst]

# Quicksort hämtat från kursboken
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

'''song_list = creator_of_songlistobject("unique_tracks_mini.txt")
print(song_list)

song_list = bubbelsortera(song_list)
print(song_list)'''

def main_compare_sorting(file):
    # Setup
    import timeit as timeit
    list_of_songobjects = creator_of_songlistobject(file)
    list_of_songobjects = list_of_songobjects[0:1000]  # Denna rad kan användas för att korta ned listan
    n = len(list_of_songobjects)
    print("Antal element =", n)

    # Del 1
    quickso = timeit.timeit(stmt=lambda: quickSort(list_of_songobjects), number=1)
    print("Quicksort tog", round(quickso, 4), "sekunder")

    # Del 2 binärsökning börjar här. Notera att vi matar in ett object som sökes.
    list_of_songobjects.sort()
    urvsort = timeit.timeit(stmt=lambda: urvalssortera(list_of_songobjects), number=1)
    print("URvalssortering tog", round(urvsort, 4), "sekunder")

main_compare_sorting("unique_tracks.txt")


# Tiden är ordo(n^2) för urvalssortering, den skenar snabbt
# Tiden är ordo(nlogn) för quicksort, den ökar i något som inte är långt ifrån linjärt.
