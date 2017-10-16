magician_names = ['Alex', 'Jo', 'Bob']

def show_magicians(magician_names):
    for name in magician_names:
        print(name)


def make_great(magician_names):
    for i, name in enumerate(magician_names):
        magician_names[i] = name + ' The Great'
    return magician_names

copy = make_great(magician_names[:])
show_magicians(magician_names)
show_magicians(copy)