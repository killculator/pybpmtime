import sys
import math


def main(args):
	if (len(args) < 2):
		print("provide a value or face my wrath")
	else:
		try:
			int(args[1])
		except ValueError:
			print("enter a number, dingus")

		bpm = int(args[1])
		ms = 60000/bpm
		baseList = [0, 1, 2, 3, 4, 5, 6, 7]

		divisorList = calculateDivisors(baseList)
		msList = calculateTimeInMs(baseList, ms)
		barList = formatBarList(baseList, divisorList, msList)
		printBars(baseList, barList)

def calculateDivisors(valueList):
	returnList = list()
	for item in valueList:
		returnList.append(int(math.pow(2, item)))
	return returnList

def calculateTimeInMs(valueList, timeInMs):
	returnList = list()
	for item in valueList:
		returnList.append(round(timeInMs if (item == 0) else timeInMs/(item * 2), 2))
	return returnList

def formatBarList(valueList, divisorList, timeList):
	returnList = list()
	for item in valueList:
		if (item < 4):
			if (item == 0):
				returnList.append("Bar:       " + str(timeList[item]) + " ms")
			else:
				returnList.append("1/" + str(divisorList[item]) + ":       " + str(timeList[item]) + " ms")
		elif(item < 7):
			returnList.append("1/" + str(divisorList[item]) + ":      " + str(timeList[item]) + " ms")
		else:
			returnList.append("1/" + str(divisorList[item]) + ":     " + str(timeList[item]) + " ms")
	return returnList

def printBars(valueList, barList):
	returnList = list()
	for item in valueList:
		print(barList[item])
	return returnList

if __name__ == "__main__":
	sys.exit(main(sys.argv))
