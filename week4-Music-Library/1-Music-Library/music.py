import datetime
import random
import time
from tabulate import tabulate
import json


class SongLength:
    def __init__(self, length):
        self.length = length
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        parts = [int(part.strip()) for part in length.split(":")]

        if len(parts) == 3:
            self.hours = parts[0]
            self.minutes = parts[1]
            self.seconds = parts[2]
        elif len(parts) == 2:
            self.minutes = parts[0]
            self.seconds = parts[1]
        else:
            raise ValueError("Length not proper format: {}".format(length))

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.hours * 60 + self.minutes

    def get_seconds(self):
        return self.get_minutes() * 60 + self.seconds


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.__lengthObject = SongLength(length)

    def __str__(self):
        return "{} - {} from {} - {}"\
            .format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__str__())

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

    def get_length(self, seconds=False, minutes=False, hours=False):
        if not seconds and not minutes and not hours:
            return self.__length

        if seconds:
            return self.__lengthObject.get_seconds()

        if minutes:
            return self.__lengthObject.get_minutes()

        if hours:
            return self.__lengthObject.get_hours()


class Playlist:
    def __init__(self, name, repeat="NONE", shuffle=False):
        self.__songs = []
        self.__name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__current_song_index = 0
        self.__shuffle_played_songs = set()

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, song):
        try:
            self.__songs.remove(song)
        except ValueError:
            pass

    def total_length(self):
        total_seconds = sum([song.get_length(seconds=True) for song in self.__songs])
        return str(datetime.timedelta(seconds=total_seconds))

    def artists(self):
        all_artists = [song.artist for song in self.__songs]
        return {name: all_artists.count(name) for name in all_artists}

    def __has_next_song(self):
        return self.__current_song_index < len(self.__songs)

    def __shuffle(self):
        song = random.choice(self.__songs)

        while song in self.__shuffle_played_songs:
            song = random.choice(self.__songs)

        self.__shuffle_played_songs.add(song)

        if len(self.__shuffle_played_songs) == len(self.__songs):
            self.__shuffle_played_songs = set()

        return song

    def next_song(self):
        if self.repeat == "SONG":
            return self.__songs[self.__current_song_index]

        if self.shuffle:
            return self.__shuffle()

        if not self.__has_next_song() and self.repeat == "NONE":
            raise Exception("End of playlist")

        if not self.__has_next_song() and self.repeat == "PLAYLIST":
            self.__current_song_index = 0

        song = self.__songs[self.__current_song_index]
        self.__current_song_index += 1

        return song

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []

        for song in self.__songs:
            table.append([song.artist, song.title, song.length])

        print(tabulate(table, headers=headers))

    def prepare_json(self):
        data = {
            "name": self.__name,
            "songs": [song.prepare_json() for song in self.__songs]
        }

        return data

    def save(self, indent=True):
        filename = self.__name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p


def test_load():
    p = Playlist.load("Manowar-songs.json")
    try:
        while True:
            song = p.next_song()
            print(str(song))
            time.sleep(1)
    except Exception as e:
        print(e)


def test_save():

    s = Song(album="The Sons of Odin", title="Odin", artist="Manowar", length="3:44")
    s1 = Song(album="The Sonds of Odin", title="Sons of Odin", artist="Manowar", length="6:08")
    p = Playlist("Manowar songs", repeat="SONG")
    p.add_song(s)
    p.add_song(s1)
    p.add_song(Song(album="Fallen", title="Bring Me To Life (radio edit)", artist="Evanesence", length="3:30"))

    p.pprint_playlist()

    p.save()


test_load()

