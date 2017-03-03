import sys
import random
import copy
import time
inf = 1000000000
hboard = [ [0 for i in range(4)]  for j in range(4) ]
class Player8:
	
	def __init__(self):
		pass

	
	
	def move(self, board, old_move, flag):
		
		if(flag == 'x'):
			opflag = 'o'
		else:
			opflag = 'x'

		cells = board.find_valid_move_cells(old_move)  #get all possible cells in block corresponding to previous move
		if (old_move[0] == -1 and old_move[1] == -1): #our chance
			return (15,0)
		
		else:
			alpha = -100000000
			beta  =  100000000
			bestval = -10000
			bestmove = []
		        backupVal = []	
			backupMove = []
			depth =  2
			temp_board = copy.deepcopy(board)
			cnt = 0
			#print "CELLS-8"
			#for i in cells:
				#print i,
			#print "\n"	
			for i in cells:
				temp_board.update(old_move, i,flag)
				nextmoveVal = self.alpha_beta( temp_board, alpha, beta, depth, False, i,flag,opflag)
				#print "NextMove: ",nextmoveVal
				backupVal.append(nextmoveVal)    #createbackup
				backupMove.append(i)             #createbackup
				cnt += 1 
				temp_board.board_status[i[0]][i[1]] = '-'
				temp_board.block_status[i[0]/4][i[1]/4] = '-'
				if nextmoveVal >= bestval :
					bestval = nextmoveVal
					bestmove = i
		        
			#print "BESTVAL is ",bestval
			#print '\n'
			if bestval == -10000:    #no cell. only 2 cells left in only one left block on board
				mx = backupVal[0]
				for i in range(cnt):
					if backupVal[i] >= mx :
						mx = backupVal[i]
						bestmove = backupMove[i]
						
					
			return bestmove
	
	
	def boardheuristic_func(self,temp_board,flag,opflag):
		cntp = [ [ 0 for i in range(4)] for j in range(4) ]
		cnto = [ [ 0 for i in range(4)] for j in range(4) ] 
		for i in range(0, 16):
			for j in range(0, 16):
				if temp_board.board_status[i][j] == flag :
					cntp[i/4][j/4] += 1
				elif temp_board.board_status[i][j] == opflag:
					cnto[i/4][j/4] += 1
		
		for i in range(0,4):
			for j in range(0,4):
				hboard[i][j] = 100*cntp[i][j] - 1000*cnto[i][j]
				
				
					

	def heuristic_func(self, temp_board, old_move,flag,opflag) :
		
		x = old_move[0]/4
		y = old_move[1]/4
		
	
		x0 = 4*x + 0
		x1 = 4*x + 1
		x2 = 4*x + 2
		x3 = 4*x + 3
		y0 = 4*y + 0
		y1 = 4*y + 1
		y2 = 4*y + 2
		y3 = 4*y + 3

		hrow = hcol = hdiag1 = hdiag2 = 0
		hfinal = 0
		
		tb = temp_board.board_status



		for i in range(4*x, 4*x + 4) :      #rowsum
			cnt_x = 0
			cnt_o = 0
			for j in range(4*y, 4*y + 4):
				if(tb[i][j] == flag):
					cnt_x += 1
					
				elif(tb[i][j] == opflag):
					cnt_o += 1
					
						
			if(cnt_x == 4 and cnt_o == 0): #x wins
				hfinal = hrow = 1000
				break
			elif(cnt_x == 3 and cnt_o == 0):
				hrow += 100
			elif(cnt_x == 2 and cnt_o == 0):
				hrow += 10
			elif(cnt_x == 1 and cnt_o == 0):
				hrow += 1
			
			elif(cnt_x == 0 and cnt_o == 1):
				hrow += -1
			elif(cnt_x == 0 and cnt_o == 2):
				hrow += -10
			elif(cnt_x == 0 and cnt_o == 3):
				hrow += -100
			elif(cnt_x == 0 and cnt_o == 4): #x loses. 
				hfinal = hrow = -1000
				break
			else :
				hrow += 0
			
					 
		for i in range(y0, y0 + 4):        #colsum
			cnt_x = 0
			cnt_o = 0
			for j in range(4*x, 4*x + 4):
				if(tb[j][i] == flag):
					cnt_x += 1
				elif(tb[i][j] == opflag):
					cnt_o += 1
					
					
			if(cnt_x == 4 and cnt_o == 0): #x wins
				hfinal = hcol = 1000
				break
			elif(cnt_x == 3 and cnt_o == 0):
				hcol += 100
			elif(cnt_x == 2 and cnt_o == 0):
				hcol += 10
			elif(cnt_x == 1 and cnt_o == 0):
				hcol += 1
			
			elif(cnt_x == 0 and cnt_o == 1):
				hcol += -1
			elif(cnt_x == 0 and cnt_o == 2):
				hcol += -10
			elif(cnt_x == 0 and cnt_o == 3):
				hcol += -100
			elif(cnt_x == 0 and cnt_o == 4): #x loses. 
				hfinal = hcol = -1000
				break
			else :
				hcol += 0


		cnt_x = cnt_o = 0		
		p = x0
		q = y0
		for i in range(4*x, 4*x + 4) :
			for j in range(4*y, 4*y + 4):
				if (i == p and j == q):                   #main diagonal
					if(tb[i][j] == flag):
						cnt_x += 1
					elif(tb[i][j] == opflag):
						cnt_o += 1
			p += 1
			q += 1   
		
		if(cnt_x == 4 and cnt_o == 0):   #x wins
			hfinal = hdiag1 = 1000
		elif(cnt_x == 3 and cnt_o == 0):
			hdiag1 += 100
		elif(cnt_x == 2 and cnt_o == 0):
			hdiag1 += 10
		elif(cnt_x == 1 and cnt_o == 0):
			hdiag1 += 1
		elif(cnt_x == 0 and cnt_o == 1):
			hdiag1 += -1
		elif(cnt_x == 0 and cnt_o == 2):
			hdiag1 += -10
		elif(cnt_x == 0 and cnt_o == 3):
			hdiag1 += -100
		elif(cnt_x == 0 and cnt_o == 4):  #x loses
			hfinal = -1000
			hdiag1 = -1000
		




		cnt_x = cnt_o = 0		
		p = x0
		q = y3
		for i in range(4*x, 4*x + 4):
			for j in range(4*y, 4*y + 4):
				if (i == p and j == q ):         #2nd diagonal
					if(tb[i][j] == flag):
						cnt_x += 1
					elif(tb[i][j] == opflag):
						cnt_o += 1
			p += 1
			q -= 1   

		if(cnt_x == 4 and cnt_o == 0):   #x wins
			hfinal = 1000
			hdiag2 = 1000
		elif(cnt_x == 3 and cnt_o == 0):
			hdiag2 += 100
		elif(cnt_x == 2 and cnt_o == 0):
			hdiag2 += 10
		elif(cnt_x == 1 and cnt_o == 0):
			hdiag2 += 1
		elif(cnt_x == 0 and cnt_o == 1):
			hdiag2 += -1
		elif(cnt_x == 0 and cnt_o == 2):
			hdiag2 += -10
		elif(cnt_x == 0 and cnt_o == 3):
			hdiag2 += -100
		elif(cnt_x == 0 and cnt_o == 4):  #x loses
			hfinal = -1000
			hdiag2 = -1000
			

	
		if (hfinal == 1000 or hfinal == -1000):
			#print "hfinal ",hfinal,"move: ",old_move
			return hfinal
			
		else :
			hsum = hrow + hcol + hdiag1 + hdiag2
			#print "hsum ",hsum,"move: ",old_move
			return hsum


	
			
			
	def alpha_beta(self, temp_board, alpha, beta, depth, ismax, old_move,flag,opflag):
			

		par = self.heuristic_func(temp_board, old_move, flag, opflag)
		
		if (depth == 0) :
		
			#par = self.heuristic_func(temp_board, old_move, flag, opflag)
			#print "par ",par
			return par

		if ( ismax == True) : #Maximiser
			
			bestval = -100000000
			cells = temp_board.find_valid_move_cells(old_move)  #get all possible cells in block corresponding to previous move
			
			
			for i in cells :
				
				temp_board.update(old_move, i, flag)
				val = self.alpha_beta(temp_board, alpha, beta, depth-1, False, i,flag,opflag)
				#print "valmax is: ",val,"depth is: ",depth
				#print "bestval: ",bestval,i
				
				temp_board.board_status[i[0]][i[1]] = '-'
				temp_board.block_status[i[0]/4][i[1]/4] = '-'
				
				bestval = max( bestval, val)
				alpha   = max( alpha, bestval)
				if ( beta <= alpha) :
					break



			return bestval/5.0 + par 		
					 

		else : #Minimiser
			
			bestval = 100000000
			cells = temp_board.find_valid_move_cells(old_move)  #get all possible cells in block corresponding to previous move
			for i in cells :
				
				temp_board.update(old_move, i,opflag)
				val = self.alpha_beta(temp_board, alpha, beta, depth-1, True, i,flag,opflag)
				#print "valmin is: ",val,"depth is: ",depth
				#print "bestval: ",bestval,i
				
				temp_board.board_status[i[0]][i[1]] = '-'
				temp_board.block_status[i[0]/4][i[1]/4] = '-'
				
				bestval = min( bestval, val)
				beta    = min( beta, bestval)
				if( beta <= alpha ):
					break


			return bestval/5.0 + par		

			
				
				
			


			
			




			 

			

















