import numpy
import pandas as pd
import numpy as np






def getMostNeg(list):

  Negcoeffind=pd.Series(list).idxmin()
  Negcoeff= ratioTest[Negcoeffind]
  if Negcoeff<0:

     return Negcoeffind

  else:
      # x= x1-x2, y= y1-y2
      return 0
#
def getLeastNonNeg(list):

    for i in range(1, len(list)):
        if list[i]>0:
           minel= list[i]
           minelindex= i

    for w in range(1,len(list)):
        if list[w]< minel and list[w]>0 :
            minel= list[w]
            minelindex =w
    print(minel)
    print(minelindex)
    #the case of all are negative

    return minelindex


def func_selec(M,rtest):

     if M== 'max':
         colno=pd.Series(rtest).idxmax()

     elif M =='min':
         colno= getMostNeg(rtest)

     return colno
# def RatioTes(colno):
#
#     for q in range( n_constrains-1):
#         if (Table[q][n_var-1] >= 0 and Table[q][colno] > 0 ):
#             ratioTest.append(Table[q][n_var-1] /Table[q][colno])
#
#    # while min(ratioTest)<0:
#         #ratioTest.remove(min(ratioTest))
#         if len(ratioTest)==0:
#             print("The function is open ")
#             # return something stops it
#             return 0
#        # min(ratioTest)
#     leaveAndEnter(min(ratioTest), colno)
# def leaveAndEnter(Lrw, Ecl):
#     print("Now x",Xb[Lrw], "leaves and x ")
#     print(Ecl,"Enters the basis")
#     Xb[Lrw]=Ecl
#     Pivot = Table[Lrw][Ecl]
#     print(Pivot)
#     for i in range(n_var):
#         Table[Lrw][i]= Table[Lrw][i]/Pivot
#     for a in range (len(Xb)):
#          B[Lrw][a]= B[Lrw][a]/Pivot# 1 canonical
#     for y in range(n_constrains):
#         MulVal = (Pivot /Table[y][Ecl]) * -1
#         print(MulVal)
#         for u in range (n_var):
#             Table[y][u]=Table[Lrw][u] *MulVal + Table[y][u]
#     return Table
def getY(cb,Xb):

    for o in range(len(Xb)) :
        yo = 0
        for p in range(len(B)):
            yo= yo+ cb[(Xb[o][0])-1]* B[o][p]
        Y.append(yo)
    return Y

def updateY():

    for o in range(len(Y)):
        yo = 0
        for p in range(len(B)):
            if B[o][p]==0:
                yo=yo+0
            else:
                yo= yo+ cb[(Xb[o][0])-1]* B[p][o]
        Y[o]= yo
    return Y

def getc1_yP(basic, Y, cb):

    for z in range(n_var):
        ratioTest.append([basic[z][0]])
        yo=0
        for c in range(len(Y)):
            yo= yo+  (Y[c]* basic[z][c+1])
        ratioTest[z].append(cb[(basic[z][0])-1]-yo)
    rtest=[]
    for u in range(n_var):
        rtest.append(ratioTest[u][1])

    colno = func_selec(M, rtest)
    print("X", ratioTest[colno][0], "is entering the basis and X")
    #updateBasic(ratioTest[colno][0]-1)
    emergingX= ratioTest[colno][0]-1
    return emergingX

def updategetc1_yP(basic, Y, cb):

    for z in range(n_var):
        ratioTest[z][0]=basic[z][0]
        yo = 0
        for b in range(len(Y)):
            yo = yo + (Y[b] * basic[z][b + 1])
        ratioTest[z][1]=(cb[(basic[z][0]) - 1] - yo)
    rtest = []

    for u in range(n_var):
        rtest.append(ratioTest[u][1])
    print("ratioTest:  ", ratioTest)
    print("rtest: ", rtest)
    colno = func_selec(M, rtest)
    print("X", ratioTest[colno][0], "is entering the basis and X")
    emergingX = ratioTest[colno][0] - 1

    return emergingX

def getPj(B,p, colno):

    for o in range(len(B)) :
        yo = 0
        for l in range(len(p[colno])-1):
            yo= yo+ p[colno][o+1] * B[o][l]
        Pj.append(yo)
    return Pj
def updatePj(B,p,colno):

    # for o in range(len(B)) :
    #     yo = 0
    #     for l in range(len(p[colno])-1):
    #         if B[l][colno+1]==0:
    #             yo=0
    #         else:
     A= np.array([[B[0][0],B[1][0],B[2][0]],
                  [B[0][1],B[1][1],B[2][1]],
                  [B[0][2],B[1][2],B[2][2]]])
     B= np.array([p[colno][1],p[colno][2],p[colno][3]])
     Pj=np.linalg.solve(A,B)

     print(Pj)
     return np.linalg.solve(A,B)

