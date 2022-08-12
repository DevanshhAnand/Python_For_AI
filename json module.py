from calendar import day_abbr
import json
from traceback import print_tb

from numpy import rint
data = '{"var1":"harry","var2":"56"}'
print(data)

parsed = json.loads(data)#This will convert the given data into json compatible
print(parsed)

data2={
    "channel_name":"CodeWithHarry",
    "Cars":['bmw','audi'],
    "fridge":('roti',540),
    "isbad":False

}

jscomp=json.dumps(data2)#This will convert the given data into javascript compatible
print(jscomp)