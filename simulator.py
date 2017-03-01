import sys
import random
import signal
import time
import copy

class TimedOutExc(Exception):
	pass

def handler(signum, frame):
	#print 'Signal handler called with signal', signum
	raise TimedOutExc()

class Random_Player():
	def __init__(self):
		pass

	def move(self, board, old_move, flag):
		#You have to implement the move function with the same signature as this
		#Find the list of valid cells allowed
		cells = board.find_valid_move_cells(old_move)
		return cells[random.randrange(len(cells))]


class player14:
	def __init__(self):
		pass

	def Winning_Heuristic(self, board, flag):
		game_state, message = self.terminal_state_reached(board)

		if game_state == True:
			if message != 'D':
				return 100000 if flag ==1 else -100000
			else:
				return 0

		start_row, start_col, ret = 0,0,0

		if flag == 0:
			flag, opponent_flag = 'x', 'o'
		else:
			flag, opponent_flag = 'o', 'x'

		POSSIBLE_WIN_SEQUENCES = [(0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15),  (0,4,5,12), (1,5,9,13), (2,6,10,14), (3,7,11,15), (0,5,10,15), (3,6,9,12) ]

		for seq in POSSIBLE_WIN_SEQUENCES:
			temp_seq = [board.block_status[index/4][index%4] for index in seq if board.block_status[index/4][index%4] != '-' and board.block_status[index/4][index%4] != 'd']

			if flag in temp_seq:
			    if opponent_flag in temp_seq:
					continue
			    if len(temp_seq) > 1:
					ret+=7
			    ret+=1
			elif opponent_flag in temp_seq:
				if len(temp_seq) > 1:
					ret-=7
				ret-=1
		ret = ret *23


		for i in xrange(16):
			if board.block_status[i/4][i%4] == 'd':
				start_col = (start_col + 4) % 16
				if start_col == 0:
					start_row += 4
				continue
			elif board.block_status[i/4][i%4] == '-':
				temp_block = [ row[start_row:start_row + 4] for row in board.board_status[start_col:start_col+4] ]

				for seq in POSSIBLE_WIN_SEQUENCES:
					temp_seq =  [board.board_status[index/4][index%4] for index in seq if board.board_status[index/4][index%4] != '-']
					if flag in temp_seq:
						if opponent_flag in temp_seq:
							continue
						if len(temp_seq) > 1:
							ret += 7
						ret += 1
					elif opponent_flag in temp_seq:
						if len(temp_seq) > 1:
							ret -= 7
						ret -=1
			elif flag == board.block_status[i/4][i%4]:
				ret +=8
			else:
				ret -=8


			start_col = (start_col + 4) % 16
			if start_col == 0:
				start_row += 4

		return ret

	def get_empty_cells(self, board, bla1):
		cells = [] #list of tuples that are allowed
		#Iterate over all the blocks that are possible, in this case it is only 1 and get all the empty cells
		for x in bla1:
			id1 = x/4
			id2 = x%4

			for i in xrange(id1*4, id1*4 + 4):
				for j in xrange(id2*4, id2*4 + 4):
					if board.board_status[i][j] == '-':
						cells.append((i,j))
		#Or else if all the blocks are full, move anywhere
		if cells == []:
			for i in range(16):
				for j in range(16):
					no = (i/4)*4 + j/4
					if board.board_status == '-' and board.block_status[no/4][no%4] == '-':
						cells.append((i,j))
		return cells


	def get_blocks(self, board, old_move):
		cells=  board.find_valid_move_cells(old_move)
		print "hooo"
		print cells
		return cells

	def terminal_state_reached(self, board):
		#CHECK ROW WIN
		if ((board.block_status[(0/4)][0%4]== board.block_status[1/4][1%4] and board.block_status[1/4][1%4]==board.block_status[2/4][2%4] and board.block_status[2/4][2%4]==board.block_status[3/4][3%4] and board.block_status[1/4][1%4]!='-' and board.block_status[1/4][1%4]!='d') or (board.block_status[4/4][4%4]== board.block_status[5/4][5%4] and board.block_status[5/4][5%4]==board.block_status[6/4][6%4] and board.block_status[6/4][6%4]==board.block_status[7/4][7%4] and board.block_status[4/4][4%4]!='-' and board.block_status[4/4][4%4]!='d') or (board.block_status[8/4][8%4]== board.block_status[9/4][9%4] and board.block_status[9/4][9%4]==board.block_status[10/4][10%4] and board.block_status[10/4][10%4]==board.block_status[11/4][11%4] and board.block_status[8/4][8%4]!='-' and board.block_status[8/4][8%4]!='d') or (board.block_status[12/4][12%4]== board.block_status[13/4][13%4] and board.block_status[13/4][13%4]==board.block_status[14/4][14%4] and board.block_status[14/4][14%4]==board.block_status[15/4][15%4] and board.block_status[12/4][12%4]!='-' and board.block_status[12/4][12%4]!='d')):

			return True, 'W'


		#Check col win
		elif (board.block_status[0/4][0%4]== board.block_status[4/4][4%4] and board.block_status[4/4][4%4]==board.block_status[8/4][8%4] and board.block_status[8/4][8%4]==board.block_status[12/4][12%4] and board.block_status[0/4][0%4]!='-' and board.block_status[0/4][0%4]!='d') or (board.block_status[1/4][1%4]== board.block_status[5/4][5%4] and board.block_status[5/4][5%4]==board.block_status[9/4][9%4] and board.block_status[9/4][9%4]==board.block_status[13/4][13%4] and board.block_status[1/4][1%4]!='-' and board.block_status[1/4][1%4]!='d') or (board.block_status[2/4][2%4]== board.block_status[6/4][6%4] and board.block_status[6/4][6%4]==board.block_status[10/4][10%4] and board.block_status[10/4][10%4]==board.block_status[14/4][14%4] and board.block_status[2/4][2%4]!='-' and board.block_status[2/4][2%4]!='d') or (board.block_status[3/4][3%4]== board.block_status[7/4][7%4] and board.block_status[7/4][7%4]==board.block_status[11/4][11%4] and board.block_status[11/4][11%4]==board.block_status[15/4][15%4] and board.block_status[3/4][3%4]!='-' and board.block_status[3/4][3%4]!='d'):

			return True, 'W'

		#Check diagonal win
		elif (board.block_status[0/4][0%4]== board.block_status[5/4][5%4] and board.block_status[5/4][5%4]==board.block_status[10/4][10%4] and board.block_status[10/4][10%4]==board.block_status[15/4][15%4] and board.block_status[0/4][0%4]!='-' and board.block_status[0/4][0%4]!='d') or (board.block_status[3/4][3%4]== board.block_status[6/4][6%4] and board.block_status[6/4][6%4]==board.block_status[9/4][9%4] and board.block_status[9/4][9%4]==board.block_status[12/4][12%4] and board.block_status[3/4][3%4]!='-' and board.block_status[3/4][3%4]!='d'):

			return True, 'W'

		else:
			smflag=0
			for i in xrange(9):
				for j in xrange(9):
					if board.board_status[i][j] == '-' and board.block_status[((i/4)*4 + (j/4))/4][((i/4)*4 + (j/4))%4] == '-':
						smflag =1
						break

			if smflag == 1:
			#GAME IS ON BRO
				return False, 'Continue'
			else:
				return False, 'Tie'


	def update_overall_board(self, board, move_ret, fl ):
		#check if we need to modify block_stat

		block_no = (move_ret[0]/4)*4 + move_ret[1]/4
		updated_block, id1,id2, mflg = -1, block_no/4, block_no%4, 0
		print 'whgooo'
		print board.board_status
		if board.block_status[block_no/4][block_no%4] == '-':
			if board.board_status[id1*4][id2*4] == board.board_status[id1*4+1][id2*4+1] and board.board_status[id1*4+1][id2*4+1] == board.board_status[id1*4+2][id2*4+2] and board.board_status[id1*4+2][id2*4+2] == board.board_status[id1*4+3][id2*4+3] and  board.board_status[id1*4+1][id2*4+1] != '-':
				mflg=1
			if board.board_status[id1*4+3][id2*4] == board.board_status[id1*4+2][id2*4+1] and board.board_status[id1*4+2][id2*4+1] == board.board_status[id1*4+1][id2*4+2] and board.board_status[id1*4+1][id2*4+2] == board.board_status[id1*4][id2*4+3] and board.board_status[id1*4+3][id2*4] != '-':
				mflg=1
			print "mfg"
			print mflg
			if mflg !=1:
				print 'kaska'
				for i in range(id2*4, id2*4 + 4):
					print 'drooska'
					if board.board_status[id1*4][i] == board.board_status[id1*4 + 1][i] and board.board_status[id1*4 + 1][i] ==board.board_status[id1*4+2][i] and board.board_status[id1*4 + 2][i]==board.board_status[id1*4 + 3][i] and board.board_status[id1*4][i]!= '-':
						mflg = 1
						break

			#rowise check for flag
			if mflg !=1:
				for i in range(id1*4, id1*4 + 4):
					if board.board_status[i][id2*4] == board.board_status[i][id2*4 + 1] and board.board_status[i][id2*4 + 1] ==board.board_status[i][id2*4+2] and board.board_status[i][id2*4 + 2]==board.board_status[i][id2*4 + 3] and board.board_status[i][id2*4]!= '-':
						mflg = 1
						print "bazooak"
						break
		
		print "taa"
		if mflg == 1:
			board.block_status[block_no/4][block_no%4] =  fl
			updated_block = block_no
			return [board.block_status, updated_block]

		#check for draw on the block if not modified

		flag = 0
		print "holalala"
		for i in xrange(id1*4, id1*4 + 4):
			for i in  xrange(id2*4, id2*4 + 4):
				if board.board_status[i][j] == '-':
					flag = 1
					break
		if flag == 0:
			#draw
			board.block_status[block_no/4][block_no%4], updated_block ='d', block_no
		xooxa =  [board.block_status, updated_block]
		print "xooxa"
		return xooxa


	def alpha_beta_pruning(self, board, old_move, alpha, beta, flag , depth):
		if(depth ==  4):
			'''
				Heuristic
			'''
			return [old_move[0], old_move[1], self.Winning_Heuristic(board, flag)]
		print "geee"
		coords = self.get_blocks(board, old_move)
		print coords 
		if (flag == 1):
			symbol = 'o'
		else:
			symbol = 'x'

		print "jjas"
		if depth%2 == 0:
			''' Max Node '''
			max_list = [-1, -1 , -100000]
			for i in coords:
				a, b = i
				print "a b "
				print a, b
				print board.board_status
				board.board_status[a][b] = symbol
				print board.board_status[a][b]
				board.block_status , updated_block = self.update_overall_board(board,(a,b),symbol)
				print "hahaha"
				print board.block_status
				game_state, message =  self.terminal_state_reached(board)

				if game_state:
					board.board_status[a][b]='-'
					if updated_block != -1:
						board.block_status[updated_block/4][updated_block%4] = '-'
					return [a, b, 10000]

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1)

				if(val[2] > max_list[2]):
					max_list[0], max_list[1], max_list[2] =a , b , val[2];

				alpha = max(alpha, max_list[2])
				board.board_status[a][b] = '-'

				if updated_block != -1:
					board.block_status[updated_block/4][updated_block%4] = '-'

				if (beta <= alpha):
					break
			print max_list
			return max_list
		else:
			'''Min Node '''

			min_list = [-1, -1, 100000]
			for i in coords:
				a, b = i

				board.board_status[a][b] = symbol

				board.block_status , updated_block = self.update_overall_board(board,(a,b),symbol)
				game_state, message =  self.terminal_state_reached(board)

				if game_state:
					board.board_status[a][b]='-'
					if updated_block != -1:
						board.block_status[updated_block/4][updated_block%4] = '-'
					return [a, b, -10000]

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1)

				if(val[2] <= min_list[2]):
					min_list[0], min_list[1], min_list[2] =a , b , val[2];

				beta = min(beta, min_list[2])
				board.board_status[a][b] = '-'

				# STAAAAAAAR CHANGE, because this is list, and we have a 2d array

				if updated_block != -1:
					board.block_status[updated_block/4][updated_block%4] = '-'

				if (beta <= alpha):
					break

			return min_list



	def move(self, board, old_move, flag):
		if flag == 'x':
			flag=1
		else:
			flag=0

		if (old_move == (-1,-1)):
			coord = (5,0)
			return coord
		coord = tuple(self.alpha_beta_pruning(board, old_move, -10**6-1, 10**6, flag, 0)[0:2])
		print 'Hello'
		print 'Coord is'
		print coord[0]
		print coord[1]
		#if old move is (-1,-1)
		if coord[0] == -1 or coord[0] == -1:
			coords = self.get_blocks(board, old_move)
			print coords
			print "hukkk"
			xy = coords[random.randrange(len(coords))]
			print "xy"
			print xy
			return xy

		#return move
		print "liyiyikykuyuyu"
		print coord
		return coord

