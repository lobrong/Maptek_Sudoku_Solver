from board import Board

def main():
	failures = 0
	emptyBoardString = '---------\n---------\n---------\n---------\n---------\n---------\n---------\n---------\n---------'

	# Invalid board string (row)
	testNumber = 1
	print 'TEST {}: Invalid Board String (row invalid)'.format(testNumber)
	boardString = '223456789\n234567891\n345678912\n456789123\n567891234\n678912345\n789123456\n891234567\n912345678'
	try:
		toSolve = Board(boardString)
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;
	except:
		pass

	# Invalid board string (col)
	testNumber = testNumber + 1
	print 'TEST {}: Invalid Board String (col invalid)'.format(testNumber)
	boardString = '123456789\n134567891\n345678912\n456789123\n567891234\n678912345\n789123456\n891234567\n912345678'
	try:
		toSolve = Board(boardString)
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;
	except:
		pass

	# valid board string
	testNumber = testNumber + 1
	print 'TEST {}: Valid Board String'.format(testNumber)
	boardString = '835416927\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'
	toSolve = Board(boardString)

	if not toSolve.isValid():
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# test solver missing one number
	testNumber = testNumber + 1
	print 'TEST {}: solve for one number'.format(testNumber)
	boardString = '-35416927\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'
	toSolve = Board(boardString)

	options = toSolve.getOptions(0, 0)

	if options != ['8']:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# get one missing options
	testNumber = testNumber + 1
	print 'TEST {}: get all missing options'.format(testNumber)
	toSolve = Board(emptyBoardString)

	options = toSolve.getOptions(0, 0)

	if options != ['1','2','3','4','5','6','7','8','9']:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test setIndex
	testNumber = testNumber + 1
	print 'TEST {}: setIndex'.format(testNumber)
	toSolve = Board(emptyBoardString)
	options = toSolve.setIndex(0, 0, 1)
	if toSolve.getIndex(0, 0) != '1':
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test setIndex
	testNumber = testNumber + 1
	print 'TEST {}: validateArrayOfNumbers'.format(testNumber)
	toSolve = Board(emptyBoardString)
	
	result = toSolve.validateArrayOfNumbers(['1','1'])
	if result == True:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test setIndex
	testNumber = testNumber + 1
	print 'TEST {}: validateArrayOfNumbers'.format(testNumber)
	toSolve = Board(emptyBoardString)
	result = toSolve.validateArrayOfNumbers(['1','2'])
	if result == False:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test getMiniSquare
	testNumber = testNumber + 1
	print 'TEST {}: getMiniSquare'.format(testNumber)
	boardString = '---------\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'
	toSolve = Board(boardString)
	
	result = toSolve.getContainingMiniSquare(3, 3)
	if result != ['1','3','4','6','7','8','5','2','9']:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test findNextCellToTry
	testNumber = testNumber + 1
	print 'TEST {}: findNextCellToTry'.format(testNumber)
	boardString = '---------\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'
	toSolve = Board(boardString)
	
	xToTry, yToTry = toSolve.findNextCellToTry()
	if xToTry != 0 or yToTry != 0:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	# -----------------------------------------------------------------------------
	# test canInsertIntoPosition
	testNumber = testNumber + 1
	print 'TEST {}: canInsertIntoPosition'.format(testNumber)
	boardString = '---------\n296857431\n417293658\n569134782\n123678549\n748529163\n652781394\n981345276\n374962815'
	toSolve = Board(boardString)
	
	canInsert = toSolve.canInsertIntoPosition(0, 0, '2')
	if canInsert:
		print 'FAILURE {}'.format(testNumber)
		failures = failures + 1;

	if failures > 0:
		print 'FAILED {}/{} tests'.format(failures, testNumber)
	else:
		print 'Passed {}/{} tests'.format(testNumber, testNumber)

if __name__ == "__main__":
    main()