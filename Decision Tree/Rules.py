# Make use of pDT
# Now we have to formalize rules agian without using libraries then use it on the test data and mwasure the error.
# At each node at level d we can have at max s^d modes
# So decide such as 1,2,4... , but may be less than s^d levels at level d

for i in pDT:
    print "level:",i[0]
    print "parent:",i[1],":",i[3]
    print "split on:",i[5]
    print "if",i[5],"=1 then",i[13]
    print "Else if",i[5],"=0 then",i[18]
    print "\n"
    
# Let's create a list where each list is a 2^1 multilist.
