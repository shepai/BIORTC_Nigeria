# Python BOOTCAMP

This part of the repo provides worksheets and support videos to guide you through the basics in preperation for the computational neurosciene course. Much of this is taken from the <a href="https://github.com/SussexPAL/PythonCrashCourse">University of Sussex PAL resouces</a>. See <a href="https://github.com/SussexPAL/PythonCrashCourse">teh github</a> for more Python resources if you want to go further... We have taken the worksheets that are most related to this course's content. 

## Foundational skils (Setup)

 To run the code we have taken a snippet from a <a href="https://github.com/wimmerlab/MBC_data_analysis/tree/main">tutorial on Python for neuroscience)</a>. 
 There are two different options to run code: in the first one code will be run locally on your computer, while the second option uses cloud computing (so no installation of any software on your computer):
- If you will be using your own laptop at all times, you may want to install Python locally. The best option is to install the [Anaconda package](https://www.anaconda.com/products/distribution), which comes with everything we need for the class.
- The **preferred option** for running Python codes in the cloud is using Google Colab, which is a free service. Just click on the "Google Colab" icon next to an assignment to open it in Google Colab (you can also go to the [Google Colab homepage](https://colab.research.google.com/) and import a notebook from your computer or with an url.

## Level 1 - Algorithms


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

Being able to import and preprocess various types of data forms the foundation for all the modeling and analysis we will do later.

#### Task a - Handling of your data with Numpy
- numpy, arrays, accessing data

#### Task b - Unsing Pandas to load and inspect datasets
- pandas - dataframes to load in different types of data(csv,json,...)
- inspecing this data, simple statistics, what does that mean

#### Task c - Application of this to real-world datasets
- tasks with different types of actually relevent datasets to the projects(look into spreadsheet)
- load in these datasets, gather images, simple data visualisation?
