from matplotlib import pyplot as plt
import re

def main():
	name_list = []
	while True:
		holder = input("Enter a .csv file name, type 'done' when all files have been entered: ")
		if holder == "done":
			break
		name_list.append(holder)
	legend_counter = 0
	for name in name_list:
		labels = general(name)
		if legend_counter == 0:
			create_legend(labels)
		legend_counter += 1

def general(file_name):
	backwards_name = file_name[::-1]

	yeet = re.split("[a-z]+", backwards_name)
	bruh = yeet[0]
	bruh = bruh[::-1]

	f = open(file_name + ".csv", "r")
	lines = f.readlines()
	label_list = []
	number_list = []
	for line in lines:
		broken_line = line.split(",")
		label = broken_line[0]
		number = broken_line[3]
		if label == "":
			continue
		label_list.append(label)
		number_list.append(number)
	plotter(number_list, bruh, label_list)
	f.close()
	return label_list

def plotter(number_list, bruh, label_list):
	maximum = int(bruh) + 1000
	marker_list = ["rx", "bs", "g^", "ko", "y*", "mp", "cd"]
	count = 0
	for number in number_list:
		plt.plot(bruh, number, marker_list[count])
		count += 1
	plt.xlabel("Buffer Size")
	plt.ylabel("Power Undersupply")
	plt.axis([0, maximum, 0, 25])

def create_legend(label_list):
	plt.legend(label_list, loc = "best")

if __name__ == "__main__":
	main()
plt.show()


