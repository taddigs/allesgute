
def aufzählung():
    monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November","Dezember"]
    tage =[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(len(monate)):

        for e in range(tage[i]):
            print("Alles Gute für den ",e+1,"\b.",monate[i] ,"2022 \b.")

aufzählung()