def getTheta(B,Pj,Xb):

    for t in range(n_constrains):
        theta.append(numpy.asarray(Xb[t][1])/numpy.asarray(Pj[t]))
    Lrw= getLeastNonNeg(theta)
    print(Lrw+n_var+1,"is leaving the basis")
    updateXb(numpy.asarray(Xb[Lrw][1])/numpy.asarray(Pj[Lrw]), Lrw,Pj)
    updateB2(B)
    B=updateB(Lrw,Pj)

    updateBasic(colno,Lrw)
    #print(Lrw)
    return (Xb[Lrw][1])/numpy.asarray(Pj[Lrw])

def updateTheta(Pj,Xb,B):

    for t in range(n_constrains):
        theta[t]=(numpy.asarray(Xb[t][1])/numpy.asarray(Pj[t]))
    print("thetasss: ", theta)
    Lrw= getLeastNonNeg(theta)
    print(Lrw+n_var+1,"is leaving the basis")
    updateXb((Xb[Lrw][1])/numpy.asarray(Pj[Lrw]), Lrw,Pj)

    B=updateB(Lrw,Pj)

    updateBasic(colno,Lrw)
    #print(Lrw)
    return B


def updateXb(theta, Lrw,Pj):

     for i in range(len(Xb)):
         if i == Lrw:
             Xb[i][0]= colno+1
             Xb[i][1]= theta
         else:
             Xb[i][1]= numpy.asarray(Xb[i][1]) - numpy.asarray(Pj[i])*theta
     return Xb

def updateB(Lrw,Pj):

    for i in range(n_constrains):
        B[Lrw][i]= Pj[i]
    Bin= np.linalg.inv(B)
    print(Bin)
    return Bin

def updateB2(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            B2[i][j]=B[i][j]
    print("B2: ", B2)

def updateBasic(colno, Lrw):
    print(colno)
    print(Lrw)
    for i in range(n_constrains+1):
        if i==0:
            basic[colno][i]= Lrw+n_var+1
        else:
            basic[colno][i]= B2[Lrw][i-1]
    return basic
emerging=[]
Lrw=0
emergingX=0
B=[]
B2=[]
Xb=[]
Pj=[]
basic=[]
sol=[]
Table= []
Y=[]
cb=[]
p=[]
E=[]
theta=[]
ratioTest=[]
n_var =int(input("Enter the number of variables: "))
n_constrains= int(input("Enter the number of constrains: "))
for e in range(n_constrains+1):
    Table.append([])
    for r in range (n_var):
        Table[e].append(0)

j=0
for v in range (n_var):
    basic.append([])
    basic[v].append(v+1)


for i in range(n_constrains):
   print("--- Next constraint ---")
   Xb.append([])

   for j in range( n_var +1):

        if j< n_var:
           print("coefficient of x", j)
           basic[j].append(int(input()))
        if j == n_var-1:
            sign= input(  "for (>=) enter g\n for (<=) enter s\n for (=) enter e ")
            if sign =='s':
                Xb[i].append(n_var+i+1)

          #if sign =='g':
        if j== n_var:

            #sol.append()
            Xb[i].append(int(input("The solution for constraint")))
        #input 00 in the function last input

#creating the B matrix
for y in range(len(Xb)):

    B.append([])
    for u in range(len(Xb)):

        if y == u:
            B[y].append(1)
        else:
            B[y].append(0)

print(B)
for i in range( len(B)):
    B2.append([])
    for j in range(len(B[0])):
        B2[i] .append(B[i][j])
print("B2: ",B2)
#Done creating table
print("Enter the objective function: ")

for t in range(n_var+n_constrains):
    if t <n_var:
        print("coefficient of x", t)
        #Table[n_constrains][t] = int(input())
        cb.append(int(input()))
    else:
        cb.append(0)

M= input("Enter (max) to maximize or (min) to minimize function?")
getY(cb, Xb)
colno=getc1_yP(basic, Y, cb)

if colno <n_var:
    getPj(B, basic,colno)

else:
    getPj(B, B,colno)

Lrw= getTheta(B,Pj,Xb)


updateY()

colno=updategetc1_yP(basic, Y, cb)
print(colno)
if colno <n_var:

     Pj= updatePj(B, basic,colno)
else:
    updatePj(B, B,colno)
B=updateTheta(Pj, Xb,B)
updateY()

print("Pj:", Pj)

#
#Lrw= getTheta(Pj,Xb)
print("Cb:  ", cb)
print("y: ", Y)
print("Xb: ", Xb)

print("B: ",B)
print("basic: ", basic)
print("X" ,Xb[0][0],"*=", Xb[0][1])
print("X" ,Xb[1][0],"*=", Xb[1][1])
print("X" ,Xb[2][0],"*=", Xb[2][1])
print("The objective function is now:")
for l in range(n_var):
    sol=0
    if Xb[l][0]==1:
        sol=sol+Xb[l][1]*cb[0]
    if Xb[l][0]==2:
        sol=sol+Xb[l][1]*cb[1]
    print(sol)
# print(RatioTes(colno))
# rowno =int(RatioTes(colno))
# print(Xb[rowno])
# leaveAndEnter(rowno,colno)

#print(Table)
#print(ratioTest)
# defining B and c
