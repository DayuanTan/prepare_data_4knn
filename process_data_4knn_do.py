import os

resultHandler = open('results.csv','w')

path = "individual_stocks_5yr"
files = os.listdir(path)
print(files)
files.sort()
files.remove(".DS_Store")
print(files)

for file in files:
    if not os.path.isdir(file):         # only open if it's directory
        f = open(path + "/" + file)     # open this file
        iter_f = iter(f)                # create iterator

        counter = 0
        openChangesArray = list()
        highChangesArray = list()
        lowChangesArray = list()
        closeChangesArray = list()
        volumeChangesArray = list()
        lastline = 'Hello,This is virtual empty line.'
        for line in iter_f:             # traverse the file line by line
            line = line.rstrip()
            #print(line)
            thisline = line.split(',')
            #print(thisline[1]," ",lastline[1])
            try:
                openChanges = round(float(thisline[1]) - float(lastline[1]),2)
                highChanges = round(float(thisline[2]) - float(lastline[2]), 2)
                lowChanges = round(float(thisline[3]) - float(lastline[3]), 2)
                closeChanges = round(float(thisline[4]) - float(lastline[4]), 2)
                volumnChanges = int(thisline[5]) - int(lastline[5])
                counter = counter + 1
                if counter <= 9:
                    openChangesArray.append(openChanges)
                    highChangesArray.append(highChanges)
                    lowChangesArray.append(lowChanges)
                    closeChangesArray.append(closeChanges)
                    volumeChangesArray.append(volumnChanges)
                else:
                    openChangesStr = str(openChangesArray)
                    openChangesStr = openChangesStr.lstrip('[')
                    openChangesStr = openChangesStr.rstrip(']')
                    highChangesStr = str(highChangesArray)
                    highChangesStr = highChangesStr.lstrip('[')
                    highChangesStr = highChangesStr.rstrip(']')
                    lowChangesStr = str(lowChangesArray)
                    lowChangesStr = lowChangesStr.lstrip('[')
                    lowChangesStr = lowChangesStr.rstrip(']')
                    closeChangesStr = str(closeChangesArray)
                    closeChangesStr = closeChangesStr.lstrip('[')
                    closeChangesStr = closeChangesStr.rstrip(']')
                    volumeChangesStr = str(volumeChangesArray)
                    volumeChangesStr = volumeChangesStr.lstrip('[')
                    volumeChangesStr = volumeChangesStr.rstrip(']')

                    resultHandler.writelines([openChangesStr,';',highChangesStr,';',lowChangesStr,';',closeChangesStr,';',volumeChangesStr,';',thisline[6],'\n'])
                    openChangesArray = list()
                    highChangesArray = list()
                    lowChangesArray = list()
                    closeChangesArray = list()
                    volumeChangesArray = list()
                    counter = 0
                #print(counter," ",openChangesArray)
                ##print(changesArray)
            except:
                print("Can't do divison.")
            finally:
                lastline = thisline

            #print(openChangesArray)




