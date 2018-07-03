# -*- coding: utf-8 -*-
'''
Loops in a program go over a particular set of actions repeatedly until a condition is met/not met. 
Below is a list with a set of numbers as given below. 
Print out all the even numbers in the sequence. Write the solution (in Python 3) into a function and have it called in your main block for the requested answer.

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]


eg:
find_even()
output : The even numbers are : 2,4,6,8
'''

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

def find_even():
	even_list = []
	for sequence in numbers:
		value_list = sequence['sequence'].split(",")
		for value in value_list:
			int_value = int(value)
			if int_value > 0 and int_value%2 == 0:
				even_list.append(value)
	print ("The even numbers are : %s " % (", ".join(even_list)))
	pass

def find_even_1():
	even_map = {}
	even_list = []
	for sequence in numbers:
		value_list = sequence['sequence'].split(", ")
		for value in value_list:
			for seq in range(0, len(value)):
				int_value = int(value[seq])
				if int_value > 0 and int_value%2 == 0:
					even_map[value[seq]] = int_value
	for key_val in even_map.keys():
		even_list.append(key_val)
	even_list.sort()
	print ("The even numbers are : %s " % (", ".join(even_list)))

	pass

def main():
	find_even()
	find_even_1()
if __name__ == "__main__":
	main()
	