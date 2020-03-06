import re

class Compiler:

    lib = {}
    lib_dir = "lib.cpp"
    # raw = ""
    raw_dir = "raw.cpp"
    out = ""
    out_dir = "out.cpp"
    enable_debug = False

    def __init__(self, mode = "", debug = False):
        self.enable_debug = debug
        self.mode = mode

    def fetchLibrary(self, loc = ""):
        if loc != "":
            self.lib_dir = loc
        with open(self.lib_dir,'r') as f :
            d = f.readlines()
            for i in d:
                data = i.rstrip("\n")
                data = re.sub(r'#define\s+', "", data, re.IGNORECASE)
                var = re.search(r'\S+',data)[0]
                ctx = re.sub(r'^\w+\s+',"",data)
                if re.match(r"(?<![\w\d\.\[\]$])[A-Za-z][\w$]*(\.[\w$]+)?(\[\d+])?(?![\w\d\.\[\]$])",var):
                    self.lib[ctx] = var  
                f.close()

    # def fetchRaw(self, loc = ""):
    #     if loc != "":
    #         self.raw_dir = loc

    def checkVar(self, name):
        if re.match(r"(?<![\w\d\.\[\]$])[A-Za-z][\w$]*(\.[\w$]+)?(\[\d+])?(?![\w\d\.\[\]$])",name):
            return True
        return False

    def output(self, loc = ""):
        if loc != "":
            self.out_dir = loc
        f = open(self.out_dir,'w+')
        f.write(self.out)
        f.close()

    def addDefinition(self):
        for i in self.lib.keys():
            self.out += "#define "+ self.lib[i] + " " + i + "\n\n"

    def compile_deprecated(self):
        f = open(self.raw_dir, 'r')
        fr = f.readlines()
        f.close()
        self.out = ""
        self.addDefinition()
        for x in fr:
            xr = x.split(' ')
            for i in xr:
                if self.checkVar(i):
                    if i in self.lib.keys():
                        self.out += self.lib[i]
                    else:
                        self.out += i
                elif i in self.lib.keys():
                    self.out += self.lib[i]
                else:
                    found = False
                    for j in i:
                        if j in self.lib.keys():
                            self.out += self.lib[j]
                            found = True
                    if not found:
                        self.out += i
                self.out+= " "

    def compile(self, loc = ""):
        if loc != "":
            self.raw_dir = loc
        f = open(self.raw_dir, 'r')
        fr = f.readlines()
        f.close()
        self.out = ""
        self.addDefinition()
        for x in fr:
            if re.match(r'#include',x, re.IGNORECASE) or re.match(r'#define',x, re.IGNORECASE):
                self.out = x + self.out
                continue
            self.convertLine(x)

    def convertLib(self, raw):
        if raw in self.lib.keys():
            return self.lib[raw]
        else:
            return raw

    def convertLine(self, line):
        word = ''
        collected = []
        quoted = False
        last_quote = ''
        for i in range(len(line)):
            if line[i] == " " and not quoted: #auto break when whitespace found
                collected.append(word)
                word = ''
                continue
            if line[i] == ";" and not quoted:
                word += " "+self.convertLib(';')
                collected.append(word)
                word = ''
                continue
            word+=line[i] #add new char reading
            if line[i] == "'" or line[i] == '"':
                if quoted and last_quote == line[i]: #close quote
                    if word[-2] == "\\":
                        continue 
                    quoted = False
                    last_quote = ''
                    if line[i] in self.lib.keys(): #if quote was defined
                        word = word[:-1]
                        word += self.lib[line[i]]
                    collected.append(word)
                    word = ''
                    continue
                elif last_quote == '' and not quoted: #open quote
                    last_quote = line[i]
                    quoted = True
            if word in self.lib.keys():
                collected.append(self.lib[word])
                word = ''
            elif i == len(line)-1:
                collected.append(word)
        self.out += ' '.join(collected) 
        if self.enable_debug:
            print(' '.join(collected), end = "")

