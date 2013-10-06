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

try:
    ifile = open(filename, "r", newline = "")
except IOError:
    print("Uh oh, I don't see " + filename + "!")

reader = csv.reader(ifile)

cont = input("Is " + filename + " correct? type \"Y\" to continue... ")
if cont.lower() != "y":
    sys.exit(0)




rownum = 0

OA_columns = []
OA_count = 0

summative_column = 0
exam_column = 0

students = []

grade = {
"R-": 25, "-R": 25, "R": 35, "R+": 45, "+R": 45,
"1-": 52, "-1": 52, "1": 55, "1+": 58, "+1": 58,
"2-": 62, "-2": 62, "2": 65, "2+": 68, "+2": 68,
"3-": 72, "-3": 72, "3": 75, "3+": 78, "+3": 78,
"4--": 80, "4-": 85, "4": 90, "4+": 95, "4++": 100,
"--4": 80, "-4": 85, "+4": 95, "++4": 100,
"5": 100,
"A": 0
}

csv_contents = []

for row in reader:
    
    # Find which columns have headers of "O.A"
    if rownum == 0:
        cellnum = 0
        for cell in row:
            cell = cell.lower()
            if cell == "o.a" or cell == "oa" or cell == "o.a.":
                OA_columns.append(cellnum)
                OA_count += 1
            elif cell == "s":
                summative_column = cellnum
            elif cell == "e":
                exam_column = cellnum
            cellnum += 1
        row.append("Ave")
        row.append("Course Ave")

    # Calculate averages for each student using each "O.A" column
    else:
        average = 0
        for cellnum in OA_columns:
            average += grade[row[cellnum]]
        average /= OA_count
        row.append(average)
        
        summative = grade[row[summative_column]] * 0.1
        exam = grade[row[exam_column]] * 0.2
        ave = average * 0.7
        
        row.append(summative + exam + ave)

    csv_contents.append(row)
    rownum += 1

ifile.close()

open(filename, "w").close() #delete contents of file
ofile = open(filename, "w", newline = "")
writer = csv.writer(ofile)

for row in csv_contents:
    writer.writerow(row)

ofile.close()

print("Averages calculated!")
time.sleep(2)
