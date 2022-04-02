import os
import os.path
import sys
import json
import importlib
import shutil
import math

from PIL import Image
from itertools import combinations
from celloapi2 import CelloQuery, CelloResult


# Set our directory variables.  If you have a Windows based
# operating system you need to input window based paths.
in_dir = os.path.join(os.getcwd(), 'input')
out_dir = os.path.join(os.getcwd(), 'output')

#User input decides what circuit we are building with which parts
print('Welcome to Gee-COD, Genetic Circuit Optimizated Designer')
print('With this tool, you will be able to import your own design, or create your own, and then choose specific functions to optimize your design')
verilog_file_yes_no = input("Do you wish to import your own gate design (.v file) ? ")

if verilog_file_yes_no == "yes":
	# Source path
	sourceAddress = input('What is the path of directory of your file(Please use double\\ format):')
	sourceFile = input('What is the name of your file (.v file) :')
	src = sourceAddress + '\\' + sourceFile
	print(src)
	print(os.getcwd())
	print(f'input\\{sourceFile}')
	dest = os.path.join(os.getcwd(), f'input\\{sourceFile}')
	try:
		shutil.copy(src, dest)
		print("File copied successfully.")

	# If source and destination are same
	except shutil.SameFileError: 
		print("Source and destination represents the same file.")

	# If there is any permission issue
	except PermissionError:
		print("Permission denied.")

	# For other errors
	except:
		print("Error occurred while copying file. Please use double forward slashes when providing your files path")
else:
	# Calculate number of inputs into the Circuit.
	signal_input = int(input("How many promoter inputs do you wish to have in your design :"))
	gate_select = int(input("How many gates do you wish to have in your design :"))
	v_file_select1 = input("Enter First Gate of your circuit design (and, or, not) :")
	v_file_select2 = ''
	v_file = v_file_select1 + '.v'
	
	if gate_select == 2:
		v_file_select2 = input("Enter Second Gate of your circuit design (and, or, not, xor, nand):")
		v_file = v_file_select1 + '_' + v_file_select2 + '.v'
		print(f'Verilog file for design: {v_file}')
	if gate_select == 3:
		v_file_select2 = input("Enter Second Gate of your circuit design (and, or, not, xor, nand):")
		v_file_select3 = input("Enter Third Gate of your circuit design (and, or, not, xor, nand):")
		v_file = v_file_select1 + '_' + v_file_select2 + '_' + v_file_select3 + '.v'
	print(f'Verilog file for design: {v_file}')




# Let use determine chassis library for design
chassis_num = int(input("How many bacteria chassis would you like to compare (functional for only 1 at the moment):"))
chassis_select1 = input("Enter First E-coli Chassis' option (Eco1C1G1T1(only one that is function), Eco1C2G2T2, Eco2C1G3T1):")
chassis_name = [chassis_select1]
if chassis_num == 2:
	chassis_select2 = input("Enter Second E-coli Chassis' option (Eco1C1G1T1, Eco1C2G2T2, Eco2C1G3T1):")
	chassis_name = [chassis_select1,chassis_select2]
if chassis_num == 3:
	chassis_select2 = input("Enter Second E-coli Chassis' option (Eco1C1G1T1, Eco1C2G2T2, Eco2C1G3T1):")
	chassis_select3 = input("Enter Third E-coli Chassis' option (Eco1C1G1T1, Eco1C2G2T2, Eco2C1G3T1):")
	chassis_name = [chassis_select1,chassis_select2,chassis_select3]
print(f'Chassis options selected for design: {chassis_name}')





#functions to be applied to the inputs
def  stretch(dictionary,value):
	for x in  range(0, 15,4):
		dictionary[x] = float(dictionary[x]) * value
		dictionary[x + 1] = float(dictionary[x + 1]) / value
	return dictionary

def  increaseslope(dictionary,value):
	for x in  range(2, 14,4):
		dictionary[x] = dictionary[x] * value
		x = x + 4
	return dictionary

def  decreaseslope(dictionary,value):
	for x in  range(2, 14,4):
		dictionary[x] = dictionary[x] / value
		x = x + 4
	return dictionary

def  strongpromoter(dictionary,value):
	for x in  range(0, 15,4):
		dictionary[x] = dictionary[x] / value
		dictionary[x + 1] = dictionary[x + 1] / value
		x = x + 4
	return dictionary

def  Weakerpromoter(dictionary,value):
	for x in  range(0, 15,4):
		dictionary[x] = dictionary[x] / value
		dictionary[x + 1] = dictionary[x + 1] / value
		x = x + 4
	return dictionary

def  StrongerRBS(dictionary,value):
	for x in  range(3, 15,4):
		dictionary[x] = dictionary[x] / value
		x = x + 4
	return  dictionary

def  WeakerRBS(dictionary,value):
	for x in  range(3, 15,4):
		dictionary[x] = dictionary[x] * value
		x = x + 4
	return  dictionary



