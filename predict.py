import json

# Function to retrieve the parameters found from the training
def get_params():
	try:
		with open('parameters.json', 'r') as file:
			parameters = json.load(file)
	except:
		print('No parameters found, try training the model first!'), exit()

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

# Estimate price
price = round(parameters['Theta1'] * mileage + parameters['Theta0'])

if price <= 0:
	print('Ehm... maybe it\'s time to get rid of it...')
else:
	print(f'Your car should be valued around {price} euro!')
