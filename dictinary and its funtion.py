# dictionary is nothing but key value pairs
d1={"harry":"burger","rohan":"fish","bhiku":"bhau",
    "shub":{"1":"elevated","2":"no love"}}
d1["ankit"]="junk food"
d1["aurang"]="kebbab"
print(d1)
print(d1["bhiku"])
del d1["aurang"]
print(d1)

d2  = d1.copy()
print(d2)
print(d1.values())
print(d1.keys())
print(d1.items())