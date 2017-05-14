from board import Board
import datetime
import sys

def main():
	emptyBoardString = '---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------\n'
	emptyBoardString +='---------'

	easyboardString = '--39--76-\n'
	easyboardString +='-4---6--9\n'
	easyboardString +='6-7-1---4\n'
	easyboardString +='2--67--9-\n'
	easyboardString +='--43-56--\n'
	easyboardString +='-1--49--7\n'
	easyboardString +='7---9-2-1\n'
	easyboardString +='3--2---4-\n'
	easyboardString +='-29--85--'

	oneNumberMissing = '-35416927\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'

	hardBoardString = '--------5\n'
	hardBoardString +='18--549--\n'
	hardBoardString +='-----124-\n'
	hardBoardString +='-----918-\n'
	hardBoardString +='---4-3---\n'
	hardBoardString +='-638-----\n'
	hardBoardString +='-716-----\n'
	hardBoardString +='--297--51\n'
	hardBoardString +='8--------'

	toSolve = Board(emptyBoardString)

	startTime = datetime.datetime.now()
	result = toSolve.solveSudoku()
	endTime = datetime.datetime.now()
	timeDifference = endTime - startTime
	print 'That took', timeDifference
	if result == True:
		print 'SOLVED'
		toSolve.printBoard()
	else:
		print 'Could not solve :('

if __name__ == "__main__":
    main()