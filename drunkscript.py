import csv,string

reader = csv.reader(open("drunks.csv", "rU"),dialect=csv.excel)

reader.next()

for row in reader:
    if int(row[1])>19: #all if statements have to have an else
        exclamation = "Holy shit."
        judgement = "real drunk"
    elif int(row[1])<10: 
        exclamation = "Teetotaler alert!"
        judgement = "lightweight"
    else: 
        exclamation = "Merp."
        judgement = ""
    if row[0]=="Sara":
        pronoun = "she"
    else: 
        pronoun = "he"
        
    record = 45
    difference = record - int(row[1])
    percent = (float(row[1])/float(record))*100
    print "%s %s is a %s; %s drank %s drinks in one sitting once. That's %i off the record of %i or, %f.1 percent." % (exclamation, row[0], judgement, pronoun.title(), row[1], difference, record, percent)