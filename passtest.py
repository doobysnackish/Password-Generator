import random;
import os;
import datetime;
import re;

#special characters
vowels = ['a','e','i','o','u'];

def returnSpec():
    spec = ['/','@','#','&','*','^','%','(','}',')','{'];
    return spec[random.randrange(0,11)];

def returnNums():
    return str(random.randrange(1,3000));
#to do list
#add an if to remove illegal characters from randrange

def returnChars():
    return chr(random.randrange(33,125));

def preAmble():
    i = 0;
    pre = "";
    while i < 6:
        #pre+=returnSpec()+returnChars();
        if((random.randrange(0,1))==1):
            pre+=returnSpec();
        else:
            pre +=returnChars();
        i+=1;
    return pre;

def autoGen(size):
    i = 0;
    build = '';
    while i < size:
        build+=preAmble();
        i+=1;
    return build;

def fileStuff():
    cwd = os.getcwd();
    x = "PassList"+str(datetime.datetime.now());
    x.strip();
    x.replace(" ","");
    x = re.sub('[.:-]\s','',x);
    x = re.sub(' ','',x);
    x.strip();
    blah = x[:-13];
    print(x);
    print(blah);
    i = 0;
    f = open(blah,'a+');
    size=1;

    while i <= 30:
        stuff = "Password: " + autoGen(size) + "\n";
        f.write(stuff);
        if i == 10:
            f.write("*"*30);
            f.write("\Longer Passwords\n");
            size = 2;
        if i == 20:
            f.write("*"*30);
            f.write("\Even Longer Passwords\n");
            size = 3;
        i+=1;

    f.close()
    exit()



#print(''.join(blah)+addit+vo+specplus);
#print(returnNums()+returnSpec()+returnChars());
#print(preAmble()+''.join(blah)+preAmble());

print('*'*30);

#while i <= 5:
#    print(autoGen(2));
#    i+=1;
print(os.getcwd());
fileStuff();
print(autoGen(1));
print(autoGen(2));

#for line in f:
#    print(f.readline())
