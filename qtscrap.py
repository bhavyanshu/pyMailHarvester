import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtWebKit import *
from BeautifulSoup import BeautifulSoup
import re 
from HTMLParser import HTMLParser
import urllib2


  
class Render(QWebPage):  
  def __init__(self, url):
			self.app=QApplication.instance()
			print "Checking if QApplication already exists or not."	
			if not self.app: 
     					self.app = QApplication(sys.argv)
					print "Created Qapplication because it does not exist."
                	QWebPage.__init__(self)
                	self.loadFinished.connect(self._loadFinished)
                	self.mainFrame().load(QUrl(url))
                	self.app.exec_()
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  


commonURL = ".yellowpages.co.in/"
url = "http://ahmedabad" + commonURL + "Catering+Services"
soup = BeautifulSoup(urllib2.urlopen(url))
list = soup.findAll("div" ,{"class":"MT_20"})
for i in range(1, len(list)):
                list[i] = list[i].find("a")['href']
                list[i] = "http://ahmedabad.yellowpages.co.in/" + list[i]
                print list[i]
                url = list[i]  
		# Create a Qt application
		r = Render(url)  
		html = r.frame.toHtml()  
		soup = BeautifulSoup(html)
		data = soup.findAll("span" ,{"class":"jqOfcEmail"})
		print data
		stringhtml= unicode.join(u'\n',map(unicode,data))
		regexp_email = r"\w+@\w+\.(?:com|in)"
		pattern = re.compile(regexp_email)
		emailAddresses = re.findall(pattern, stringhtml)
		print emailAddresses
