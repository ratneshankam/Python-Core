print("Hello Python!");       # ';' works in python

# This is a Single and below is multi-line comment in python

# This is a command to display bytecode on terminal for python

"""
Command: python -m dis Start.py

  0           0 RESUME                   0
              2 LOAD_CONST               0 (None)
              4 RETURN_VALUE

"""

# To compile python and generate .pyc file [Under __Pycache__ folder ] use this command -->

# PS A:\Core2Web\C2W_Python> python -m py_compile Start.py

# PS A:\Core2Web\C2W_Python\__pycache__> python Start.cpython-311.pyc



# To check python version
import sys
print (sys.version)