import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d') #flag for day
parser.add_argument('filepath') #filepath given

#parse cli
args = parser.parse_args()
filepath = args.filepath
specifiedDate = args.d

class StoreLog:
	def __init__(self):
		self.hashmap = {} #map dates to hashmaps of cookies to frequencies for that particular date

	def addToMap(self,day,cookie):
		if day not in self.hashmap:
			self.hashmap[day] = {}
		if cookie not in self.hashmap[day]:
			self.hashmap[day][cookie] = 0
		self.hashmap[day][cookie] += 1

	def processLogFile(self,filepath):
		file  = open(filepath)
		contents = file.read()
		activityLog = contents.splitlines()
		for activity in activityLog:
			cookie,timestamp = activity.split(",")
			day = timestamp.split("T")[0] #the date is everything before first T
			self.addToMap(day, cookie)

	def getMaxCookieOnDate(self,specifiedDate):
		maxFreq = 0
		cookies = []
		dayOfInterest = {}
		if specifiedDate in self.hashmap:
			dayOfInterest = self.hashmap[specifiedDate]
		for cookie in dayOfInterest.keys():
			if dayOfInterest[cookie] > maxFreq:
				cookies = []
				cookies.append(cookie)
				maxFreq = dayOfInterest[cookie]
			elif dayOfInterest[cookie] == maxFreq:
				cookies.append(cookie)
		return cookies

#print desired output
logStorage = StoreLog()
logStorage.processLogFile(filepath)
freqCookies = logStorage.getMaxCookieOnDate(specifiedDate)
print("\n".join(cookie for cookie in freqCookies))


