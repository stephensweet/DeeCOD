# GeeCOD
<img src="https://github.com/stephensweet/DeeCOD/blob/main/GeeCOD_logo.png" width=50% height=50%>



Genetic Circuit Optimized Designer
This tool with implementation of Cello v2, allows users to design genetic gates of their choice, or import their prexisting verilog gate file, then choose a bacterial chassis library(s).
Users have the ability to apply functions to the signal responses of the promoter inputs to maximize the responsivity of the genetic circuit.
Our output is then the optimized design given these parameters utilizing a modified simulated annealing via Cello v2.

## Requirements
[Python 3.8+](https://www.python.org/downloads/)

[Docker](https://docs.docker.com/get-docker/)

## Commands
```
docker pull cidarlab/cello-dnacompiler:latest

pip install celloapi2
```

## Instructions
For the terminal version

Some simple examples can be run using our terminal based interface by following the prompts after running the program in your environment of choice. (see workflow diagrams for more details). Currently GeeCOD only supports the Eco1C1G1T1 chassis but additional organisms can easily be incorporated into the functionality of the program if the respective input JSON files are available. 

For GUI version

Our GUI implementation can also serve as a template for how the designer tool would function. But the mapping of the GUI to the functions of our program still has some bugs, therefore the right now the GUI is still just a skeleton. Nevertheless it provides the user with the structure of how to use the design tool. 

