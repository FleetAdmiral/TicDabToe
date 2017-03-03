import random
import time

class Player14:
	def __init__(self):
		self.init_time = time.time()
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

		POSSIBLE_WIN_SEQUENCES = [(8,9,10,11), (12,13,14,15), (0,1,2,3), (4,5,6,7),  (0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15), (0,5,10,15), (3,6,9,12) ]

		for seq in POSSIBLE_WIN_SEQUENCES:
			temp_seq = [board.block_status[index/4][index%4] for index in seq if board.block_status[index/4][index%4] != '-' and board.block_status[index/4][index%4] != 'd']

			if flag in temp_seq:
			    if opponent_flag in temp_seq:
					#ret-=1
					continue
			    if (len(temp_seq) > 1):
					ret+=55
					if (len(temp_seq))==3:
						ret+=100
			    ret+=1
			elif opponent_flag in temp_seq:
				if len(temp_seq) > 1:
					ret-=7
					if(len(temp_seq) == 3):
						ret-=40
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
							#ret-=1
							continue
						if len(temp_seq) ==2:
							ret += 50
						if len(temp_seq) == 3:
							ret+=100
						ret += 1
					elif opponent_flag in temp_seq:
						if len(temp_seq) == 2:
							ret -= 75
						elif len(temp_seq)==3:
							ret-=125
						ret -=5
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
		#print "hooo"
		#print cells
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
		#print 'whgooo'
		#print board.board_status
		if board.block_status[block_no/4][block_no%4] == '-':
			if board.board_status[id1*4][id2*4] == board.board_status[id1*4+1][id2*4+1] and board.board_status[id1*4+1][id2*4+1] == board.board_status[id1*4+2][id2*4+2] and board.board_status[id1*4+2][id2*4+2] == board.board_status[id1*4+3][id2*4+3] and  board.board_status[id1*4+1][id2*4+1] != '-':
				mflg=1
			if board.board_status[id1*4+3][id2*4] == board.board_status[id1*4+2][id2*4+1] and board.board_status[id1*4+2][id2*4+1] == board.board_status[id1*4+1][id2*4+2] and board.board_status[id1*4+1][id2*4+2] == board.board_status[id1*4][id2*4+3] and board.board_status[id1*4+3][id2*4] != '-':
				mflg=1
			#print "mfg"
			#print mflg
			if mflg !=1:
				#print 'kaska'
				for i in range(id2*4, id2*4 + 4):
					#print 'drooska'
					if board.board_status[id1*4][i] == board.board_status[id1*4 + 1][i] and board.board_status[id1*4 + 1][i] ==board.board_status[id1*4+2][i] and board.board_status[id1*4 + 2][i]==board.board_status[id1*4 + 3][i] and board.board_status[id1*4][i]!= '-':
						mflg = 1
						break

			#rowise check for flag
			if mflg !=1:
				for i in range(id1*4, id1*4 + 4):
					if board.board_status[i][id2*4] == board.board_status[i][id2*4 + 1] and board.board_status[i][id2*4 + 1] ==board.board_status[i][id2*4+2] and board.board_status[i][id2*4 + 2]==board.board_status[i][id2*4 + 3] and board.board_status[i][id2*4]!= '-':
						mflg = 1
						#print "bazooak"
						break

		#print "taa"
		if mflg == 1:
			board.block_status[block_no/4][block_no%4] =  fl
			updated_block = block_no
			return [board.block_status, updated_block]

		#check for draw on the block if not modified

		flag = 0
		#print "holalala"

		for i in range(id1*4, id1*4 + 4):
			for j in  range(id2*4, id2*4 + 4):
				if board.board_status[i][j] == '-':
					flag = 1
					break
		#print "flag hai yeh"
		#print flag
		if flag == 0:
			#draw
			board.block_status[block_no/4][block_no%4], updated_block ='d', block_no
		xooxa =  [board.block_status, updated_block]
		#print "xooxa"
		return xooxa


	def alpha_beta_pruning(self, board, old_move, alpha, beta, flag , depth, fin_depth, init_time):
		now_time = time.time()
		#print "ahaa"
		#print now_time
		#print "Ok"
		#print init_time
		#print "now"
		#print (now_time - init_time)
		#print now_time.seconds - initial_time.seconds
		if((now_time - init_time)>= 13):
			return [-100,100, -100000]
		if(depth ==  fin_depth):
			'''
				Heuristic
			'''
			return [old_move[0], old_move[1], self.Winning_Heuristic(board, flag)]
		#print "geee"
		coords = self.get_blocks(board, old_move)
		random.shuffle(coords)
		#print coords
		if (flag == 1):
			symbol = 'o'
		else:
			symbol = 'x'

		#print "jjas"
		if depth%2 == 0:
			''' Max Node '''
			max_list = [-1, -1 , -100000]
			for i in coords:
				a, b = i
				#print "a b "
				#print a, b
				#print board.board_status
				board.board_status[a][b] = symbol
				#print board.board_status[a][b]
				board.block_status , updated_block = self.update_overall_board(board,(a,b),symbol)
				#print "hahaha"
				#print board.block_status
				game_state, message =  self.terminal_state_reached(board)

				if game_state:
					board.board_status[a][b]='-'
					if updated_block != -1:
						board.block_status[updated_block/4][updated_block%4] = '-'
					return [a, b, 10000]

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1, fin_depth, init_time)

				if(val[2] > max_list[2]):
					max_list[0], max_list[1], max_list[2] =a , b , val[2];

				alpha = max(alpha, max_list[2])
				board.board_status[a][b] = '-'

				if updated_block != -1:
					board.block_status[updated_block/4][updated_block%4] = '-'

				if (beta <= alpha):
					break
			#print max_list
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

				val = self.alpha_beta_pruning(board, (a,b), alpha, beta, flag^1, depth+1, fin_depth, init_time)

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
		init_time = time.time()
		if flag == 'x':
			flag=1
		else:
			flag=0
		#print "oldaa movaa"
		#print old_move
		if (old_move == (-1,-1)):
			coords = board.find_valid_move_cells(old_move)
			return (13,14)
			#return coords[random.randint(0,len(coords))]
		old_coords=[]
		for i in range(1,7):
			coord = tuple(self.alpha_beta_pruning(board, old_move, -10**6-1, 10**6, flag, 0, i, init_time)[0:2])
			if(coord[0]==-100):
				print "Oh no"
				break
			old1_coords = coord
		#print 'Hello'
		#print 'Coord is'
		#print coord[0]
		#print coord[1]
		#if old move is (-1,-1)
		if coord[0] == -1 or coord[0] == -1:
			coords = self.get_blocks(board, old_move)
			#print coords
			#print "hukkk"
			xy = coords[random.randrange(len(coords))]
			#print "xy"
			#print xy
			return xy

		#return move
		#print "liyiyikykuyuyu"
		#print coord
		return old1_coords
