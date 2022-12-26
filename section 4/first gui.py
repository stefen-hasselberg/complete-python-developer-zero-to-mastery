# Exercise
# Loop through the list of list
# each time we encounter a  0
# display a empty space
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# 1 iterate over pictue.
# if 0 => print ''
# if 1 => print '*'

for image in picture:
    for pixel in image:
        if pixel == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
