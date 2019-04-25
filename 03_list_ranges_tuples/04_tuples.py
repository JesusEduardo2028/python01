# Tuples are ordered set of data
# Similar to lists for they are inmutable so they can be changed

t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

metallica = "Ride The lighting", "Metallica", 1994
print(metallica)
# Print each element
print(metallica[0])
print(metallica[1])
print(metallica[2])

# This causes an error because tuple objects are inmutable
# TypeError: 'tuple' object does not support item assignment
# metallica[0] = "master of puppets"

#
# THIS CREATES A NEW TUPLE WITH LAST TUPLE KEYS
metallica2 = "Master of puppets", metallica[1], 1996
print(metallica2)
print(metallica)
print(metallica == metallica2)

# List are meant to hold homogenous type objects
# Tuples are meant to hold heterogeneious type objects


albumName, artist, year, tracks = "Kill em all", "Metallica", 1992, ((1, "kill em all"), (2, "Four Horsemen"))
print(albumName)
print(artist)
print(year)
print(tracks)
track1, track2 = tracks
print(track1)
print(track2)
trackNumber, trackName = track1
print(trackNumber)
print(trackName)

print("For loop example")
for song in tracks:
    track, songName = song
    print(track)
    print(songName)
    # or
    # print(song[0])
    #   print(song[1])
