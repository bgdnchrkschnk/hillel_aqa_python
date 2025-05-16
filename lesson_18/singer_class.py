class Song:
    TOTAL_SONGS = 0

    def __init__(self, title, artist, bpm):
        self.title = title
        self.artist = artist
        self.__bpm = bpm
        self.__increment_song()


    @classmethod
    def get_total_songs(cls):
        return cls.TOTAL_SONGS

    @property
    def bpm(self):
        return self.__bpm

    @bpm.setter
    def bpm(self, new_bpm):
        if new_bpm in range(29, 200):
            self.__bpm = new_bpm
        else:
            raise ValueError(f"new_bpm {new_bpm} must be between 29 and 200")

    @bpm.deleter
    def bpm(self):
        del self.__bpm

    def __increment_song(self):
        Song.TOTAL_SONGS += 1


    @staticmethod
    def convert_bpm_to_miliseconds(bpm):
        return bpm * 1000

    def __str__(self):
        return f"The title is {self.title}, and the artist is {self.artist} (BPM: {self.__bpm})"



rock_song: Song = Song('Die MF!', 'HardFucker', 140)
pop_song: Song = Song("Love 4ever", "Sweetkitty", 100)
rap_song: Song = Song("Street life", "Lil Python", 80)

print(pop_song.get_total_songs())
print(Song.get_total_songs())


print(
    Song.convert_bpm_to_miliseconds(bpm=120)
)
print(
    rock_song.convert_bpm_to_miliseconds(bpm=120)
)


# print(rock_song)
# print(pop_song)
# print(rap_song)
#
# print(rock_song.bpm)
# print(pop_song.bpm)
# print(rap_song.bpm)
#
# rap_song.bpm = 180
# print(rap_song.bpm)




