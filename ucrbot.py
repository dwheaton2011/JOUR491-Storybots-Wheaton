

import csv, string, datetime

reader = csv.reader(open("UCRdata.csv","rU"), dialect=csv.excel)
                    
reader.next()            


for row in reader:
   

    try: 
        rate12 = (float(row[4])/float(row[3]))*100000
        rate11 = (float(row[14])/float(row[15]))*100000
        if rate12 > rate11:
            verb = "increased"
        elif rate11 > rate12:
            verb = "decreased"
        else:
            verb = "held steady"

        mrate12 = (float(row[5])/float(row[3]))*100000
        mrate11 = (float(row[16])/float(row[15]))*100000
        if mrate12 > mrate11:
            mverb = "increased"
        elif mrate11 > mrate12:
            mverb = "decreased"
        else:
            mverb = "held steady"

        rrate12 = (float(row[6])/float(row[3]))*100000
        rrate11 = (float(row[17])/float(row[15]))*100000
        if rrate12 > rrate11:
            rapeverb = "increased"
        elif rrate11 > rrate12:
            rapeverb = "decreased"
        else:
            rapeverb = "held steady"

        robrate12 = (float(row[7])/float(row[3]))*100000
        robrate11 = (float(row[18])/float(row[14]))*100000
        if robrate12 > robrate11:
            robverb = "increased"
        elif robrate11 > robate12:
            robverb = "decreased"
        else:
            robverb = "held steady"

        rate12 = (float(row[4])/float(row[3]))*100000
        rate10 = (float(row[23])/float(row[24]))*100000
        rate09 = (float(row[34])/float(row[35]))*100000
        if rate12 > rate09:
            exsen = "The overall crime rate rose since 2009."
        elif rate12 < rate09:
            exsen = "The overall crime rate decreased since 2009."
        elif rate12 == rate09:
            exsen = "The crime rate is the same as it was in 2009."
        else:
            exsen = ""

        if rate12 > rate11 > rate10 > rate09:
            final = "This is the forth year in the row the rate increased."
        elif rate12 < rate11 < rate10 < rate09:
            final = "This is the fourth year in a row the rate decreased."
        elif rate12 > rate11 > rate10:
            final = "This is the third year of this downward trend."
        elif rate12 < rate11 < rate10:
            final = "This is the third year of this upward trend."
        else:
            final = ""
    except:
        continue
        

    print "WASHINGTON (AP)-- The overall crime rate for %s, %s %s by %.2f percent according to updated data from the FBI. The number of murders %s by %.2f percent. Violent rapes %s by %.2f percent as well. Robberies %s since last year by %.2f percent. %s " %(row[2], row[1], verb, rate12, mverb, mrate12, rapeverb, rrate12, robverb, robrate12, exsen)
    
