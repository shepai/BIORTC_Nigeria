# Python BOOTCAMP

This part of the repository provides worksheets and support videos to guide you through the basics in preperation for the computational neurosciene course. Much of this is taken from the <a href="https://github.com/SussexPAL/PythonCrashCourse">University of Sussex PAL resouces</a>. See <a href="https://github.com/SussexPAL/PythonCrashCourse">the github</a> for more Python resources if you want to go further... We have taken the worksheets that are most related to this course's content. 

## Setup

 There are different options to run code: _locally_ or using _cloud computing_. You can use different things at different times, depending on the purpose of the code, or how good the internet connection is. 

- To run things _locally_ on your computer, you can start by installing:
  -  the [Anaconda package](https://www.anaconda.com/products/distribution), which comes with everything we need for the class;
  -   [Python](https://www.python.org/downloads/); 
  -   an IDE (Integrated Development Environment), which is where you will write your code. We recommend [VSCode](https://code.visualstudio.com/Download).  
  
- The easiest option for running Python codes is in the _cloud_, using Google Colab, which is a free service. Just click on the "Google Colab" icon next to an assignment to open it in Google Colab (you can also go to the [Google Colab homepage](https://colab.research.google.com/) and import a notebook from your computer or with an url. 


## Level 1 - Algorithms
The word _algorithm_ might seem a bit scary if you are new to coding, but in reality it's just a set of instructions. In this first part of the bootcamp we will work on building some intuition of how Python and algorithms work. 

**Karel the Robot** is a simple virtual robot created by Richard E. Pattis in 1981, designed to teach fundamental programming concepts.  

![Karel World](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcompedu.stanford.edu%2Fkarel-reader%2Fdocs%2Fimages%2Fch1%2Fworld.png&f=1&nofb=1&ipt=a96c726da6bc255557da4be0c6e10b348dcc8c5ad52a2222129f9ddd1f292365 "Karel World")

- **World**  
  A 2D grid of “streets” (rows) and “avenues” (columns), with optional walls and beepers (the diamond shaped objects) placed at grid intersections.  
- **Commands**  
  Karel only has 4 commands, and in the various exercises you will learn how to use them to get it to do complex things.   

  - `move()` – advance one cell forward  
  - `turn_left()` – rotate 90° counter-clockwise  
  - `pick_beeper()` / `put_beeper()` – interact with beepers  


> In this part you will learn how write small programs that navigate Karel through mazes, manipulate beepers, and solve well-defined puzzles.  Head over to 
[Karel reader](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter1.html) to learn more about Karel and prepare for the first lab, and then <a href="https://github.com/shepai/BIORTC_Nigeria/blob/main/BOOTCAMP/Level%201%20-%20Algorithms/Lab_day1.ipynb">Click here to see the challenge</a>! :)



## Level 2 - Python Coding

#### Task a - Maths through programming
Programming and maths are intertwined. Look at how we can do basic operations with Python

[![maths](https://img.youtube.com/vi/GTaE5NSzItw/0.jpg)](https://www.youtube.com/watch?v=GTaE5NSzItw)

[![maths2](https://img.youtube.com/vi/_XvHuiKWipE/0.jpg)](https://www.youtube.com/watch?v=_XvHuiKWipE)

[![maths3](https://img.youtube.com/vi/0uBWvzF91i8/0.jpg)](https://www.youtube.com/watch?v=0uBWvzF91i8)

<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_1_maths_through_programming.ipynb">Click here to view worksheet</a>

#### Task b - Data types
Understanding your data is key to making a program that uses it. This worksheet teaches you how to make different variables for different data, and how this is used.

* recapping bools vs numbers
* int vs float
* strings 
* lists 
* dictionaries
  
[![datatypes](https://img.youtube.com/vi/nsVPueieqzY/0.jpg)](https://www.youtube.com/watch?v=nsVPueieqzY) 

[![datatypes2](https://img.youtube.com/vi/EQppV-ffrZw/0.jpg)](https://www.youtube.com/watch?v=EQppV-ffrZw) 

[![refval](https://img.youtube.com/vi/mArBkIrCDdM/0.jpg)](https://www.youtube.com/watch?v=mArBkIrCDdM) 

<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_1_data_types.ipynb">Click here to view worksheet</a>

#### Task c - statements/expressions/logic
Computers use logic, 1 for on or 0 for off. Binary, at the simplest level, is a computers language. This still holds true in coding. We have True (1) and False (0) when making choices. 

[![Expressions](https://img.youtube.com/vi/leysSDiLLSs/0.jpg)](https://www.youtube.com/watch?v=leysSDiLLSs)

<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_2_logic_expressions.ipynb">Click here to view worksheet</a>

#### Task d - Flow of control

* introducing scope
* loop/iterator variables
  
[![flow1](https://img.youtube.com/vi/eUvVqedh838/0.jpg)](https://www.youtube.com/watch?v=eUvVqedh838)

[![flow2](https://img.youtube.com/vi/gj60K2j23YI/0.jpg)](https://www.youtube.com/watch?v=gj60K2j23YI)

[![Scope](https://img.youtube.com/vi/GIKhBCIH5wY/0.jpg)](https://www.youtube.com/watch?v=GIKhBCIH5wY) 

<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_2_flow_of_control.ipynb">Click here to view worksheet</a>

#### Task e - Functions
What if we want to execute the same bit of code multiple times throughout different parts of our program. Copying and pasting it will look messy, instead we can write it once as a function and recall it whenever we need it.
* simple functions
* parameters
* return values
* default parameters

[![functions1](https://img.youtube.com/vi/RaS9R50k--c/0.jpg)](https://www.youtube.com/watch?v=RaS9R50k--c)

[![functions2](https://img.youtube.com/vi/JQ5rdpqKpos/0.jpg)](https://www.youtube.com/watch?v=JQ5rdpqKpos)

<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_2_functions.ipynb">Click here to view worksheet</a>

#### Task f - Understanding Errors & The Call Stack
What does an error actually mean? The way that we can understand when our code breaks is understanding the error itself!
* syntax error
* overflow/timeout error
* logic error
* try catch


<a href="https://github.com/SussexPAL/PythonCrashCourse/blob/main/Worksheets/day_2_understanding_errors.ipynb">Click here to view worksheet</a>



## Level 3 - Data Science

Being able to import and preprocess various types of data forms the foundation for all the modeling and analysis we will do later. In this last part of the Bootcamp, we will learn how to handle data in python code with _numpy_, inspect and load it with _pandas_, and visualise it with _matplotlib_. This will give you all the nessesary tools for working with your own datasets in your projects.

#### Task a - Handling of your data with Numpy
First, we will learn how to use the library _numpy_ to handle and understand scientific data in python.

<a href="Level 3 - Data Science/3a_numpy.ipynb">Click here to view worksheet</a>

#### Task b - Using Pandas to load and inspect datasets
Next, we will learn how to load in different types of data, inspect it to understand the basic needed preprocessing steps, and then do the preprocessing. For this, we will use the _pandas_ library.

<a href="Level 3 - Data Science/3b_pandas.ipynb">Click here to view worksheet</a>

#### Task c - Using Matplotlib ot visualise your data
Last, we learn how to visualise that loaded data with _Matplotlib_, another very useful important library:

<a href="Level 3 - Data Science/3c_datasets.ipynb">Click here to view worksheet</a>
#### Task c - Application of this to real-world datasets
- tasks with different types of actually relevent datasets to the projects(look into spreadsheet)
- load in these datasets, gather images, simple data visualisation?

## Next steps
 If you feel comfortable with Python already and would like to do some extra reading on data analysis for neuroscience in preparation for the course, take a look at the interesting stuff on this page <a href="https://github.com/wimmerlab/MBC_data_analysis/tree/main">tutorial on Python for neuroscience</a>
