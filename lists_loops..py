guests = ['akmal', 'said', 'lenur', 'Jacob']
print('Hello ' + guests[0].title() + ', I am inviting you to the party')
print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')
print(f'Hello guests[0].title ,I am inviting you to the party')
removed_guest = guests.pop(1)
# removed_guest2 = guests.remove('akmal')
# a = 'said' same think as line 7
# said can't make it to the party
print(guests)
print(f'{removed_guest}, cant make it to the party')
# print(f'{removed_guest2}, cant make it to the party')
guests.append('max')
print(guests)
print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[3].title()}, I am inviting you to the party')




