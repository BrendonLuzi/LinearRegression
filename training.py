import numpy
import pandas as pandas
import matplotlib.pyplot as pyplot

def save_parameters(price_min, price_max, mileage_min, mileage_max, theta0, theta1):
	param = open('parameters.txt', 'w')
	param.truncate()
	param.write('{\n')
	param.write(f'\tMin price: {price_min}\n')
	param.write(f'\tMax price: {price_max}\n')
	param.write(f'\tMin mileage: {mileage_min}\n')
	param.write(f'\tMax mileage: {mileage_max}\n')
	param.write(f'\tTheta0: {theta0}\n')
	param.write(f'\tTheta1: {theta1}\n')
	param.write('}')
	param.close()

# Normalize function
def normalize(values):
	return (values - values.min()) / (values.max() - values.min())

# Linear regression
def linear_regression(x, y, n, learning_speed):
	# Initial parameters of the line that describes the data where price = mileage * theta1 + theta0
	theta0 = 0.0
	theta1 = 0.0

	# Initialize mean sqaured error variable
	mse = 0

	# Loop until convergence or 1000000 epochs
	for _ in range(1000000):
		# Predictions of the y values acoording to the temporary parameters
		est_y = x * theta1 + theta0
		# Error estimation
		error = est_y - y

		# Calculation of the mean squared error to determine if we reached convergence
		new_mse = (1 / n) * numpy.sum(error ** 2)
		# If the difference in the mse is small enough, convergence has been reached, quit the loop
		if abs(new_mse - mse) < 0.00000000001:
			break
		# If not, update the mse value
		mse = new_mse

		# Calculation of the gradients
		grad_theta0 = (1 / n) * numpy.sum(error)
		grad_theta1 = (1 / n) * numpy.sum(error * x)
		
		# Update the parameters
		theta0 = theta0 - learning_speed * grad_theta0;
		theta1 = theta1 - learning_speed * grad_theta1;

	return theta0, theta1;

# Read the dataset and define the initial parameters
try:
	dataset = pandas.read_csv("data.csv")

	price = dataset['price']
	mileage = dataset['km']
except:
	print('Error reading the dataset!'), exit()

# Normalize the values
norm_price, norm_mileage = normalize(price), normalize(mileage)

n = len(price)

learning_speed = 0.001

# Compute the parameters training the model
theta0, theta1 = linear_regression(numpy.array(norm_mileage), numpy.array(norm_price), n, learning_speed)

# Save the parameters
save_parameters(price.min(), price.max(), mileage.min(), mileage.max(), theta0, theta1)

if input('Model trained! Input \'y\' to see the results plotted...', ) == 'y':
	# Plot the results
	pyplot.scatter(norm_mileage, norm_price)
	pyplot.plot(norm_mileage, (norm_mileage * theta1) + theta0, color='red')

	pyplot.show()
