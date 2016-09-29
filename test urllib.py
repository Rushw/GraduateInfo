import urllib,urllib2
from bs4 import BeautifulSoup
class MyOpener(urllib.FancyURLopener):
    version ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
 
headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Content - Type': 'application / x - www - form - urlencoded',
            'Origin':'http://202.119.4.150',
            'Referer':'http://202.119.4.150/nstudent/ggxx/XSggxxsearch.ASPx',
            
            }

myopener = MyOpener()
link = "http://202.119.4.150/nstudent/ggxx/XSggxxsearch.ASPx"
f = myopener.open(link)
soup = BeautifulSoup(f,"html.parser")
# parse and retrieve two vital form values
viewstate = soup.findAll("input", {"type": "hidden", "name": "__VIEWSTATE"})
# eventvalidation = soup.findAll("input", {"type": "hidden", "name": "__EVENTVALIDATION"})
formData = (
    # ('__EVENTVALIDATION', eventvalidation[0]['value']),
    ('__EVENTTARGET',''),
    ('__EVENTARGUMENT',''),
    ('__VIEWSTATE', viewstate[0]['value']),
    ('__VIEWSTATEENCRYPTED',''),
    ('drpyx',''),
    ('drpzy',''),
    ('1','rdossdx1'),
    ('2','rdoxslb'),
    ('txtxh',''),
    ('txtxm',''),
    ('btnSearch.x','30'),
    ('btnSearch.y','9'),
    )
encodedFields = urllib.urlencode(formData)
# second HTTP request with form data
f = myopener.open(link, encodedFields)
print f.read().decode('utf-8')
try:
    # actually we'd better use BeautifulSoup once again to
    # retrieve results(instead of writing out the whole HTML file)
    # Besides, since the result is split into multipages,
    # we need send more HTTP requests
    fout = open('tmp.html', 'w')
except:
    print('Could not open output file\n')
fout.writelines(f.readlines())
fout.close()


#
# request = urllib2.Request(link,params)

responce = urllib2.urlopen('http://202.119.4.150/nstudent/ggxx/xsggxxinfo.aspx?xh=161522')
text = responce.read().decode('utf-8')
print text