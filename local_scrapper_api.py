from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://www.hltv.org/matches/#")

@app.route('/')
def init():
	return {
		'msg':'Welcome to CSGO matches API !!'
	}

@app.route('/allmatches')
def notFormMatches():
	
	#access HLTV page
	teamNames = driver.find_elements_by_class_name('matchTeamName')
	matchesList = []
	
	for team in range(len(teamNames)):
		if(team%2 == 1):
			matchesObj = {}
			matchesObj = {
				'team1': teamNames[team - 1].text ,
				'team2': teamNames[team].text
			}
			matchesList.append(matchesObj)
	return {
		'Matches': matchesList
	}
@app.route('/live_matches')
def liveMatches():
	#choose webdriver

	#access HLTV page

	#check live matches
	liveMatchesElement = driver.find_element_by_class_name('liveMatchesContainer')
	teamNames = liveMatchesElement.find_elements_by_class_name('matchTeamName')
	matchesObj = {}
	liveMatchesList = []
	for team in range(len(teamNames)):
		if(team%2 == 1):
			matchesObj = {
				'team1': teamNames[team - 1].text ,
				'team2': teamNames[team].text
			}
			liveMatchesList.append(matchesObj)
			matchesObj = {}
	return {
		'live': liveMatchesList
	}
@app.route('/upcoming_matches')
def upcomingMatches():
	#choose webdriver
	

	upcomingMatchesElement = driver.find_element_by_class_name('upcomingMatchesContainer')
	upcomingMatchesSectionByDate = upcomingMatchesElement.find_elements_by_class_name('upcomingMatchesSection')


	upcomingMatchesList = []

	#only 3 days
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
	return {
		'matches': upcomingMatchesList
	}




@app.route('/matches')
def allMatches():
	#choose webdriver
	
	#access HLTV page
	#driver.get("https://www.hltv.org/matches/#")

	#check live matches
	liveMatchesElement = driver.find_element_by_class_name('liveMatchesContainer')
	teamNames = liveMatchesElement.find_elements_by_class_name('matchTeamName')
	matchesObj = {}
	liveMatchesList = []
	for team in range(len(teamNames)):
		if(team%2 == 1):
			matchesObj = {
				'team1': teamNames[team - 1].text ,
				'team2': teamNames[team].text
			}
			liveMatchesList.append(matchesObj)
			matchesObj = {}

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

	return {
		'live': liveMatchesList,
		'upcoming': upcomingMatchesList
	}


if __name__ == '__main__':
    app.run(threaded = True ,port = 5000)