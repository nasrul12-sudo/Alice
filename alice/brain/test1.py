import numpy as np

def reg1(X, Y): 
    vallx = []
    for i in range(len(x)):
        vallX = x[i] ** 2
        vallx.append(vallX)
        
    vally = []
    for j in range(len(y)):
        vallY = y[j] ** 2
        vally.append(vallY)
    
    temp = 0
    vallxy = []
    for i in range(len(vallx)):
        vallXY = vallx[i] * vally[i]
        vallxy.append(vallXY)

    return vallx, vally, vallxy

def siqmax(x):
    sumx = 0
    for i in range(len(x)):
        sumx+=x[i]
    return sumx

def siqmay(y):
    sumy = 0
    for i in range(len(y)):
        sumy+=y[i]
    return sumy

def siqmaxy(xy):
    sumxy = 0
    for i in range(len(xy)):
        sumxy+=xy[i]
    return sumxy

def b1(n, sumx, sumy, vallx, sumxy):
    b0 = ((sumy*vallx)-(sumx*sumxy))/((n*vallx)-(sumx**2))
    return b0

def b2(n, sumx, sumy, vallx, sumxy):
    b1 = ((n*sumxy)-(sumx*sumy))/((n*vallx)-(sumx**2))
    return b1

def predic(x, b1, b2):
    Y = b1+(b2*x)
    print(Y)
    
        
if __name__ == "__main__":
    x = ([530, 300, 358, 510, 302, 300, 387, 527, 415, 512])
    y = ([89, 48, 56, 72, 54, 42,60, 85, 63, 74])

    n = len(x)
    
    sumX = []
    sumx = 0
    for i in range(len(x)): 
        sumx+=x[i]
        sumX.append(sumx)

    sumY = []
    sumy = 0
    for i in range(len(y)):
        sumy+=y[i]
        sumY.append(sumy)
        
    for i in range(len(sumX)):
        sumxy = sumX[i] * sumY[i]

    req = reg1(x,y)
    siqx = siqmax(req[0])
    siqy = siqmay(req[1])
    siqxy = siqmaxy(req[2])

    print(siqx)
    B1 = b1(n, sumx, sumy, siqx, sumxy)
    print(B1)
    B2 = b2(n, sumx, sumy, siqx, sumxy)
    print(B2)
    
    inp = int(input(">>> "))
    pred = predic(inp, B1, B2)
