# Don't make your file name as per any module name of python because when you import any module it follows the herechy technique to find that module file

from ctypes.wintypes import PINT
import sys
print(sys.path)

# By this you can import your own local files and their functions and variables which are frequently used in programs

from time_module import inital
print(inital)