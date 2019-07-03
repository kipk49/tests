#from matplotlib import pyplot as plt

file_name = input("Enter the .csv file name: ")

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

print(label_list)

print(number_list)

f.close()

