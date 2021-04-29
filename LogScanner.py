f = open("logfile.txt", "r")
fError = open("error.txt", "w")
fWarning = open("warning.txt", "w")
lines = f.readlines()

def listToString(s): 
    str1 = " " 
    return (str1.join(s))

for line in lines:
    timestamp = line.split()[0][1:-1]
    messageType = line.split()[1][:-1]
    message = listToString(line.split()[2:])
    if(messageType == "Error"):
        fError.write(timestamp + ": " + message+"\n")
    else:
        fWarning.write(timestamp + ": " + message+"\n")



        