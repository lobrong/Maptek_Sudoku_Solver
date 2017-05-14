validNumbers = ['1','2','3','4','5','6','7','8','9'];
EMPTY = '-'

class Board():
	board = []

	def __init__(self, boardString):
		self.board = self.parseBoardString(boardString)

		if not self.isValid():
			raise 'Invalid board state'

	def parseBoardString(self, board):
		# Validation (length 9)
		rows = board.split('\n')
		newRows = []
		for row in rows:
			newRows.append(list(row))
		return newRows;

	def getBoardString(self):
		boardString = ''
		for row in self.board:
			for cell in row:
				boardString += cell;
			boardString += '\n'
		return boardString

	def getRow(self, rowIndex):
		return self.board[rowIndex]

	def getColumn(self, colIndex):
		column = [];
		for x in range(0, 9):
			column.append(self.getIndex(x, colIndex))
		return column;

	def getIndex(self, xIndex, yIndex):
		return self.board[xIndex][yIndex]

	def setIndex(self, xIndex, yIndex, newValue):
		currentValue = self.getIndex(xIndex, yIndex)
		if not self.isEmpty(currentValue):
			if not self.isEmpty(newValue):
				raise 'trying to get already set position {} {} {} {}'.format(currentValue, xIndex, yIndex, newValue)

		self.board[xIndex][yIndex] = str(newValue)

	def getMiniSquare(self, xIndex, yIndex):
		# Validation 0 - 2
		aggregator = []
		for x in range((xIndex * 3), ((xIndex * 3) + 3)):
			for y in range((yIndex * 3), (yIndex * 3) + 3):
				aggregator.append(self.getIndex(x, y))
		return aggregator

	def validateArrayOfNumbers(self, numbers):
		# Validation numbers are an array
		numberAlreadyCountedInRow = {}
		for cell in numbers:
			if numberAlreadyCountedInRow.get(cell) != None and not self.isEmpty(cell):
				return False
			numberAlreadyCountedInRow[cell] = 'exists'
		return True

	def isEmpty(self, toCheck):
		return str(toCheck) == EMPTY

	def isValid(self):
		for row in self.board:
			valid = self.validateArrayOfNumbers(row)
			if not valid:
				return False

		for number in range(0, 9):
			column = self.getColumn(number)
			valid = self.validateArrayOfNumbers(column)
			if not valid:
				return False

		for x in range(0, 3):
			for y in range(0, 3):
				miniSquareToCheck = self.getMiniSquare(x, y)
				valid = self.validateArrayOfNumbers(miniSquareToCheck)
				if not valid:
					return False
		return True;

	def printBoard(self):
		for x in range(0, 9):
			row = self.getRow(x)
			print '{}{}{}-{}{}{}-{}{}{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

	def getContainingMiniSquare(self, xIndex, yIndex):
		return self.getMiniSquare(int((xIndex/3)), int((yIndex/3)))

	def getOptions(self, xIndex, yIndex):
		currentValue = self.getIndex(xIndex, yIndex)
		if not self.isEmpty(currentValue):
			return None

		options = ['1','2','3','4','5','6','7','8','9']
		row = self.getRow(xIndex)
		col = self.getColumn(yIndex)
		miniSquare = self.getContainingMiniSquare(xIndex, yIndex)

		alreadyUsedNumbers = row + col + miniSquare

		for usedNumber in alreadyUsedNumbers:
			if usedNumber in options:
				options.remove(usedNumber)

		return options

	def findNextCellToTry(self):
		for x in range(0, 9):
			for y in range(0, 9):
				if self.isEmpty(self.getIndex(x, y)):
					return x,y
		return None, None

	def canInsertIntoPosition(self, i, j, newValue):
		if newValue in self.getRow(i):
			return False

		if newValue in self.getColumn(j):
			return False

		if newValue in self.getContainingMiniSquare(i, j):
			return False

		return True


	def solveSudoku(self):
		x,y = self.findNextCellToTry()
		if x is None:
			return True

		for option in self.getOptions(x, y):
			if self.canInsertIntoPosition(x, y, option):
				self.setIndex(x, y, option)
				if self.solveSudoku():
					return True

				# Didnt work, backtrack time
				self.setIndex(x, y, '-')
		return False
