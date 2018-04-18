import urllib2
from bs4 import BeautifulSoup

url = "https://www.sec.gov/Archives/edgar/data/1720116/000119312518110178/d654140dsc13d.htm"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

for script in soup(["script", "style"]):
    script.extract()    

text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode("utf-8"))


#fields = ("NAMES OF REPORTING PERSONS",)

#response = urllib2.urlopen('https://www.sec.gov/Archives/edgar/data/1720116/000119312518110178/d654140dsc13d.htm')

#html = response.read()

#soup = BeautifulSoup(html)

#for script in soup(["script", "style"]):
#    script.extract()    # rip it out
#if html.find(field) >= 0:
#	print field

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())