#108

favorite_langues = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_langues.items():
    print(name.title() + "'s favorite language is " + language.title())

already_taken = favorite_langues.keys()
who_should_take = ['jen', 'eric', 'bob', 'phil']

for name in who_should_take:
    if(name in already_taken):
        print('Thank you for responding, ' + name)
    else:
        print('Please take the poll, ' + name)