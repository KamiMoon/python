guest_list = ['Bob', 'Jill', 'Jack']

guest_list.insert(0, 'George')
guest_list.insert(1, 'Alex')
guest_list.append('Drew')

print("You are invited to dinner, " + guest_list[0])
print("You are invited to dinner, " + guest_list[1])
print("You are invited to dinner, " + guest_list[2])
print("You are invited to dinner, " + guest_list[3])
print("You are invited to dinner, " + guest_list[4])
print("You are invited to dinner, " + guest_list[5])

print("Only 2 can go")


print("You can't go, " + guest_list.pop())
print("You can't go, " + guest_list.pop())
print("You can't go, " + guest_list.pop())
print("You can't go, " + guest_list.pop())

print("You can still go, " + guest_list[0])
print("You can still go, " + guest_list[1])

del guest_list[0]
del guest_list[0]

print(guest_list)