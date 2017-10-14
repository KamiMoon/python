current_users = ['admin', 'root', 'power', 'some', 'blank']
new_users = ['admi1n', 'root1', 'power', 'some', 'blank1']

for user in new_users:
    if user.lower() in current_users:
        print('Already in use - ' + user)
    else:
        print('Good - ' + user)