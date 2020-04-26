import matplotlib.pyplot as plt

x=list()
y=list()

def visualise(filename):
	with open(filename) as fh:
		for line in fh:
			pt=line.split(',')
			x.append(float(pt[0]))
			y.append(float(pt[1]))

	plt.scatter(x, y)
	plt.title(filename)
	plt.xlabel('X axis')
	plt.ylabel('Y axis')
	plt.show()

	print("The nummber of data points are:",len(x))


visualise("outlier.txt")
