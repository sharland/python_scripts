import arrow
from time import sleep

for i in range(100):
	localTime = arrow.now('Europe/London') #use olson tz database
	localTimeNice = localTime.format('YYYY-MM-DD HH:mm:ss')
	print(localTimeNice)
	sleep(1)


