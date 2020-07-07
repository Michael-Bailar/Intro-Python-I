"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
import platform
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
sysargs = sys.argv
sysSplit = sysargs[0].split("/")
print("**command line information**")
[print(i) for i in sysSplit]
print("**command complete - next operation**")

# Print out the OS platform you're using:
# YOUR CODE HERE
print("platform OS: " + platform.system() + " " + platform.release())

# Print out the version of Python you're using:
# YOUR CODE HERE
print ("python version: " + sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Process Id: ", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("working directory: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print ("login name: ", os.getlogin() )