class Manual_Player:
	def __init__(self):
		pass
	def move(self, board, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))

class Board:

	def __init__(self):
		# board_status is the game board
		# block status shows which blocks have been won/drawn and by which player
		self.board_status = [['-' for i in range(16)] for j in range(16)] #BIIIG BAORD
		self.block_status = [['-' for i in range(4)] for j in range(4)]  #SAME FOR BOTH CODES

	def print_board(self):
		# for printing the state of the board
		print '==============Board State=============='
		for i in range(16):
			if i%4 == 0:
				print
			for j in range(16):
				if j%4 == 0:
					print "",
				print self.board_status[i][j],
			print
		print

		print '==============Block State=============='
		for i in range(4):  #printing horizontally
			for j in range(4):
				print self.block_status[i][j],
			print
		print '======================================='
		print
		print


	def find_valid_move_cells(self, old_move):
		#returns the valid cells allowed given the last move and the current board state
		allowed_cells = []
		allowed_block = [old_move[0]%4, old_move[1]%4]
		#checks if the move is a free move or not based on the rules

		if old_move != (-1,-1) and self.block_status[allowed_block[0]][allowed_block[1]] == '-':
			for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
				for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
					if self.board_status[i][j] == '-':
						allowed_cells.append((i,j))
		else:
			for i in range(16):
				for j in range(16):
					if self.board_status[i][j] == '-' and self.block_status[i/4][j/4] == '-':
						allowed_cells.append((i,j))
		return allowed_cells

	def find_terminal_state(self):
		#checks if the game is over(won or drawn) and returns the player who have won the game or the player who has higher blocks in case of a draw
		bs = self.block_status

		cntx = 0
		cnto = 0
		cntd = 0

		for i in range(4):						#counts the blocks won by x, o and drawn blocks
			for j in range(4):
				if bs[i][j] == 'x':
					cntx += 1
				if bs[i][j] == 'o':
					cnto += 1
				if bs[i][j] == 'd':
					cntd += 1

		for i in range(4):
			row = bs[i]							#i'th row
			col = [x[i] for x in bs]			#i'th column
			#print row,col
			#checking if i'th row or i'th column has been won or not
			if (row[0] =='x' or row[0] == 'o') and (row.count(row[0]) == 4):
				return (row[0],'WON')
			if (col[0] =='x' or col[0] == 'o') and (col.count(col[0]) == 4):
				return (col[0],'WON')
		#checking if diagnols have been won or not
		if(bs[0][0] == bs[1][1] == bs[2][2] ==bs[3][3]) and (bs[0][0] == 'x' or bs[0][0] == 'o'):
			return (bs[0][0],'WON')
		if(bs[0][3] == bs[1][2] == bs[2][1] ==bs[3][0]) and (bs[0][3] == 'x' or bs[0][3] == 'o'):
			return (bs[0][3],'WON')

		if cntx+cnto+cntd <16:		#if all blocks have not yet been won, continue
			return ('CONTINUE', '-')
		elif cntx+cnto+cntd == 16:							#if game is drawn
			return ('NONE', 'DRAW')

	def check_valid_move(self, old_move, new_move):
		#checks if a move is valid or not given the last move
		if (len(old_move) != 2) or (len(new_move) != 2):
			return False
		if (type(old_move[0]) is not int) or (type(old_move[1]) is not int) or (type(new_move[0]) is not int) or (type(new_move[1]) is not int):
			return False
		if (old_move != (-1,-1)) and (old_move[0] < 0 or old_move[0] > 16 or old_move[1] < 0 or old_move[1] > 16):
			return False
		cells = self.find_valid_move_cells(old_move)
		return new_move in cells

	def update(self, old_move, new_move, ply):
		#updating the game board and block status as per the move that has been passed in the arguements
		if(self.check_valid_move(old_move, new_move)) == False:
			return 'UNSUCCESSFUL'
		self.board_status[new_move[0]][new_move[1]] = ply

		x = new_move[0]/4
		y = new_move[1]/4
		fl = 0
		bs = self.board_status
		#checking if a block has been won or drawn or not after the current move
		for i in range(4):
			#checking for horizontal pattern(i'th row)
			if (bs[4*x+i][4*y] == bs[4*x+i][4*y+1] == bs[4*x+i][4*y+2] == bs[4*x+i][4*y+3]) and (bs[4*x+i][4*y] == ply):
				self.block_status[x][y] = ply
				return 'SUCCESSFUL'
			#checking for vertical pattern(i'th column)
			if (bs[4*x][4*y+i] == bs[4*x+1][4*y+i] == bs[4*x+2][4*y+i] == bs[4*x+3][4*y+i]) and (bs[4*x][4*y+i] == ply):
				self.block_status[x][y] = ply
				return 'SUCCESSFUL'

		#checking for diagnol pattern
		if (bs[4*x][4*y] == bs[4*x+1][4*y+1] == bs[4*x+2][4*y+2] == bs[4*x+3][4*y+3]) and (bs[4*x][4*y] == ply):
			self.block_status[x][y] = ply
			return 'SUCCESSFUL'
		if (bs[4*x+3][4*y] == bs[4*x+2][4*y+1] == bs[4*x+1][4*y+2] == bs[4*x][4*y+3]) and (bs[4*x+3][4*y] == ply):
			self.block_status[x][y] = ply
			return 'SUCCESSFUL'

		#checking if a block has any more cells left or has it been drawn
		for i in range(4):
			for j in range(4):
				if bs[4*x+i][4*y+j] =='-':
					return 'SUCCESSFUL'
		self.block_status[x][y] = 'd'
		return 'SUCCESSFUL'

