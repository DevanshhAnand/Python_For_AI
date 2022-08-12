import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
+91 9408378640
+91 9188378640
+91 9408375440
+91 9408374140
+91 9408365640
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# strfunctions-findall,search,split,sub,finditer

# patt=re.compile(r'fass')
# patt=re.compile(r'.')
# patt=re.compile(r'.adm')
# patt=re.compile(r'.adm')
# patt=re.compile(r'^Tata')
# patt=re.compile(r'iin $')#This will show matches which ends with iin
# patt=re.compile(r'a*i{2}')
# patt=re.compile(r'(ai){2}')
# patt=re.compile(r'(ai)|t')

# patt = re.compile(r'\d{5}-\d{4}')
patt =  re.compile(r'.+91 \d{10}')

# listno=[]
# print(r"\n")#This is known as raw string
matches = patt.finditer(mystr)
for match in matches:
    # listno=[match]
    print(match)
# print(listno)


# Store numbers in list