# Function to retrieve the parameters found from the training
def get_params():
	try:
		p_file = open('parameters.txt')
		parameters = p_file.readlines()[1:-1]
	except:
		print('No parameters found, try training the model first!'), exit()

	# For every string, trim and find the value, convert to float and store it
	for i, param in enumerate(parameters):
		parameters[i] = float(param[param.find(':') + 1:])

	return parameters

# Input the requested mileage
try:
	mileage = float(input('Hi! What\'s your car mileage? '))
except:
	print('That\'s not a valid mileage!'), exit()

if (mileage < 0):
	print('Yes, and it\'s a time machine! Give me a real mileage!'), exit()

# Get params
parameters = get_params()
p_price = parameters[:2]
p_mileage = parameters[2:4]
theta = parameters[4:]

# Normalize according to the training model params
mileage = (mileage - p_mileage[0]) / (p_mileage[1] - p_mileage[0])

# Estimate price
price = theta[1] * mileage + theta[0]

# Denormalize the price and round the price
price = price * (p_price[1] - p_price[0]) + p_price[0]
price = round(price)

if price <= 0:
	print('Maybe it\'s time to get rid of it...')
print(f'Your car should be valued around {price} euro!')