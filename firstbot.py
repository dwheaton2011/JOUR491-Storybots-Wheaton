import csv, string, datetime

reader = csv.reader(open("blsdata.csv", "rU"), dialect=csv.excel)

reader.next()

blslist = []

for row in reader:
    blslist.append(row)

currentyear = blslist[-1]
currentyear = filter(None,currentyear)

yearlen = len(currentyear)

if yearlen != 1:
    currentmonth = currentyear[-1]
    previousmonth = currentyear[-2]
    reportyear = int(currentyear[0])
    reportmonth = len(currentyear)-1
    reportdate = datetime.datetime(reportyear, reportmonth, 1)
else:
    currentmonth = currentyear[1]
    previousyear = blslist[-2]
    previousmonth = previousyear[-1]
    reportyear = int(currentyear[0])
    reportmonth = len(currentyear)-1
    reportdate = datetime.datetime(reportyear, reportmonth, 1)

previousyear = blslist[-2]
previousyearmonth = previousyear[yearlen-1]

if currentmonth > previousmonth:
    verb = "increased"
    adjective = "higher"
elif currentmonth == previousmonth:
    verb = "held steady"
    adjective = "the same as"
else:
    verb = "decreased"
    adjective = "lower"
    
pctchange = ((float(currentmonth)-float(previousmonth))/float(previousmonth)*100)

#current month, previous monht, previous years

lastyear = (float(previousyearmonth)-float(currentmonth))



print verb, abs(pctchange)
print "WASHINGTON (AP) -- The United States' unemployment rate %s last month, to %s percent. That represents a percent change %s of percent from two months ago. That is %.2f percentage points %s than this time last year, according to the Bureau of Labor Statistics." % (verb, currentmonth, lastyear, abs(pctchange), adjective)