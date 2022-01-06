import csv
with open('E:\python\Python Codes\data3.csv','r')as f:
 reader=csv.reader(f)   
 your_list=list(reader)

 h=[['0','0','0','0','0',]]
 for i in your_list:
     print(i)
     if i[-1] =="Yes":
         j=0
         for x in i:
             if x !="Yes":
                 if x !=h[0][j] and h[0][j]=='0':
                     h[0][j]=x
                 elif x!=h[0][j] and h[0][j]!='0':
                     h[0][j]='?'
             j=j+1
 print("*********************************************************************")
 print("the maximally specific hypothesis is",h)
