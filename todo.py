import sys,os
if len(sys.argv)==1:
    print("error insufficient args")
    sys.exit(1)


if len(sys.argv)>=1:
    filename=sys.argv[1]
    if not os.path.isfile(filename):
        with open(filename,'w') as f:
            f.write("written")
try:
    if sys.argv[2]=="-a":
        print(5*"*"+"appending into file"+5*"*")
        fl = open(filename,'a')
        fl.write("\n"+sys.argv[3])

    elif sys.argv[2]=="-v":
        fl = open(filename,'r')
        print("displaying contains\n\n")
        print(fl.read())
    elif sys.argv[2]=="-lines":
        fl=open(filename,'r')
        print("total line numbers")
        print(len(fl.readlines()))
    elif sys.argv[2]=="-h" or sys.argv[2]=="-help":
        fl=open("option.txt",'r')
        print(fl.read())
    elif sys.argv[2]=="-delete":
        fl=open(filename,'r+')
        xx=""
        cont=fl.read()
        xx=cont[:cont.find(sys.argv[3])]+cont[cont.find(sys.argv[3])+len(sys.argv[3]):]
        fl.write(xx)
    else:
        print("invalid argument")
except Exception as e:
    print(e)



