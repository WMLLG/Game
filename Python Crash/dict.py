'''
aliens = []

for elien_number in range(20):
    new_alien = {'color':'green', 'point':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['point'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print alien

print "\nTotal number of aliens: " + str(len(aliens))
'''
age = raw_input("How old are you? ")

print type(age)
