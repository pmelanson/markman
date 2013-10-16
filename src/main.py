"""
Program created by Patrick Melanson, 2013
Contact: patrick.melanstone@gmail.com
Licensed under the MIT license. See accompanying LICENSE.txt file
"""
import csv
from time import sleep


filename = input("Type in the filename of the .csv file you have placed \
next to this program: ")
while (filename[-3:]) != "csv":
    print("The file must be a .csv file")
    filename = input("Type in the filename of the .csv file you have placed \
next to this program: ")

if filename.casefold() == "harriz.csv":
    print("""
    CCCGGCCCGG@@@@@@LGLGGGCCGG@@@G@@@GGCCCCLLLLLLLLC
    GCGCGCCCG@@@@@@@@@GGG@@@@@@@G@@@@@GCCLLCLCLCLLCC
    CCGCCGCL@@@@@@@@@GCLLCG@@@@@@@@@@@@CCfCfCLCCLLLC
    CCCCCCL@C@@@@@@GLtliiltCG@@@@GGGG@@G@CCLLLLLCfLC
    CCGCCCL@@@@@@@fti;;;;::lLCCCLffllfCG@CLLLLfCCCCC
    CLCCCL@@@@@@GLtii;;;:::::iliii:::lfG@@LffLLCCGGC
    CLCCCG@@@@@Gfflii;;;::::,,::,,,,,,:tCGGLfCCLLCLL
    CLCCL@@@@@@Cftli;;;::,,,,,,,,,,,,,::lCGCLLCCGCLC
    CCCLG@@@@@GCflli;;;::,,,,,,..,,,,,,::fGGLLCGLCLC
    CLCC@@@@@@@Cftli;;:::,,,,,..,..,,,,,:;fGCLLLCfCL
    CCCC@@@@@@GCftli;;;::,,,,,.......,,,:;lGGCLCLLLL
    CCLC@@@@@@@CLtli;;;;::,,,,......,,,,::lCGLLLfLLL
    CLCG@@@@@@@Lftl;;;;;:,,,,....,,,,,,,,:lGGLffLLfL
    CfLG@@@@@@GLftlltll;:,,,......,,,,,,::lGGLLfLLLf
    fCLG@@@@@@LLffLCCCCLLfi,......,,,,::::iGGCCLLCLf
    ffC@@@@@@CLLLCLfiilfttl:......,lfftt;:iCGLfCLLff
    ftl@@@@@CLLLCfl;:,,,:;;,.....,itLLLffiiGGfCfLfLL
    tLtC@@@@LLfLftli::::,:;:,....,:::,.,;tiLGfLLLLLL
    ffftL@@CLfftftlLfCC:;;:l:. .,;;;::,,:iliGLLLLLLL
    fttif@@CftttffLGCGGft:;l;. .;iitCCti;;i;C:fLfCLf
    ttt;fG@LftilfLLflli::::t:,..,:i;CClCl:::C:;LLLCf
    tflilLGfftlilltl:::,,,il;,..,:::;iilf;::C,ifLLLL
    ffiiffGfftiii;::;;::,,il:,..,.::,,,:i:,:L,itLLLf
    ftiltLGfftli;:,,,,,,,:il:,..,...:::,,,,::,:fLfLf
    ffillLGfftl;::,,,,,,,:ii;:..,,.......,,:,,:LLfLf
    CLlttCGfLtli::,,,...,:;i;:..,,........,:,;tffLff
    fLtlfGGLffli;:,......;iii,,.,,.   ....,:,:ttffff
    LCfilCGLfftl;:,.....ii:li,..,,,.   ...,:.:ttffff
    LCtltLGLfftti:,....;l;:i;,..,,,.   ...,;:ifffffL
    LCfttLGffftli;,,..,ili;;;, .,,,,......,i,fLLLfft
    CLLftGGfftlll;:,,,,;;lffLt.,:,,,.....,:t.ffLCCft
    LLLLLGGfftli;;:,:;;;iltftiiLfl;,..,,,,:f,fLtLLff
    LLLLLGGLft;;:;,,ifLLLLCLt:ffLLff,,..,,::ifffffff
    LLLLLCGCfli:,:,:LCCfl;;,,,,,,:lLi....,;ttfLfLLLL
    LLLLLCLGLti:,:,,;tfffttiiillli,;:....,LffLLCLLLL
    tfLLLGLGGti:::,,:,;ttl:,,,,,;,.......:fLfLfLCLLf
    fLLLLCLCGCt;:::,i,:;;;;::,,:,...,...,tfffffLLLLt
    ffLLLLLLGGCf;;::;,,::;;;;i:,....,..,;fLfLfLLLCCt
    LfLLLCLLLGGCfi;;;:,:,:;;ti:....,:.,:LffffLLLLCLf
    fLLLfGLffCGCLfftt;;,,,,,:,.....,;,;LLLLttffLCLLt
    tLLlCGLfffLGCLCfLfi;,.,,:,....,;itLCLLfftfLLLCCf
    LLLtGGLffffCCGCCCCfliii::;;,ifLLfLCLLLLLLLCCLLCf
    LLffGGLfttffLCGGCCLLftl;;liiflLCLLLLLLLLLLLCCCCf
    """)
    sleep(10)
    exit(3141)

