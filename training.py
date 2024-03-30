import numpy
import json
import pandas as pandas
import matplotlib.pyplot as pyplot

EPOCHS_LIMIT = 1000000
PRECISION = 0.00000000001
LEARNING_SPEED = 0.001

def save_parameters(theta0, theta1):
	params = {
		"Theta0": theta0,
		"Theta1": theta1
	}
	with open("parameters.json", "w") as file:
		json.dump(params, file)

# Normalize function
def normalize(values):
	return (values - values.min()) / (values.max() - values.min())

# Mean squared error
def mean_squared_error(y, est_y):
	return numpy.mean((y - est_y) ** 2)

# Gradient descent
def gradient_descent(x, y, n):
	# Initial parameters of the line that describes the data where price = mileage * theta1 + theta0
	theta0 = 0.0
	theta1 = 0.0
	# Initialize mean sqaured error variable
	mse = 0

	# Loop until convergence or until a predetermined amount of iterations
	for _ in range(EPOCHS_LIMIT):
		# Predictions of the y values acoording to the temporary parameters
		est_y = x * theta1 + theta0
		# Error estimation
		error = est_y - y

		# Calculation of the mean squared error to determine if we reached convergence
		new_mse = mean_squared_error(y, est_y)
		# If the difference in the mse is small enough, convergence has been reached, quit the loop
		if abs(new_mse - mse) < PRECISION:
			break
		# If not, update the mse value
		mse = new_mse

		# Calculation of the gradients
		grad_theta0 = numpy.sum(error) / n
		grad_theta1 = numpy.sum(error * x) / n
		
		# Update the parameters
		theta0 = theta0 - LEARNING_SPEED * grad_theta0
		theta1 = theta1 - LEARNING_SPEED * grad_theta1

	return theta0, theta1

def plot_results(x, y, theta0, theta1):
	# Plot the results
	pyplot.scatter(x, y)
	pyplot.plot(x, (x * theta1) + theta0, color='red')

	pyplot.show()

def main():
	# Read the dataset and define the initial parameters
	try:
		dataset = pandas.read_csv("data.csv")

		price = dataset['price']
		mileage = dataset['km']
	except:
		print('Error reading the dataset!'), exit()

	# Normalize the values
	norm_price, norm_mileage = normalize(price), normalize(mileage)

	# Compute the parameters training the model
	theta0, theta1 = gradient_descent(numpy.array(norm_mileage), numpy.array(norm_price), len(norm_price))

	# Denormalize the parameters
	theta1 = theta1 * (price.max() - price.min()) / (mileage.max() - mileage.min())
	theta0 = theta0 * (price.max() - price.min()) + price.min() - theta1 * mileage.min()

	# Save the parameters
	save_parameters(theta0, theta1)

	if input('Model trained! Input \'y\' to see the results plotted...', ) == 'y':
		plot_results(mileage, price, theta0, theta1)

if __name__ == '__main__':
	main()