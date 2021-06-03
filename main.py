# Battaglia navale
# Campo:
# 0=acqua
# 1=nave/colpito
# 2=colpito e affontato
# 3=colpo a vuoto

import BattLibCreazione as bc
import BattLibGioco as bg

nNavi=bc.leggi_navi()
nNavi=sum(nNavi.values())
nNaviRimaste=nNavi

cb=bc.creazione_campo_vuoto()
cpc=bc.Creazione_campo_pc()
maxS=bc.maxScore()

#bg.stampa_mappa(cpc)

tn=1
for scorr in range(10): print("\n")
print("\033[1;34mBATTAGLIA NAVALE by VAR")
print("\033[2;35mTentativi: "+str(tn)+"     --> Record: "+str(maxS))
print('\033[mNavi: ' + str(nNavi))

#for n in range(10):
while not bg.controlo_vitt(cpc,cb):
    tn+=1
    bg.stampa_mappa(cb)
    cxy = input('\033[mScrivi le coordinate: ')
    cxy = bg.check_Coordinate(cxy, cb)
    while cxy==False:
        cxy=input('Non valide -> riscrivi le coordinate: ')
        cxy=bg.check_Coordinate(cxy,cb)

    for scorr in range(10): print("\n")
    print("\033[1;34mBATTAGLIA NAVALE by VAR")
    print("\033[2;35mTentativi: "+str(tn)+"     --> Record: "+str(maxS)+'\n')

    if bg.check_Colpito(cpc,cb,cxy): nNaviRimaste-=1
    print('\033[m       Ancora '+str(nNaviRimaste)+' su '+str(nNavi))

tn-=1
for scorr in range(20): print("\n")

print("\033[1;34mBATTAGLIA NAVALE by VAR")
print("\033[2;35mScore: "+str(tn)+"     --> best score: "+str(maxS)+'\n')
bg.stampa_mappa(cb)
print("\n\033[1;32mHAI VINTO! tentativi: "+str(tn))

if tn<maxS :
    print("\n\033[1;31mRECORD BATTUTO!")
    bg.New_maxScore(tn)