cont = input("Is " + filename + " correct? type \"Y\" to continue... ")
if cont.casefold() != "y":
    print("Input was not \"Y\", exiting...")
    sleep(3)
    exit(1)

try:
    ifile = open(filename, "r", newline = "")
except PermissionError:
    print("Uh oh, I don't have permission to open" + filename +
          "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)
except IOError:
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)
except:
    print("Uh oh, something went wrong while opening" + filename + "!")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)

reader = csv.reader(ifile)

grade = {
    "r-": 25, "-r": 25, "r": 35, "r+": 45, "+r": 45,
    "1-": 52, "-1": 52, "1": 55, "1+": 58, "+1": 58,
    "2-": 62, "-2": 62, "2": 65, "2+": 68, "+2": 68,
    "3-": 72, "-3": 72, "3": 75, "3+": 78, "+3": 78,
    "4--": 80, "4-": 85, "4": 90, "4+": 95, "4++": 100,
    "--4": 80, "-4": 85, "+4": 95, "++4": 100,
    "5": 100
}

class MarkMan():
    
    def __init__(self, header_string):
        self.header_string = header_string.casefold().strip()
    
    headers = {}
    marks = {}
    
    def find_headers(self, row):
        """
        Builds an index of the column number of each relevant header,\
        and which unit it corresponds to
        """
        self.headers = {}
        i = 0
        for cell in row:
            cell = cell.casefold()
            if cell.startswith(self.header_string):
                key = cell.strip().strip(self.header_string)
                if key.isdigit() == False:
                    print("The header \"" + cell + "\" contains \""
                          + self.header_string + "\" and \"" + key
                          + "\" where \"" + key + "\" is not a number, \
                          skipping this header...")
                else:
                    self.headers[key] = i
            i += 1
    
    
    def find_marks(self, row):
        """
        Method 'find_headers' must have been run prior to calling this
        """
        self.marks = {}
        for key in self.headers:
            self.marks[key] = row[self.headers[key]].casefold()
    
    
    def average(self):
        """
        Method 'find_marks' must have been run prior to calling this
        """
        ave = n = 0
        for mark in self.marks.values():
            if mark != "a" and mark != "":
                try:
                    ave += grade[mark]
                    n += 1
                except KeyError:
                    print("I found the mark " + mark +
                          ", which I don't understand, skipping that mark.")
        try:
            ave /= n
        except ZeroDivisionError:
            return None
        
        return round(ave, 2)


course = MarkMan("O.A")
summative = MarkMan("S")
exam = MarkMan("E")

found_header = False

csv_contents = []


"""
                        This is where the magic happens:
"""

print("Calculating Averages")

for row in reader:
    
    """
    If a row is completely empty, replace it with
    a row of empty cells
    """
    try:
        row[0]
    except IndexError:
        row = [""]
    
    
    if found_header:
        """
        This block is triggered for every row (which should
        contain a student), but only once the header has been
        found
        """
        course.find_marks(row)
        summative.find_marks(row)
        exam.find_marks(row)
        
        row.append(course.average())
        
        """
        If the exam mark for a strand is greater than the course mark,
        overwrite the course mark with the exam mark
        """
        for key in exam.marks.keys():
            try:
                if grade[exam.marks[key]] > grade[course.marks[key]]:
                    course.marks[key] = exam.marks[key]
            except KeyError:
                break
        
        if summative.average() != None and exam.average() != None:
            row.append(course.average()*0.7 +
                       summative.average()*0.1 +
                       exam.average()*0.2)
    
    elif row[0].casefold().strip() == "type":
        """
        This block is triggered by the header row, identified by the first cell
        being "Type", case-insensitive and whitespace padding-insensitive
        """
        found_header = True
        
        course.find_headers(row)
        summative.find_headers(row)
        exam.find_headers(row)
        
        row.append("Term Average")
        row.append("Total Average")
        
    csv_contents.append(row)

ifile.close()


"""
Write contents to file
"""
if found_header == False:
    print("Uh oh, I couldn't find the header in " + filename + "!")
    print("Make sure the .csv file is comma-delimited, not tab-delimited")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)

try:
    open(filename, "w").close() # Delete contents of file
    ofile = open(filename, "w", newline = "")
except PermissionError:
    print("Uh oh, I don't have permission to open" + filename
          + "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)
except IOError:
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)
except:
    print("Uh oh, something went wrong while opening" + filename + "!")
    print("Nothing written to " + filename + ".")
    sleep(4)
    exit(1)

writer = csv.writer(ofile)

for row in csv_contents:
    writer.writerow(row)

ofile.close()

print("Averages calculated!")
sleep(3)
