# Librerie
from random import randint as rint

def ordina_array(a):
    #a.sort()
    #a.reverse()
    aComplesso={}

    for i in range(len(a)):
        aComplesso[int(a[i][0])]=int(a[i][2])

    return aComplesso

def creazione_campo_vuoto():
    c=[]
    for i in range(10):
        c.append([0])
        for r in range(10-1):
             c[i].append(0)
    return c

def leggi_navi():
    try:
        f = open('navi.txt', 'r')
        lett = []
        for line in f:
            lett.append(line)
        #print(lett)
    except:
        print('Errore nel leggere il file')
    finally:
        f.close()
    lett.pop(0)
    lett=ordina_array(lett)
    return lett

def controllo_posizione(griglia,posx,posy):
    for i in range(-1,2,1):
        for r in range(-1, 2, 1):
            if (posx + i) < 0:
                i+=1
            if (posy + r ) < 0:
                r+=1
            if (posx+i) > 9:
                break
            if (posy + r) >9:
                break
            if griglia[posx+i][posy+r]!=0:
                return False
    return True

def inserisci_Nave(griglia,lung):
    acc=False
    while not acc:
        orient=rint(0,1)
        if orient==0:
            posx=rint(0,10-lung)
            posy=rint(0,9)
            for a in range(lung):
                acc = controllo_posizione(griglia,posx+a,posy)
                if not acc: break
        else:
            posy=rint(0,10-lung)
            posx=rint(0,9)
            for a in range(lung):
                acc = controllo_posizione(griglia,posx,posy+a)
                if not acc: break

    if orient==0:
        for a in range(lung):
            griglia[posx+a][posy]=1
    else:
        for a in range(lung):
            griglia[posx][posy+a]=1
    return griglia

def Creazione_campo_pc():
    cpc=creazione_campo_vuoto()
    dicNavi=leggi_navi()
    for i in range(10,0,-1):
        if dicNavi.get(i):
            for r in range(dicNavi.get(i)):
                cpc=inserisci_Nave(cpc,i)
    return cpc

def maxScore():
    try:
        f = open('maxScore.txt', 'r')
        max=int(f.read())
    except:
        print('Errore nel leggere il file')
    finally:
        f.close()
        return max
