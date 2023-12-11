import getopt, sys, hashlib, time, multiprocessing, bcrypt, numpy as np

mode = ""
modePrint = ""
attack = ""
attackPrint = ""
dictFile = ""
dictPrint = ""

#determines the hashe that is checked
def setMode(modeSet):
    global mode, modePrint
    mode = modeSet
    modePrint = ("Mode : %s" % mode)
    
#determines the method of password cracking
def setAttack(attackSet, file):
    global attack, dictFile, dictPrint, attackPrint
    attack = attackSet
    attackPrint = ("Method : %s" % attackSet)
    if(attack == "Dictionary"):
        dictFile = file
        dictPrint = ("Dictionary File : %s" % dictFile)
#calls the method of password cracking
def checkMode(test):
    global mode
    if test == mode:
        return True
    else:
        return False

def loading():
    global notcomplete

    i = 0
    while True:
        time.sleep(0.1)
        sys.stdout.flush()
        i += 1

    print("\n")

def bruteForceCheck(password_len=4):
    N = 100000
    A=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*~?")
    for i in range(N):
        l ="".join(np.random.choice(A, password_len).tolist()).encode('utf-8')

    if checkMode("MD5"):
        hashLine = hashlib.md5(l)
        check = hashLine.hexdigest()
    elif checkMode("SHA-256"):
        hashLine = hashlib.sha256(l)
        check = hashLine.hexdigest()
    elif checkMode("BCrypt"):
        salt = bcrypt.gensalt()
        check = bcrypt.hashpw(l, salt) 
        print(check)
    if(check == pw):
            print("--- Password is :",line.rstrip(),"---")
            quit()
    print("\n")
    print("Password Not Found in Brute Force")

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[2:]

options = "msbd:c"

pw = sys.argv[1]
if pw in ['-m','-s', '-b', '-d', '-c']:
    print("No Password Given To Crack!")
    quit()


# Parsing argument
arguments, values = getopt.getopt(argumentList, options)
 
# checking each argument
for currentArgument, currentValue in arguments:
 
         
    if currentArgument in ("-m"):
        setMode("MD5")
         
    elif currentArgument in ("-s"):
        setMode("SHA-256")
    
    elif currentArgument in ("-c"):
        setMode("BCrypt")
        
    elif currentArgument in ("-b"):
        setAttack("Brute Force", "")
        bruteForceCheck()
        quit()
    
    elif currentArgument in ("-d"):
        #print ("Dictionary file Name: ", sys.argv[sys.argv.index("-d")+1])  
        setAttack("Dictionary", sys.argv[sys.argv.index("-d")+1])
       
if(attack == "Dictionary"):
    f = open(dictFile)
    
    for line in f:
        l = line.rstrip().encode('utf-8')

        if checkMode("MD5"):
            hashLine = hashlib.md5(l)
            check = hashLine.hexdigest()
        elif checkMode("SHA-256"):
            hashLine = hashlib.sha256(l)
            check = hashLine.hexdigest()
        elif checkMode("BCrypt"):
            salt = bcrypt.gensalt()
            check = bcrypt.hashpw(l, salt)
        
        if(check == pw):
            print("--- Password is :",line.rstrip(),"---")
            quit()
print("\n")
print("Password Not Found in Dictionary")

