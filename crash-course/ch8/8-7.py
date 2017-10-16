def make_album(artist_name, album_title, tracks=0):
    music = {}
    music['artist_name'] = artist_name
    music['album_title'] = album_title

    if tracks > 0:
        music['tracks'] = tracks
    
    return music

print(str(make_album('red', 'asdf')))

print(str(make_album('rerasdd', 'asdfasf', 2)))