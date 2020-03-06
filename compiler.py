import re

# File 'lib.txt' hanya berisi define
# File 'raw.cpp' hanya berisi kode dibawah define (define boleh dicantumkan tapi tidak boleh ada di file lib.txt)

lib = {}
with open('lib.txt','r') as f :
    d = f.readlines()
    for i in d:
        data = i.rstrip("\n")
        data = re.sub(r'#define\s+', "", data)
        var = re.search(r'\S+',data)[0]
        ctx = re.sub(r'^\w+\s+',"",data)
        if re.match(r"(?<![\w\d\.\[\]$])[A-Za-z][\w$]*(\.[\w$]+)?(\[\d+])?(?![\w\d\.\[\]$])",var):
          lib[ctx] = var  
        f.close()

f = open('raw.cpp', 'r')
fr = f.readlines()
f.close()
res = ""
for i in lib.keys():
    res += "#define "+ lib[i] + " " + i + "\n"
res += "\n"
for x in fr:
    xr = x.split(' ')
    for i in xr:
        if i in lib.keys():
            res += lib[i]
        else:
            res += i
        res+= " "

f = open('out.cpp','w+')
f.write(res)
f.close()
    