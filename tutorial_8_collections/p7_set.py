# Music playlist
# set is used to carry unique values - {}
playlist = {"Jai ho", "Jai jai santoshi maa", "Wakka wakka", "Jai ho", "Wakka wakka"}
print(type(playlist))

# print(playlist[0])
index = 0
for song in playlist:
    print(f"{index} -> {song}")
    index = index + 1