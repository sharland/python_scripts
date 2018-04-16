import urllib.request

x = urllib.request.urlopen('http://ikhowudi.com')
print(x.read())
