"""
Program created by Patrick Melanson, 2013
Contact: patrick.melanstone@gmail.com
Licensed under the MIT license. See accompanying LICENSE.txt file
"""
import csv
from time import sleep


filename = input("Type filename of .csv file you placed with this program: ")
while (filename[-3:]) != "csv":
    print("The file must be a .csv file")
    filename= input("Type filename of .csv file you placed with this program: ")

if filename.lower() == "harriz.csv":
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
if cont.lower() != "y":
    print("Input was not \"Y\", exiting...")
    input("Press enter to continue...")
    exit(1)

try:
    ifile = open(filename, "r", newline = "")
except PermissionError:     # Triggers on a permissions error, usually when
                            # the file is open in another program
    print("Uh oh, I don't have permission to open" + filename +
          "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)
except IOError:             # Triggers on a read error
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)
except:                     # Triggers on any other error
    print("Uh oh, something went wrong while opening" + filename + "!")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)


delim_count = {";": 0, ",": 0, "\t": 0}

for line in ifile.readlines():
    for delimiter in delim_count.keys():
        delim_count[delimiter] += line.count(delimiter)

delim = ";"

for delimiter in delim_count:
    if delim_count[delim] < delim_count[delimiter]:
            delim = delimiter

print("It looks like " + delim + " is the delimiter, with " +
      str(delim_count[delim]) + " occurences")

reader = csv.reader(ifile, delimiter=delim)  # A class that contains functions to read the file

ifile.seek(0)   # Return read cursor to beginning of file




grade = {   # A python "dict"
    "r-": 25, "-r": 25, "r": 35, "r+": 45, "+r": 45,
    "1-": 52, "-1": 52, "1": 55, "1+": 58, "+1": 58,
    "2-": 62, "-2": 62, "2": 65, "2+": 68, "+2": 68,
    "3-": 72, "-3": 72, "3": 75, "3+": 78, "+3": 78,
    "4--": 80, "4-": 85, "4": 90, "4+": 95, "4++": 100,
    "--4": 80, "-4": 85, "+4": 95, "++4": 100,
    "5": 100
}

#===============================================================================
# In python, a "dict" is an array of key/value pairs, where the key is a string
# 
# e.g.:
# 
# grade["4--"] == 80    # True
# 
# grade["--4"] == 80    # True
#===============================================================================

class MarkMan():
    
    def __init__(self, header_string):
        self.header_string = header_string.lower().strip()
    
    headers = {}
    #===========================================================================
    # self.headers is a dict where the key is a unit number and the value is
    # the index at which that unit's column is found. See self.find_headers.
    #===========================================================================
    
    marks = {}
    #===========================================================================
    # self.marks is a dict that stores the mark in each unit for a student.
    # e.g.
    # self.marks = {["1", 4+], ["2", 3]}
    # means the student got a 4+ in unit 1 and a 3 in unit 2
    #===========================================================================
    
    def find_headers(self, row):
        """
        When passed the header row, finds the columns that correspond
        to self.header_string and then stores the index of each unit
        ["Type", "S1", "O.A1", "E1", "O.A2"]
        and self.header_string == "O.A"
        self.headers will become
        {["1": 2], ["2": 4]}
        since O.A, unit 1, is in row[2] and O.A, unit 2, is in row[4].
        """
        self.headers = {}
        i = 0
        for cell in row:
            cell = cell.lower()
            if cell.startswith(self.header_string) and\
               cell != "summative mark" and\
               cell != "exam mark":
                unit = cell.strip().strip(self.header_string)
                if unit.isdigit() == False:
                    print("The header \"" + cell + "\" contains \""
                          + self.header_string + "\" and \"" + unit
                          + "\" where \"" + unit + "\" is not a number, \
                          skipping this header...")
                else:
                    self.headers[unit] = i
            i += 1
    
    def find_marks(self, row):
        """self.find_headers must have been run prior to calling this."""
        self.marks = {}
        for unit in self.headers:
            self.marks[unit] = row[self.headers[unit]].lower()
    
    
    def average(self):
        """
        self.find_marks must have been run prior to calling this.
        Returns the average of of all the marks in self.marks.
        Returns None if there are no marks in self.marks
        """
        ave = n = 0
        for mark in self.marks.values():
            if mark != "a" and mark != "":
                try:
                    ave += grade[mark]
                    n += 1
                except KeyError:
                    print("I found the mark " + mark + " under category " +
                          self.header_string +
                          ", which I don't understand, skipping that mark.")
        try:
            ave /= n
        except ZeroDivisionError:
            return None
        
        return ave


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
        
        if course.average() != None:
            row.append(round(course.average(), 2))
        else:
            row.append("")
        if summative.average() != None:
            row.append(round(summative.average(), 2))
        else:
            row.append("")
        if exam.average() != None:
            row.append(round(exam.average(), 2))
        else:
            row.append("")
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
        
        if summative.average() != None and\
           exam.average() != None and\
           course.average() != None:
            row.append(round(
                             course.average()*0.7 +
                             summative.average()*0.1 +
                             exam.average()*0.2,
                             2))
        elif summative.average() != None and\
             course.average() != None:
            row.append(round(
                             course.average()*0.7 +
                             summative.average()*0.3,
                             2))
        elif course.average() != None:
            row.append(round(
                             course.average(),
                             2))
    
    elif row[0].lower().strip() == "type":
        """
        This block is triggered by the header row, identified by the first cell
        being "Type", case-insensitive and whitespace padding-insensitive
        """
        found_header = True
        
        course.find_headers(row)
        summative.find_headers(row)
        exam.find_headers(row)
        
        row.append("Term Mark")
        row.append("Summative Mark")
        row.append("Exam Mark")
        row.append("Final Mark")
        
    csv_contents.append(row)

ifile.close()


"""
Write contents to file
"""
if found_header == False:
    print("Uh oh, I couldn't find the header in " + filename + "!")
    print("Make sure the .csv file is delimited consistently")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)

try:
    open(filename, "w").close() # Delete contents of file
    ofile = open(filename, "w", newline = "")
except PermissionError:
    print("Uh oh, I don't have permission to open " + filename
          + "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)
except IOError:
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)
except:
    print("Uh oh, something went wrong while opening " + filename + "!")
    print("Nothing written to " + filename + ".")
    input("Press enter to continue...")
    exit(1)

writer = csv.writer(ofile)

for row in csv_contents:
    writer.writerow(row)

ofile.close()

print("Averages calculated!")
input("Press enter to exit...")
