from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#choose webdriver
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
#access HLTV page
driver.get("https://www.hltv.org/matches/#")

#check live matches
liveMatchesElement = driver.find_element_by_class_name('liveMatchesContainer')
teamNames = liveMatchesElement.find_elements_by_class_name('matchTeamName')
matchesObj = {}
liveMatchesList = []
print('*********** Partidas ao vivo ********************')
for team in range(len(teamNames)):
	if(team%2 == 1):
		matchesObj = {
			'team1': teamNames[team - 1].text ,
			'team2': teamNames[team].text
		}
		liveMatchesList.append(matchesObj)
		matchesObj = {}

print(liveMatchesList)


#check other matches
upcomingMatchesElement = driver.find_element_by_class_name('upcomingMatchesContainer')
upcomingMatchesSectionByDate = upcomingMatchesElement.find_elements_by_class_name('upcomingMatchesSection')


upcomingMatchesList = []

for section in range(len(upcomingMatchesSectionByDate)):
	sectionObj = {}

	date = upcomingMatchesSectionByDate[section].find_element_by_class_name('matchDayHeadline').text
	upcomingMatch = upcomingMatchesSectionByDate[section].find_elements_by_class_name('upcomingMatch')

	matchList = []

	for match in range(len(upcomingMatch)):
		matchObj = {}
		matchInfo = upcomingMatch[match].find_element_by_class_name('matchTime').text
		matchTeams = upcomingMatch[match].find_elements_by_class_name('matchTeamName')

		if len(matchTeams) == 2:
			matchObj = {
				'start at (br tz)': matchInfo,
				'team1': matchTeams[0].text,
				'team2': matchTeams[1].text
			}
			matchList.append(matchObj)
	if(len(matchList) > 0):
		sectionObj = {
			'date': date,
			'matches': matchList
		}
		upcomingMatchesList.append(sectionObj)
print('********* PROXIMAS PARTIDAS ******************')
print(upcomingMatchesList)

driver.close()