#open the input file selected to be able to apply functions to
f = open(os.path.join(os.getcwd(), 'input\\Eco1C1G1T1.input.json'))
#f = open(r'C:\Users\steph\Documents\ec552\hw1\input\Eco1C1G1T1.input.json')
data = json.load(f)

y_max = []
y_min = []
alpha = []
beta = []
dictionary = []
for x in range(len(data)):
	if data[x]['collection'] == 'models':
		for i in range(0,4):
			dictionary.append(data[x]['parameters'][i]['value'])
		if i == 0:
			  y_max.append(data[x]['parameters'][i]['value'])
		elif i == 1:
			  y_min.append(data[x]['parameters'][i]['value'])
		elif i == 2:
			  alpha.append(data[x]['parameters'][i]['value'])
		else:
			  beta.append(data[x]['parameters'][i]['value'])
			 


# Let use determine if user wants to apply functions to gate library
function_select = input('Do you wish to apply one of the following functions to the gate library: \n a. Stretch \n b. Increase slope \n c. Decrease slope \n d. Stronger promoter \n e. Weaker promoter \n f. Stronger RBS \n g. Weaker RBS \n h. None \n Please enter function:')
print(f'You chose option {function_select}')

if function_select == 'Stretch':
	value = float(input('What value (at most 1.5) would you like to stretch by?:'))
	dictionary = stretch(dictionary,value)

if function_select == 'Increase slope':
	value = float(input('What value (at most 1.05) would you like to increase slope by?:'))
	dictionary = increaseslope(dictionary,value)

if function_select == 'Decrease slope':
	value = float(input('What value (at most 1.05) would you like to decrease slope by?:'))
	dictionary = decreaseslope(dictionary,value)

if function_select == 'Stronger promoter':
	value = float(input('What value multiplier would you like to increase promoter by?:'))
	dictionary = strongpromoter(dictionary,value)

if function_select == 'Weaker promoter':
	value = float(input('What value divider would you like to decrease promoter by?:'))
	dictionary = Weakerpromoter(dictionary,value)

if function_select == 'Stronger RBS':
	value = float(input('What value do you choose for stronger RBS?:'))
	dictionary = StrongerRBS(dictionary,value)

if function_select == 'Weaker RBS':
	value = float(input('What value do you choose for weaker RBS?:'))
	dictionary = WeakerRBS(dictionary,value)




counter = 0
for x in range(len(data)):
	if data[x]['collection'] == 'models':
		for i in range(0,4):  
			data[x]['parameters'][i]['value'] = dictionary[counter]
			counter = counter + 1
json_object = json.dumps(data, indent = 4)

# Writing json after function has been applied to ModifiedEco1C1G1T1... this will rewrite over itself each time in the input folder
print(dictionary)
with open(os.path.join(os.getcwd(), 'input\\ModifiedEco1C1G1T1.input.json'), "w") as outfile:
	outfile.write(json_object)

options = 'options.csv'

#API code integrated with Cello to get best score for 
best_score = 0
best_chassis = None
best_input_signals = None
for chassis in chassis_name:
	in_ucf = 'Eco1C1G1T1.UCF.json'
	if function_select == 'None':
		input_sensor_file = f'{chassis}.input.json'
	else:
		input_sensor_file = 'ModifiedEco1C1G1T1.input.json'
	output_device_file = 'Eco1C1G1T1.output.json'


	
	q = CelloQuery(input_directory=in_dir,
		output_directory=out_dir,
		verilog_file=v_file,
		compiler_options=options,
		input_ucf=in_ucf,
		input_sensors=input_sensor_file,
		output_device=output_device_file,)
	signals = q.get_input_signals()
	signal_pairing = list(combinations(signals, signal_input))
	for signal_set in signal_pairing:
		signal_set = list(signal_set)
		q.set_input_signals(signal_set)
		q.get_results()
		try:
			res = CelloResult(results_dir=out_dir)
			logscore = math.log10(res.circuit_score)
			#print to make sure best is updating
			print(logscore)
			if logscore > best_score:
				best_score = logscore
				
				best_diagram_location = os.path.join(os.getcwd(), f'output\\gatedesign_technologyMapping.png')
				#print(best_diagram_location)
				#best_eugene_diagram_location = os.path.join(os.getcwd(), f'output\\gatedesign_dpl.png') #only seemed to work for a few, ex AND gate
				#print to see that it is updating
				print(best_score)
				best_chassis = chassis
				best_input_signals = signal_set
			#print(best_diagram_location)
		except:
			pass
		q.reset_input_signals()
	print('-----')


print(f'Best Score: {best_score}')
print(f'Best Chassis: {best_chassis}')
print(f'Best Input Signals: {best_input_signals}')

#bestimage = Image.open(best_diagram_location)
#bestimage.show()