def gameplay(obj1, obj2):				#game simulator
	game_board = Board() #Equivalent: 	game_board, block_stat = get_init_board_and_blockstatus()

	fl1 = 'x'
	fl2 = 'o'
	old_move = (-1,-1)
	WINNER = ''
	MESSAGE = ''
	TIME = 15
	pts1 = 0
	pts2 = 0

	game_board.print_board()
	signal.signal(signal.SIGALRM, handler)
	while(1):
		#player 1 turn
		temp_board_status = copy.deepcopy(game_board.board_status)
		temp_block_status = copy.deepcopy(game_board.block_status)
		signal.alarm(TIME)

		try:									#try to get player 1's move
			p1_move = obj1.move(game_board, old_move, fl1)

			print "p1 ka move is " 
			print p1_move
		except TimedOutExc:					#timeout error
#			print e
			WINNER = 'P2'
			MESSAGE = 'TIME OUT'
			pts2 = 16
			break
		except Exception as e:
			WINNER = 'P2'
			MESSAGE = 'INVALID MOVE'
			pts2 = 16
			break
		signal.alarm(0)

		#check if board is not modified and move returned is valid
		if (game_board.block_status != temp_block_status) or (game_board.board_status != temp_board_status):
			WINNER = 'P2'
			MESSAGE = 'MODIFIED THE BOARD'
			pts2 = 16
			break
		if game_board.update(old_move, p1_move, fl1) == 'UNSUCCESSFUL':
			WINNER = 'P2'
			MESSAGE = 'INVALID MOVE'
			pts2 = 16
			break

		status = game_board.find_terminal_state()		#find if the game has ended and if yes, find the winner
		print status
		if status[1] == 'WON':							#if the game has ended after a player1 move, player 1 would win
			pts1 = 16
			WINNER = 'P1'
			MESSAGE = 'WON'
			break
		elif status[1] == 'DRAW':						#in case of a draw, each player gets points equal to the number of blocks won
			WINNER = 'NONE'
			MESSAGE = 'DRAW'
			break

		old_move = p1_move
		game_board.print_board()

		#do the same thing for player 2
		temp_board_status = copy.deepcopy(game_board.board_status)
		temp_block_status = copy.deepcopy(game_board.block_status)
		signal.alarm(TIME)

		try:
			p2_move = obj2.move(game_board, old_move, fl2)
		except TimedOutExc:
			WINNER = 'P1'
			MESSAGE = 'TIME OUT'
			pts1 = 16
			break
		except Exception as e:
			WINNER = 'P1'
			MESSAGE = 'INVALID MOVE'
			pts1 = 16
			break
		signal.alarm(0)
		if (game_board.block_status != temp_block_status) or (game_board.board_status != temp_board_status):
			WINNER = 'P1'
			MESSAGE = 'MODIFIED THE BOARD'
			pts1 = 16
			break
		if game_board.update(old_move, p2_move, fl2) == 'UNSUCCESSFUL':
			WINNER = 'P1'
			MESSAGE = 'INVALID MOVE'
			pts1 = 16
			break

		status = game_board.find_terminal_state()	#find if the game has ended and if yes, find the winner
		print status
		if status[1] == 'WON':						#if the game has ended after a player move, player 2 would win
			pts2 = 16
			WINNER = 'P2'
			MESSAGE = 'WON'
			break
		elif status[1] == 'DRAW':
			WINNER = 'NONE'
			MESSAGE = 'DRAW'
			break
		game_board.print_board()
		old_move = p2_move

	game_board.print_board()

	print "Winner:", WINNER
	print "Message", MESSAGE

	x = 0
	d = 0
	o = 0
	for i in range(4):
		for j in range(4):
			if game_board.block_status[i][j] == 'x':
				x += 1
			if game_board.block_status[i][j] == 'o':
				o += 1
			if game_board.block_status[i][j] == 'd':
				d += 1
	print 'x:', x, ' o:',o,' d:',d
	if MESSAGE == 'DRAW':
		pts1 = x
		pts2 = o
	return (pts1,pts2)



if __name__ == '__main__':

	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)

	obj1 = ''
	obj2 = ''
	option = sys.argv[1]
	if option == '1':
		obj1 = Random_Player()
		obj2 = Random_Player()

	elif option == '2':
		obj1 = player14()
		obj2 = Random_Player()
	elif option == '3':
		obj1 = Manual_Player()
		obj2 = Manual_Player()
	else:
		print 'Invalid option'
		sys.exit(1)

	x = gameplay(obj1, obj2)
	print "Player 1 points:", x[0]
	print "Player 2 points:", x[1]
