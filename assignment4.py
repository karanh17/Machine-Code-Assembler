import re


f = open("output.txt","w+")
loop_start = 0
gotolinenum = 0
loopstr = " "
exitline = 0


print("input a file to open.")
userinput   = input()
file = open(userinput,"r")     

def printout(strg):
    global f   
    f.write(strg)

#def Convertercondtion(B, goto):

def findexit(goto):
   global loop_start
   global gotoline
   global loopstr
   global exitline

   with open(userinput,"r") as files:
       for i in files:
           if i == goto + ":":
              return
           else:
              exitline = exitline + 1

    

def Converterloop(loop, funct, dest, inpu1, inpu2):   
        global loopstr

        if dest == "XZR,":
                dest = "31"
        elif inpu1 == "XZR,":
                inpu1 = "31"
        elif inpu2 == "XZR":
                inpu2 = "31"  

        if dest == "XZR,":
                dest = "31"
        elif inpu1 == "XZR,":
                inpu1 = "31"
        elif inpu2 == "XZR":
                inpu2 = "31"    
        
        if dest == "XZR,":
                dest = "31"
        elif inpu1 == "XZR,":
                inpu1 = "31"
        elif inpu2 == "XZR":
                inpu2 = "31"

        
        loopstr = loop
        
        ConverterDEF(funct,dest,inpu1,inpu2)
        #strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        #printout (strg)


def CBZconverter(funct,dest,inpu1):

    strg = funct + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n"
    printout(strg)

def ConverterDEF(funct, dest, inpu1, inpu2):
  
    
    
    #checks for xzr
    if dest == "XZR,":
        dest = "31"
    elif inpu1 == "XZR,":
        inpu1 = "31"
    elif inpu2 == "XZR":
        inpu2 = "31"

    if dest == "XZR,":
        dest = "31"
    elif inpu1 == "XZR,":
        inpu1 = "31"
    elif inpu2 == "XZR":
        inpu2 = "31"

    if dest == "XZR,":
        dest = "31"
    elif inpu1 == "XZR,":
        inpu1 = "31"
    elif inpu2 == "XZR":
        inpu2 = "31"


    if funct == "ADD":             
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "SUB" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "AND" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "ORR" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "EOR" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "LSL":
        strg = funct + " " + "0" + " " + re.sub("[^0-9]","",inpu2) + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "LSR" :
        strg = funct + " " + "0" + " " + re.sub("[^0-9]","",inpu2) + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "ADDI" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "SUBI" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2)  + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "ANDI":
         strg = funct + " " + re.sub("[^0-9]","",inpu2)  + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
         printout (strg)
    elif funct == "ORRI":
         strg = funct + " " + re.sub("[^0-9]","",inpu2)  + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
         printout (strg)
    elif funct == "EORI":
         strg = funct + " " + re.sub("[^0-9]","",inpu2)  + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
         printout (strg)
    elif funct == "SUBS":
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "SUBIS" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "LDUR" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)
    elif funct == "STUR" :
        strg = funct + " " + re.sub("[^0-9]","",inpu2) + " " +"0" + " " + re.sub("[^0-9]","", inpu1) + " " + re.sub("[^0-9]","", dest) + "\n" 
        printout (strg)


def ConverterGOTO(cond, goto):
    global loop_start
    global gotoline
    global loopstr
    global exitline

    if cond + " " + goto == "B " + goto  :
        gotoline = loop_start - gotoline  
        strg = "B " +" " + str(gotoline) + "\n"
        printout (strg)

    elif cond == "B.GE" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 10 \n" 
        printout (strg)

    elif cond == "B.EQ" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 0 \n" 
        printout (strg)

    elif cond == "B.NE" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 1 \n" 
        printout (strg)

    elif cond == "B.GT" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 12 \n" 
        printout (strg)

    elif cond == "B.GTE" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 12 \n" 
        printout (strg)

    elif cond == "B.LT" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 11 \n" 
        printout (strg)

    elif cond == "B.LTE" :
        findexit(goto)
        strg = cond +" " + str(exitline - gotoline - 1) + " 11 \n" 
        printout (strg)

    

def main ():
    global loop_start
    global gotoline
    

    
    # file_content = file.read()
    # opens output file
    lines = 0
       
    #counts lines in file 

    with open(userinput,"r") as files:
        for i in files:
            #print ("i = : ", i)
            test = i
            countsemi    = 0
            countdot     = 0
            countcomma   = 0
            countsemi    = test.count(":")
            countdot     = test.count(".")
            countcomma   = test.count(",")
            

    # Seperates everything into its own values

            if countsemi >= 1 :                
                 loop, funct, dest, inpu1, inpu2 = test.split()
                 #print (loop, funct, dest, inpu1, inpu2) 
                 loop_start = lines 
                 Converterloop(loop, funct, dest, inpu1, inpu2)              
            elif  countdot >=1:
                 cond, goto = test.split()
                 #print(cond, goto)
                 gotoline = lines
                 ConverterGOTO(cond, goto)
            elif countcomma >= 2:              
                 funct, dest, inpu1, inpu2 = test.split()
                 #print ( funct, dest, inpu1, inpu2)
                 ConverterDEF(funct, dest, inpu1, inpu2)
           
            elif countcomma >= 1: 
                 funct, dest, inpu1 = test.split()
                 CBZconverter(funct,dest,inpu1)
            else:
                 cond, goto = test.split()
                 #print(B, goto)
                 gotoline = lines   
                 ConverterGOTO(cond, goto)
                 
            lines = lines + 1    
    
    f.close


if __name__ == "__main__":
    main()