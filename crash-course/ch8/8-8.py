def make_album(artist_name, album_title, tracks=0):
    music = {}
    music['artist_name'] = artist_name
    music['album_title'] = album_title

    if tracks > 0:
        music['tracks'] = tracks
    
    return music


while True:
    name = input("Enter name: ")

    if name == 'quit':
        break
    
    title = input("Enter title: ")

    print(str(make_album(name, title)))