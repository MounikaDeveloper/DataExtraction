import re
frame=[]
source=[]
destination=[]
type=[]
z=[]
with open(r"C:/Users/xxx/Desktop/dataextraction/wireshark") as openfile:
    for line in openfile:
        x=line.strip().split('/n')
        if 'Frame' in line:
            for f in re.findall('Frame\s\d{1}',line):
                frame.append(f)
        if 'Source' in line:
            for s in re.findall('(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', line):
               source.append(s)
        if 'Destination' in line:
            for d in re.findall('(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', line):
                destination.append(d)
        if 'Type' in line:
            for t in re.findall('(\w{6})', line):
                type.append(t)

for x in range(0,7):
    print(frame[x]+',',"Src:"+source[x]+",","Des:",destination[x]+",","Type:"+type[x])