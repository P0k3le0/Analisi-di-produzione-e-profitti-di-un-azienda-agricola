import pandas as pd
import random as ran
import math
UMI = ran.randint(0,100)#Percentuale umidità UMI
TMA = ran.randint(8,19)#Temperatura media annua TMA
#Precipitazioni medie annue PMA
if (UMI>50):
    PMA= ran. randint(1300,3500)
else:
    PMA= ran.randint(250,1300)

#If chain per efficienza Grano EGr
if (UMI >= 80):
    EGr=ran.randint(1,49)
elif (UMI<10):
    EGr=ran.randint(50,80)
elif (UMI<15 and UMI>=10):
    EGr=ran.randint(80,100)
elif (UMI<50 and UMI>=15):
    EGr=ran.randint(50,80)
elif (UMI<80 and UMI >=50):
    EGr=ran.randint(1,49)
else:
    EGr='Null'
#If chain per peso Grano PGr
if (EGr>=80):
    PGr=ran.randint(1500,2000)
elif(EGr<80 and EGr>=50):
    PGr=ran.randint(600,1500)
else:
    PGr=ran.randint(100,500)
    
#If chain per efficienza Fieno Efi
if (UMI >= 60):
    EFi=ran.randint(1,50)
elif (UMI<60 and UMI>=30):
    EFi=ran.randint(50,100)
else:
    EFi=ran.randint(1,50)
#If chain per peso Fieno PFi
if (EFi>=80):
    PFi=ran.randint(2600,3500)
elif(EFi<80 and EFi>=50):
    PFi=ran.randint(1000,2500)
else:
    PFi=ran.randint(100,1000)
#If chain per efficienza Uva EUv
if (UMI>=80):
    EUv=ran.randint(1,49)
elif (UMI<80 and UMI>=60):
    EUv=ran.randint(50,80)
elif (UMI<60 and UMI>=40):
    EUv=ran.randint(80,100)
elif (UMI<40 and UMI>=10):
    EUv=ran.randint(50,80)
elif (UMI<10):
    EUv=ran.randint(1,49)
else:
    EUv='Null'
#If chain per peso Uva PUv
if (EUv>=50):
    PUv=ran.randint(401,1000)
else:
    PUv=ran.randint(100,400)

#If chain per efficienza Avena EAv
if (UMI>=80):
    EAv=ran.randint(50,80)
elif (UMI<80 and UMI>=60):
    EAv=ran.randint(80,100)
elif (UMI<60 and UMI>=30):
    EAv=ran.randint(50,80)
elif (UMI<30):
    EAv=ran.randint(1,49)
else:
    EAv='Null'
#If chain per peso Avena PAv
if (EAv>=50):
    PAv=ran.randint(300,600)
else:
    PAv=ran.randint(100,299)

#If chain per efficienza quadrifogli EQu
if (UMI>=50):
    EQu=ran.randint(50,100)
else:
    EQu=ran.randint(1,49)
#If chain per peso Quadrifoglio PQu
if (EQu>=50):
    PQu=ran.randint(3,5)
else:
    PQu=ran.randint(1,2)
#Uova
EUo = ran.randint(1,100)
PUo = ran.randint(100,250)
#Carne bovina
ECb = ran.randint(1,100)
PCb = ran.randint(50,400)
#spese
Stipe= ran.randint(1000,3000)
Mangi= ran.randint(600,800)
Semi= ran.randint(1100,1600)
Manu= ran.randint(500,800)
Elettr = ran.randint(500,1200)
Carbu = ran.randint(400,800)
acq = ran.randint(2000,5000)
#profitti in relazione al peso/quantità
PrUo = PUo * 0.50
PrGr = PGr * 1.50
PrCb = PCb * 5.50
PrUv = PUv * 3.50
PrFi = PFi * 2.50
PrAv = PAv * 4.50
LvPt = ran. randint(1500,3500)
SpsAnn = Stipe + Mangi + Semi + Manu + 600 + Carbu + acq + Elettr + 1500
PrfAnn = PrUo + PrGr + PrCb + PrUv + PrFi + PrAv + LvPt
data = {'Prodotti':['Uova','Grano(Kg)','Carne bovina(Kg)','Fieno(Kg)','Uva(Kg)','Avena(Kg)','Quadrifogli(Kg)',
            'Spese','Stipendio operai','Mangimi','Disserbanti e Concimi','Semi',
            'Carburanti','Acqua','Energia elettrica','Manutenzione','Fondo di emergenza',
            'Profitti','Uova','Grano','Carne bovina','Uva','Balle di Fieno','Avena','Lavoro per terzi'],
'Quantità prodotti':[PUo,PGr,PCb,PFi,PUv,PAv,PQu,
            'Quantità spese',Stipe,Mangi,'600',Semi,
            Carbu,acq,Elettr,Manu,'1500',
            'Quantità profitti',PrUo,PrGr,PrCb,PrUv,PrFi,PrAv,LvPt],
'Placeholder':[EUo,EGr,ECb,EFi,EUv,EQu,EAv,'spese',UMI,TMA,PMA,SpsAnn,PrfAnn,'','','','','','','','','','','','']}

df = pd.DataFrame(data,columns=['Prodotti','Quantità prodotti','Placeholder'])

df.to_csv('Bernardone_Leo_0312200721_random.txt',index=False)
print('File creato con successo')
