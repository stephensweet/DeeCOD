import os
import os.path
import sys
import json
import importlib
import shutil
import math
import tkinter as tk
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import numpy as np


from itertools import combinations
from celloapi2 import CelloQuery, CelloResult

# Set our directory variables.  If you have a Windows based
# operating system you need to input window based paths.
in_dir = os.path.join(os.getcwd(), 'input')
out_dir = os.path.join(os.getcwd(), 'output')

#global variables for GUI-program interface
global input_params
input_params = [0]*6

global check_butn_params
check_butn_params = [0]*7

#GUI functions
def show_frame(frame):
    frame.tkraise()

def cont_button(frame):
    show_frame(frame)
    # global input_params
    # input_params = [0]*5
    input_params[0]=var_inp.get()
    input_params[1]=var_num.get()
    input_params[2]=var_chas.get()
    input_params[3]=var.get()
    input_params[4]=var2.get()
    input_params[5]=var3.get()

def check_button(x):
    if check_butn_params[x]==0:
        check_butn_params[x] = 1
    else:
        check_butn_params[x] = 0
    
def run_circ_button(frame):
    show_frame(frame)
    op_p = np.array(['0.00', '0.00', '0.00', '0.00', '0.00'])
    op_p[0] = ce1.get()
    op_p[1] = ce2.get()
    op_p[2] = ce3.get()
    op_p[3] = ce4.get()
    op_p[4] = ce5.get()
    global operation_params
    operation_params = np.array([0.00, 0.00, 0.00, 0.00, 0.00])
    for i in range(0,5):
        if op_p[i] == '':
            op_p[i] = '0.00'
    operation_params = op_p.astype(np.double)

###################################################################### GUI ######################################################################
window = Tk()
window.geometry("900x600")
window.title("Gee-COD")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame0 = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

for frame in (frame0, frame1, frame2, frame3, frame4):
    frame.grid(row=0,column=0,sticky='nsew')

#==================Frame0 code

# image1 = Image.open("/Users/nikypopov/Desktop/homework1/GeeCOD_logo.png")
# test = ImageTk.PhotoImage(image1)
# label1 =tkinter.Label(image=test)
# label1.image=test
# label1.place(x=1, y=1)

#==================Frame 1 code
OPTIONS = ["and", "nor", "not", "none"]
NUMS = ["1"]
NUMS2 = ["1", "2", "3"]
CHASIS = ["Eco1C1G1T1"]

l0 = tk.Label(frame1, text = "Welcome to Gee-COD - The Genetic Circuit Optimized Designer")
l0.place(x=250, y=50)
lt = tk.Label(frame1, text = "Would you like to see a brief tutorial? ")
lt.place(x=150, y=100)

l_inp = tk.Label(frame1, text = "How many promoter inputs would you like? ")
l_inp.place(x=150, y=150)

l_nums = tk.Label(frame1, text = "How many chasses do you want to compare?")
l_nums.place(x=150, y=200)

l_chas = tk.Label(frame1, text = "Select First chassis")
l_chas.place(x=150, y=250)

#drop down selections
var = StringVar(frame1)
var.set(OPTIONS[0]) # default value
w = OptionMenu(frame1, var, *OPTIONS)
w.place(x=450, y=300)

var2 = StringVar(frame1)
var2.set(OPTIONS[1])
w2 = OptionMenu(frame1, var2, *OPTIONS)
w2.place(x=450, y=350)

var3 = StringVar(frame1)
var3.set(OPTIONS[2])
w3 = OptionMenu(frame1, var3, *OPTIONS)
w3.place(x=450, y=400)

var_num = StringVar(frame1)
var_num.set(NUMS[0])
w4 = OptionMenu(frame1, var_num, *NUMS)
w4.place(x=450, y=200)

var_chas = StringVar(frame1)
var_chas.set(CHASIS[0])
w_c = OptionMenu(frame1, var_chas, *CHASIS)
w_c.place(x=450, y=250)

