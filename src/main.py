import csv, sys, time

filename = "Book1.csv"

filename = input("Type in the filename of the .csv file you have placed next to this program: ")
while (filename[-3:]) != "csv":
    print("The file must be a .csv file")
    filename = input("Type in the filename of the .csv file you have placed next to this program: ")

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
    time.sleep(10)

cont = input("Is " + filename + " correct? type \"Y\" to continue... ")
if cont.lower() != "y":
    sys.exit(0)

try:
    ifile = open(filename, "r", newline = "")
except PermissionError:
    print("Uh oh, I don't have permission to open" + filename + "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)
except IOError:
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)
except:
    print("Uh oh, something went wrong while opening" + filename + "!")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)

reader = csv.reader(ifile)




rownum = 0

OA_columns = []
OA_count = 0

summative_column = 0
exam_column = 0
average_column = 0
found_header = False

students = []

grade = {
"R-": 25, "-R": 25, "R": 35, "R+": 45, "+R": 45,
"1-": 52, "-1": 52, "1": 55, "1+": 58, "+1": 58,
"2-": 62, "-2": 62, "2": 65, "2+": 68, "+2": 68,
"3-": 72, "-3": 72, "3": 75, "3+": 78, "+3": 78,
"4--": 80, "4-": 85, "4": 90, "4+": 95, "4++": 100,
"--4": 80, "-4": 85, "+4": 95, "++4": 100,
"5": 100
}

def put_record(row, cell, record):
    try:
        row[cell] = record
    except IndexError:
        row.insert(cell, record)

csv_contents = []

for row in reader:
    
    try:
        row[0]
    except IndexError:
        row = [""]
    
    # Find which columns have headers of "O.A"
    if row[0].lower() == "type":
        found_header = True
        cellnum = 0
        for cell in row:
            
            if cell.lower() == "o.a" or cell.lower() == "oa" or cell.lower() == "o.a.":
                OA_columns.append(cellnum)
                
            elif cell.lower() == "s":
                summative_column = cellnum
                    
            elif cell.lower() == "e":
                exam_column = cellnum
                average_column = cellnum + 1
                    
            cellnum += 1
        
        put_record(row, average_column, "Term Average")
        put_record(row, average_column+1, "Total Average")

    # Calculate averages for each student using each "O.A" column
    elif found_header:
        average = 0
        marks = 0
        for cellnum in OA_columns:
            if row[cellnum].lower() != "a":
                try:
                    average += grade[row[cellnum]]
                except KeyError:
                    print("I found something that didn't look like a mark in cell "
                          + str(cellnum) + " for student " + row[1] + " " + row[0])
                else:
                    marks += 1
        average /= marks
        put_record(row, average_column, average)
        
        summative = exam = 0
        
        if row[summative_column].lower() != "a" and row[exam_column].lower() != "a":
            try:
                summative = grade[row[summative_column]] * 0.1
            except KeyError:
                print("I found something that didn't look like a mark in an exam column.")
                summative = average * 0.1
                
            try:
                exam = grade[row[exam_column]] * 0.2
            except KeyError:
                print("I found something that didn't look like a mark in an exam column.")
                exam = average * 0.2
                
            average *= 0.7
        
        put_record(row, average_column+1, summative + exam + average)

    csv_contents.append(row)
    rownum += 1

ifile.close()

try:
    open(filename, "w").close() #delete contents of file
    ofile = open(filename, "w", newline = "")
except PermissionError:
    print("Uh oh, I don't have permission to open" + filename + "! Make sure nothing else is using that file.")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)
except IOError:
    print("Uh oh, I don't see " + filename + "!")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)
except:
    print("Uh oh, something went wrong while opening" + filename + "!")
    print("Nothing written to " + filename + ".")
    time.sleep(3)
    exit(1)

writer = csv.writer(ofile)

for row in csv_contents:
    writer.writerow(row)

ofile.close()

print("Averages calculated!")
time.sleep(2)
