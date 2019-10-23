BAND="T"
SUMSER=0
i=2

while i<=1800:
    SUMSER=SUMSER+1
    print(i)

    if BAND=="T":
        BAND="F"
        i=i+3
    else:
        BAND="T"
        i=i+2

print("La suma total es ",SUMSER)
