df = pd.read_csv('Test.csv')
del df["Instance"]


X1 = df["X1"]
X2 = df["X2"]
X3 = df["X3"]
lst = [X1,X2,X3]
Y = df["Class"]
tree = []
level = 1
global level2
level2 = 0
VALUE = 100
XpS = 0
XpN = 0
PARENT = 'Y'

def partition(level,target,lst,df,parent,value):
    """
    This method partitions the node based on Information Gain recursively.
    """
    Y = target
    X = df[lst[highIG(lst,Y)].name]
    
    Xp = [s for (p,s) in zip(X,Y)   if p == 1 ]
    Xn = [s for (p,s) in zip(X,Y)   if p == 0 ]
    
    print "You should split on:",X.name
    valuePa = "Parent Value:",value
    parentPa = "Parent is:",parent
    tree.append((level,X.name,parentPa,valuePa))
   
    if all(v == 0 for v in Xp) or all(v == 1 for v in Xp):
        XpS = 0
    else:
        XpS = 1
        
    if all(v == 0 for v in Xn) or all(v == 1 for v in Xn):
        XpN = 0
    else:
        XpN = 1
    for i in tree:
        print i
    tada = (level,tree,X,Xp,"Split Needed on Left" if XpS else "Left Is Pure",Xn,"Split Needed on Right" if XpN else "Right Is Pure")
    print "Split done:",(tada[4],tada[6])
    
    if tada[4] == 'Split Needed on Left':
        global level2
        level2 = tada[0] + 1
        print "\n\n\n"
        print "This is level",level+1
        df2 = df[tada[2]==1]
        Y2 = df2["Class"]
        X1 = df2["X1"]
        X2 = df2["X2"]
        X3 = df2["X3"]
        lst2 = [X1,X2,X3]
        parent = X.name
        tada2 = partition (level2, Y2,lst2,df2,parent,1)
    else:
        pass
        
    if tada[6] == 'Split Needed on Right':
        level3 = level + 1
        print "\n\n\n"
        print "This is level",level+1
        df3 = df[tada[2]==0]
        Y3 = df3["Class"]
        X1 = df3["X1"]
        X2 = df3["X2"]
        X3 = df3["X3"]
        lst3 = [X1,X2,X3]
        parent = X.name
        tada2 = partition (level3,Y3,lst3,df3,parent,0)
    else:
        pass
