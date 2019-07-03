#from matplotlib import pyplot as plt

file_name = input("Enter the .csv file name: ")

f = open(file_name + ".csv", "r")
lines = f.readlines()
for line in lines:
	value = line.split(",")
	print(value[3])

f.close()

