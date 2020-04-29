# At first, you might think that switchLights() should simply switch each light to the next color in the sequence:
# Any 'green' values should change to 'yellow', 'yellow' values should change to 'red', and 'red' values should change to 'green'.
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'


assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)


# Since you’ve already written the rest of the program, you have no idea where the bug could be.
# Maybe it’s in the code simulating the cars or in the code simulating the virtual drivers.
# It could take hours to trace the bug back to the switchLights() function.

# But if while writing switchLights() you had added an assertion to check that at least one of the lights is always red
