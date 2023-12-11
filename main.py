import getopt, sys, hashlib, time, multiprocessing, bcrypt, numpy as np

mode = ""
modePrint = ""
attack = ""
attackPrint = ""

dictFile = ""
dictPrint = ""


def setMode(modeSet):
    global mode, modePrint
    mode = modeSet
    modePrint = ("Mode : %s" % mode)
    

def setAttack(attackSet, file):
    global attack, dictFile, dictPrint, attackPrint
    attack = attackSet
    attackPrint = ("Method : %s" % attackSet)
    if(attack == "Dictionary"):
        dictFile = file
        dictPrint = ("Dictionary File : %s" % dictFile)

def checkMode(test):
    global mode
    if test == mode:
        return True
    else:
        return False

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[2:]

options = "pmsbd:la"

pw = sys.argv[1]
if pw in ['-p','-m','-s', '-b', '-d', '-l', '-a']:
    print("No Password Given To Crack!")
    quit()



try:
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
        
        elif currentArgument in ("-d"):
            #print ("Dictionary file Name: ", sys.argv[sys.argv.index("-d")+1])  
            setAttack("Dictionary", sys.argv[sys.argv.index("-d")+1])
        
count = 0

start_time = time.time()

t = multiprocessing.Process(target=loading)

if(attack == "Dictionary"):
    f = open(dictFile)
    
    t.start()
    for line in f:
        l = line.rstrip().encode('utf-8')

        if checkMode("MD5"):
            hashLine = hashlib.md5(l)
            check = hashLine.hexdigest()
        elif checkMode("SHA-256"):
            hashLine = hashlib.sha256(l)
            check = hashLine.hexdigest()
        elif checkMode("BCrypt"):
            hashline = bcrypt.gensalt()
            check = bcrypt.hashpw(bytes, salt)
        
        count = count + 1
        if(check == pw):
            t.terminate()
            print("--- Password is :",line.rstrip(),"---")
            quit()
print("\n")
print("Password Not Found in Dictionary")

if(attack == "Brute Force"):
    N = 100000
    A=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*~?")
    password_len=int(pw.len())
    for i in range(N):
        password="".join(np.random.choice(A, password_len).tolist())
    if checkMode("MD5"):
        hashLine = hashlib.md5(l)
        check = hashLine.hexdigest()
    elif checkMode("SHA-256"):
        hashLine = hashlib.sha256(l)
        check = hashLine.hexdigest()
    elif checkMode("BCrypt"):
        hashline = bcrypt.gensalt()
        check = bcrypt.hashpw(bytes, salt)    
    if(check == pw):
            t.terminate()
            print("--- Password is :",line.rstrip(),"---")
            quit()
    
t.terminate()
print("\n")
print("Password Not Found in Brute Force")
