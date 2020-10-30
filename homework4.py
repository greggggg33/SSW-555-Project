#Guowei Li
def printGED(text_file):
    f = open(text_file+'.txt',"r")
    for lines in f:
        temp = lines.split(" ",2)
        temp[-1] = temp[-1][:-1]
        print ("--> " + lines, end ='')
        if temp[1] in ("NOTE","NAME","SEX","FAMC","FAMS","HUSB","WIFE","CHIL","DATE"):
            print ("<-- {}|{}|Y|{}".format(temp[0],temp[1],temp[2]))
        elif temp[1] in ("BIRT","DEAT","MARR","DIV"):
            print ("<-- {}|{}|Y".format(temp[0],temp[1]))
        elif temp[2] in ("INDI","FAM"):
            print ("<-- {}|{}|Y|{}".format(temp[0],temp[2],temp[1]))
        else:
            print ("<-- {}|{}|N|{}".format(temp[0],temp[1],temp[2]))
    return None

def searchByYears(text_file, startYear, endYear):
    "The method shows how many people was born between the startyear and endyear"
    f = open(text_file+".txt",'r')
    result = 0
    for lines in f:
        temp = lines.split(" ")
        temp[-1] = temp[-1][:-1]
        if temp[1] == "DATE":
            if int(temp[4]) >= startYear and int(temp[4]) <= endYear:
                print("I have fund someone was born {} {} {}".format(temp[2],temp[3],temp[4]))
                result += 1
    print("there are {} people was borned from {} to {}".format(result,startYear,endYear))
    return result

def getID(text_file): #return a dictionary that store everyone's name and their ID number in the GED#
    f = open(text_file+".txt",'r')
    lines = f.read().splitlines()
    result = {}
    c = 0 #counter to iterate the list
    while c < len(lines):
        temp = lines[c].split(" ")
        if temp[1].startswith("I"):
            result[lines[c+1].split(" ")[2]] = temp[1] #set the key as the name of the individual and value as its ID number
        c += 1
    print(result)
    return result

def main():
    printGED("test GEDCOM file")

if __name__ == "__main__":
    main()