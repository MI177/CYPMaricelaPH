SUMPAR=0
SUMIMP=0
CUEPAR=0

for i in range (1,271,1):
    NUM=int(input("Ingrese el numero "))
    
    if NUM!=0:
        if (-1**NUM)>0:
            SUMPAR=SUMPAR+NUM
            CUEPAR=CUEPAR+1
        else:
            SUMIMP+NUM
           
PROPAR=SUMPAR/CUEPAR
print(PROPAR,CUEPAR)