var_inp = StringVar(frame1)
var_inp.set(NUMS2[0])
w5 = OptionMenu(frame1, var_inp, *NUMS2)
w5.place(x=450, y=150)

#gate selection label
l2 = tk.Label(frame1, text = "Select first gate: ")
l3 = tk.Label(frame1, text = "Select second gate: ")
l4 = tk.Label(frame1, text = "Select third gate: ")

l2.place(x=150, y=300)
l3.place(x=150, y=350)
l4.place(x=150, y=400)


#tutorial button
tut_btn = tk.Button(frame1, text='Tutorial',command=lambda:show_frame(frame2))
tut_btn.place(x=450, y=96)

submit = Button(frame1,text="Continue", command=lambda:cont_button(frame3))
submit.place(x=700, y=500)

#==================Frame 2 code

frame2_btn = tk.Button(frame2, text='Back to Menu',command=lambda:show_frame(frame1))
frame2_btn.place(x=30, y=20)

#==================Frame 3 code

#labels
frame3_title=  tk.Label(frame3, text='What Operations do you want to apply to your input signal?')
frame3_title.place(x=30, y = 20)

run = Button(frame3,text="Run Circuit", command=lambda:run_circ_button(frame4))
run.place(x=700, y=500)

#entry box labels
c1_entry = Label(frame3,text="Enter strech paramater (must be <1.05): ")
c1_entry.place(x=240, y=100)

c2_entry = Label(frame3,text="Enter slope increase/decrease parameter (must be <1.05): ")
c2_entry.place(x=240, y=160)

c3_entry = Label(frame3,text="Enter promoter adjustment parameter: ")
c3_entry.place(x=240, y=230)

c4_entry = Label(frame3,text="Enter alpha parameter for RBS adjustment: ")
c4_entry.place(x=240, y=300)

c5_entry = Label(frame3,text="Enter beta parameter for RBS adjustment: ")
c5_entry.place(x=240, y=340)


#entry boxes
ce1=DoubleVar()
ce2=DoubleVar()
ce3=DoubleVar()
ce4=DoubleVar()
ce5=DoubleVar()

ce1 = Entry(frame3) 
ce2 = Entry(frame3) 
ce3 = Entry(frame3)
ce4 = Entry(frame3)
ce5 = Entry(frame3)
ce1.place(x=610, y=100)
ce2.place(x=610, y=160)
ce3.place(x=610, y=230)
ce4.place(x=610, y=300)
ce5.place(x=610, y=340)

#checkbuttons
c1 = Checkbutton(frame3,text="Stretch", relief=SUNKEN, command=lambda:check_button(0))
c1.place(x=30, y=100)

c2 = Checkbutton(frame3,text="Increase Slope",relief=SUNKEN, command=lambda:check_button(1))
c2.place(x=30, y = 140)

c3 = Checkbutton(frame3,text="Decrease Slope",relief=SUNKEN, command=lambda:check_button(2))
c3.place(x=30, y = 180)

c4 = Checkbutton(frame3,text="Stronger Promoter",relief=SUNKEN, command=lambda:check_button(3))
c4.place(x=30, y = 220)

c5 = Checkbutton(frame3,text="Weaker Promoter",relief=SUNKEN, command=lambda:check_button(4))
c5.place(x=30, y = 260)

c6 = Checkbutton(frame3,text="Strong RBS",relief=SUNKEN, command=lambda:check_button(5))
c6.place(x=30, y = 300)

c7 = Checkbutton(frame3,text="Weak RBS",relief=SUNKEN, command=lambda:check_button(6))
c7.place(x=30, y = 340)

#==================Frame 4 code

frame4_btn = tk.Button(frame4, text="Run New Design",command=lambda:run_circ_button(frame1))
frame4_btn.place(x=700, y=500)

#==================

show_frame(frame1)
window.mainloop()
###################################################################################################################################################


########################################################### MAIN PROGRAM ##########################################################################


