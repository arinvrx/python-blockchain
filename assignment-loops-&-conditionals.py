# 1 Create a list of names and use a for loop to output the lenght of each name (len())
usernames = ['ari', 'on', 'srn', 'sis', 'canoopsy']

for name in usernames:
    print(name)
    print(len(name))

# 2 Add  an if check inside the loop to only output names longer than 5 characters.
print('-' * 30)
for name in usernames:
    if len(name) > 5:
        print(name)
        print(len(name))

# 3 Add another if check to see whether a name includes a "n" or "N" character.
print('-' * 30)
for name in usernames:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(name)
        print(len(name))
# 4 Use while loop to empty the list of names (via pop())
print('-' * 30)
while len(usernames) >= 1:
    print(usernames.pop())

print(usernames)
