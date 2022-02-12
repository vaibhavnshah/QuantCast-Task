import unittest
import quantcast

class testQuantCastSol(unittest.TestCase):
	def setUp(self):
		self.logStore = quantcast.StoreLog()

	def test_addToMap(self):
		expected = {"2000-01-01":{"SAZuXPGUrfbcn5UA":1}}
		self.assertEqual(self.logStore.addToMap("2000-01-01","SAZuXPGUrfbcn5UA").hashmap, expected,'StoreLog.addToMap() failed to process another cookie/timestamp datapoint')

	def test_processLogFile(self):
		logStore.hashmap = {}
		logStore.processLogFile("./logFile.csv")
		expected = {'2018-12-09': {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1}, '2018-12-08': {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1}, '2018-12-07': {'4sMM2LxV07bPJzwf': 1}}
		self.assertEqual(self.logStore.hashmap, expected,'StoreLog.processLogFile() failed to execute properly')

	def test_getMaxCookieOnDate(self):
		logStore.hashmap = {}
		logStore.processLogFile("./logFile.csv")
		popularCookie08 = logStore.getMaxCookieOnDate("2018-12-08")
		popularCookie09 = logStore.getMaxCookieOnDate("2018-12-09")
		expected08 = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
		expected09 = ["AtY0laUfhglK3lC7"]
		self.assertEqual(popularCookie08, expected08,'StoreLog.getMaxCookieOnDate() failed to execute properly on test case 2018-12-08')
		self.assertEqual(popularCookie09, expected09,'StoreLog.getMaxCookieOnDate() failed to execute properly on test case 2018-12-09')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