## edit GUI to have option for user input .v
verilog_file_yes_no = "no"

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
	signal_input = int(input_params[0])
	# gate_select = int(input("How many gates do you wish to have in your design :"))
	# v_file_select1 = (input_params[3])
	# v_file_select2 = ''
	# v_file = v_file_select1 + '.v'
	# print(f'Verilog file for design: {v_file}')
	# if gate_select == 2:
	# 	v_file_select2 = input("Enter Second Gate of your circuit design (and, or, not, xor, nand):")
	# 	v_file = v_file_select1 + '_' + v_file_select2 + '.v'
	# 	# print(f'Verilog file for design: {v_file}')
	# if gate_select == 3:
	# 	v_file_select2 = input("Enter Second Gate of your circuit design (and, or, not, xor, nand):")
	# 	v_file_select3 = input("Enter Third Gate of your circuit design (and, or, not, xor, nand):")
	# 	v_file = v_file_select1 + '_' + v_file_select2 + '_' + v_file_select3 + '.v'
	# 	# print(f'Verilog file for design: {v_file}')

if input_params[4]=='none' and input_params[5]=='none':
    v_file_select1 = (input_params[3])
    v_file = v_file_select1 + '.v'
elif input_params[4]!='none' and input_params[5]=='none':
        v_file_select1 = input_params[3]
        v_file_select2 = input_params[4]
        v_file = v_file_select1 + '_' + v_file_select2 + '.v'
else:
    v_file_select1 = input_params[3]
    v_file_select2 = input_params[4]
    v_file_select3 = input_params[5]
    v_file = v_file_select1 + '_' + v_file_select2 + '_' + v_file_select3 + '.v'


chassis_name = input_params[2]

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

if check_butn_params[0] == 1:
   dictionary = stretch(dictionary,operation_params[0])

if check_butn_params[1] == 1:
   dictionary = increaseslope(dictionary,operation_params[1])

if check_butn_params[2] == 1:
   dictionary = decreaseslope(dictionary,operation_params[1])

if check_butn_params[3] == 1:
	dictionary = strongpromoter((dictionary,operation_params[2]))

if check_butn_params[4] == 1:
	dictionary = Weakerpromoter((dictionary,operation_params[2]))

if check_butn_params[5] == 1:
	dictionary = StrongerRBS((dictionary,operation_params[3]))

if check_butn_params[6] == 1:
	dictionary = WeakerRBS((dictionary,operation_params[4]))

counter = 0
for x in range(len(data)):
	if data[x]['collection'] == 'models':
		for i in range(0,4):  
			data[x]['parameters'][i]['value'] = dictionary[counter]
			counter = counter + 1
json_object = json.dumps(data, indent = 4)

# Writing to sample.json
print(dictionary)
with open(os.path.join(os.getcwd(), 'input\\sample1.input.json'), "w") as outfile:
	outfile.write(json_object)

options = 'options.csv'


#API code integrated with Cello
best_score = 0
best_chassis = None
best_input_signals = None
for chassis in chassis_name:
	in_ucf = 'Eco1C1G1T1.UCF.json'
	if sum(operation_params) == 0:
		input_sensor_file = 'Eco1C1G1T1.input.json'
	else:
		input_sensor_file = 'sample1.input.json'
	output_device_file = 'Eco1C1G1T1.output.json'

	
	q = CelloQuery(input_directory=in_dir,
		output_directory=out_dir,
		verilog_file=v_file,
		compiler_options=options,
		input_ucf=in_ucf,
		input_sensors=input_sensor_file,
		output_device=output_device_file,)
	signals = q.get_input_signals()
	signal_pairing = list(combinations(signals, 2))
	for signal_set in signal_pairing:
		signal_set = list(signal_set)
		q.set_input_signals(signal_set)
		q.get_results()
		try:
			res = CelloResult(results_dir=out_dir)
			logscore = print(math.log10(res.circuit_score))
			if logscore > best_score:
				best_score = logscore
				print(best_score)
				best_chassis = chassis
				best_input_signals = signal_set
		except:
			pass
		q.reset_input_signals()
	print('-----')
print(f'Best Score: {best_score}')
print(f'Best Chassis: {best_chassis}')
print(f'Best Input Signals: {best_input_signals}')