def controlo_vitt(campo,cb):
    for x in range(10):
        for y in range(10):
            if campo[x][y]==1:
                if cb[x][y]!=2: return False
    return True

def numeri_Lett(n):
    if n==0: return 'A'
    elif n==1: return 'B'
    elif n==2: return 'C'
    elif n==3: return 'D'
    elif n==4: return 'E'
    elif n==5: return 'F'
    elif n==6: return 'G'
    elif n==7: return 'H'
    elif n==8: return 'I'
    elif n==9: return 'J'

def lett_Numeri(n):
    n=n.upper()
    if n=='A': return 0
    elif n=='B': return 1
    elif n=='C': return 2
    elif n=='D': return 3
    elif n=='E': return 4
    elif n=='F': return 5
    elif n=='G': return 6
    elif n=='H': return 7
    elif n=='I': return 8
    elif n=='J': return 9
    else: return -1

def stampa_mappa(campo):
    print('\033[1;33m\n   1 2 3 4 5 6 7 8 9 10')
    for i in range(10):
        print('\033[1;33m'+numeri_Lett(i)+'|',end=' ')
        for r in range(10):
            if campo[i][r]==0:
                print('\033[m'+'-',end=' ')
            elif campo[i][r]==1:
                print('\033[35m'+'C',end=' ')
            elif campo[i][r]==2:
                print('\033[31m'+'A',end=' ')
            elif campo[i][r]==3:
                print('\033[34m'+'V',end=' ')
            else:
                print('\033[m'+str(campo[i][r]),end=' ')
        print()

def check_Coordinate(posxy,griglia):
    if len(posxy)==2:
        if posxy[0]=='0' or posxy[1]=='0': return False

    if len(posxy)==3:
        if not(posxy[0].isdigit()) and posxy[1]=='1' and posxy[2]=='0':
            posxy=('0'+posxy[0])
        elif not(posxy[2].isdigit()) and posxy[0]=='1' and posxy[1]=='0':
            posxy=('0'+posxy[2])

    if len(posxy)==2 and((posxy[0].isdigit() and not(posxy[1].isdigit())) or (posxy[1].isdigit() and not(posxy[0].isdigit()))):
        #print(posxy)
        if posxy[0].isdigit():
            posy=int(posxy[0])-1
            if posy==-1: posy=9
            posx=lett_Numeri(posxy[1])
        else:
            posy=int(posxy[1])-1
            if posy==-1: posy=9
            posx=lett_Numeri(str(posxy[0]))

        if posx==-1: return False
        if(griglia[posx][posy]!=0):return False
        return [str(posx),str(posy)]
    else: return False

def check_Affondato(cpc,cb,xy):
    x=int(xy[0])
    y=int(xy[1])
    i=0
    while x-i>=0 and int(cpc[x-i][y])==1:
        if int(cb[x-i][y])!=1:
            return False
        i+=1
    i=1
    while x+i<=9 and int(cpc[x+i][y])==1:
        if int(cb[x+i][y])!=1:
            return False
        i+=1
    i=1
    while y+i<=9 and int(cpc[x][y+i])==1:
        if int(cb[x][y+i])!=1:
            return False
        i+=1
    i=1
    while y-i>=0 and int(cpc[x][y-i])==1:
        if int(cb[x][y-i])!=1:
            return False
        i+=1

    i=0
    while x-i>=0 and int(cpc[x-i][y])==1:
        cb[x-i][y]=2
        i+=1
    i=1
    while x+i<=9 and int(cpc[x+i][y])==1:
        cb[x+i][y]=2
        i+=1
    i=1
    while y+i<=9 and int(cpc[x][y+i])==1:
        cb[x][y+i]=2
        i+=1
    i=1
    while y-i>=0 and int(cpc[x][y-i])==1:
        cb[x][y-i]=2
        i+=1
    print('\033[1;31m e affontata!',end=' ')
    return True

def check_Colpito(cpc,cb,xy):
    x=int(xy[0])
    y=int(xy[1])
    if int(cpc[x][y])==1:
        cb[x][y]=1
        print('\033[1;31mColpita',end='')
        if check_Affondato(cpc,cb,xy): return True
        print('\033[1;31m!',end=' ')
    elif int(cpc[x][y])==0:
        cb[x][y]=3
        print('\033[1;36mMancata!',end='')

def New_maxScore(newMax):
    try:
        f = open('maxScore.txt', 'w')
        f.write(str(newMax))
    except:
        print('Errore nel leggere il file')
    finally:
        f.close()
        return max
