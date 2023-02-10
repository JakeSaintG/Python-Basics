movies = {'The Grinch': "11:00am",
          'Rudolph': "1:00pm",
          'Frosty the Snowman': "3:00pm",
          'Christmas Vacation': "5:00pm"}

print("We are showing the following movies:")

for key in movies:
    print(key)

userPick = input('What movie would you like a showtime for?\n\n')

showtime = movies.get(userPick)

if not showtime:
    print("WE AREN'T SHOWING THAT ONE, NERD!")
else:
    print(userPick, 'is playing at', showtime)
