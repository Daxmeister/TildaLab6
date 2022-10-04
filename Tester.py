
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





def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i + 1, n):
            if data[j] < data[minst]:
                minst = j
        data[minst], data[i] = data[i], data[minst]


def creator_of_songlistobject(file):
    with open(file) as song_file:
        song_object_list = []
        for line in song_file:
            song_object_list.append(Song(line))
    return song_object_list

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

    def __eq__(self, other):
        return self.artist == other.artist

    def __gt__(self, other):
        return self.artist > other.artist

    def __str__(self):
        return self.artist

    def __repr__(self):
        return str ("Object " + self.artist)

    def __hash__(self):
        return hash(self.artist)

list_of_songobjects = creator_of_songlistobject("unique_tracks_mini.txt")
list = [2, 4, 1, 5, 2, 5]
urvalssortera(list)
print(list_of_songobjects)
urvalssortera(list_of_songobjects)
print(list_of_songobjects)

def is_greater(object1, object2):
    if object1 > object2:
        print ("first bigger")
    if object1 == object2:
        print ("Is same")
    if object1 < object2:
        print("Second bigger")

#is_greater()
is_greater(list_of_songobjects[2], list_of_songobjects[4])