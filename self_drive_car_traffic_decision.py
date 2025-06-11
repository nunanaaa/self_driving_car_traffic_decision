traffic_sign = input('Please enter the traffic sign colour: ').lower()

if traffic_sign == 'red':
    action = 'turn right'
elif traffic_sign == 'green':
    action = 'turn left'
else :
    action = 'Unknown sign! Drive on and perform parallel parking.'

print('Traffic sign colour detected: ',traffic_sign)
print('Car action: ',action)