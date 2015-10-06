#UNL scraper bot
from twython import Twython
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords
import sys, random, time, string, codecs
from datetime import datetime
import csv


API_KEY = 'OqnYUXdcLGV5fhrRs4veM6nUr'
API_SECRET = 'Q8YqoYd6jHm5Kv4tVFIsSyuIL9fgLUgUGG9kbDJ7ZjDffmhu7s' 
ACCESS_TOKEN = '21812439-Hy7iB3hv6GtUZYbEnzakHbfdXa0W6945os2SpVo73'
ACCESS_TOKEN_SECRET = 'W8Rf8ZHP4Z7ypjeuTBJAUzH6zEjDw3NC4RBOkL9mXxcSo' 

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def get_hourly():
    UNLusers =  ["UNLnews","UNLresearch","UNLOnline","UNLincoln","UNLGreek","UNL_UHC","u_nebraska","ASUN_UNL","NebraskaAlumni","UNLHousing","Harvey_Perlman","RedCladLoon"]

    statuses = []
    
    f = codecs.open('scraper.txt', 'ab+', encoding='utf-8') 
    for line in f:
        statuses.append(line)
    
    for user in UNLusers:
        user_timeline = twitter.get_user_timeline(screen_name='%s' % user)
        for tweet in user_timeline:
            if tweet['text'] not in statuses:
                statuses.append(tweet['text'])
                                                                       
    local_search = twitter.search(q='python', geocode='40.810556,96.680278,5mi')
    for tweet in local_search['statuses']:
        if tweet['text'] not in statuses:
            statuses.append(tweet['text'])

    hash_search = twitter.search(q='python', hashtags= ["#UNL"]) 
    for tweet in hash_search['statuses']:
        if tweet['text'] not in statuses:
            statuses.append(tweet['text'])
                                  
    for status in statuses:
        f.write('%s\n' % status) 
        
    return "Got hourly searches"
                                                                         
def process_report():
    tokenizer = RegexpTokenizer(r'\w+')
    f = open('scraper.txt','r')
    textfile = unicode(f.read(),errors='ignore')
    words = tokenizer.tokenize(textfile)
    filtered_words = [w for w in words if not w in stopwords.words('english')]
    fdist = FreqDist(filtered_words)
    with open("report.csv", "wb") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        writer.writerows(fdist.items())
    return "Wrote report"

now = datetime.now


hourly = get_hourly()

daily = process_report()