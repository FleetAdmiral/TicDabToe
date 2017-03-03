# 0 -> empty ; 1-> X ; 2->O
#player 1 -1
from __future__ import print_function
import copy
import random
import datetime

INFINITY = 1e10
class Player1:

    def __init__(self):
        self.termVal = 10000000
        self.limit = 5
        self.count = 0
        self.weight = [3,2,2,3,2,3,3,2,2,3,3,2,3,2,2,3]
        self.dict = {'x':1,'o':-1,'-':0,'d':0}
        self.trans = {}
        self.timeLimit = datetime.timedelta(seconds = 14)
        self.begin = INFINITY

    def evaluate(self,board,blx,bly):
        # print("Calculating for block ",blx, " " , bly)
        val = 0
        rowCnt = [3,3,3,3]
        colCnt = [3,3,3,3]
        for i in xrange(4):
            for j in xrange(4):
                mark = board.board_status[4*blx+i][4*bly+j]
                # print("hi")
                dictVal = self.dict[mark]
                if(dictVal!=0):
                    val+=dictVal*self.weight[4*i+j]
                    if (rowCnt[i]==3):
                        rowCnt[i] = dictVal*5
                    elif(dictVal*rowCnt[i]<0):
                        rowCnt[i] = 0
                    rowCnt[i]+=rowCnt[i]
                    if (colCnt[j]==3):
                        colCnt[j] = dictVal*5
                    elif(dictVal*colCnt[j]<0):
                        colCnt[j] = 0
                    colCnt[j]+=colCnt[j]

        for i in xrange(4):
            if(rowCnt[i]!=3):
                val+=rowCnt[i]
            if(colCnt[i]!=3):
                val+=colCnt[i]

        diag1,diag2 = 3,3
        for i in xrange(4):
                mark = board.block_status[i][i]
                dictVal = self.dict[mark]
                if(dictVal!=0):
                    if(diag1==3):
                        diag1 = dictVal*5
                    elif(dictVal*diag1<0):
                        diag1 = 0
                    diag1+=diag1
                mark = board.block_status[i][3-i]
                dictVal = self.dict[mark]
                if(dictVal!=0):
                    if(diag2==3):
                        diag2 = dictVal*5
                    elif(dictVal*diag2<0):
                        diag2 = 0
                    diag2+=diag2

        for i in xrange(4):
            if(diag1!=3):
                val+=diag1
            if(diag2!=3):
                val+=diag2

        # print("val is ",val)
        return val

    def blockEval(self,board):
        val = 0
        rowCnt = [3,3,3,3]
        colCnt = [3,3,3,3]
        for i in xrange(4):
            for j in xrange(4):
                mark = board.block_status[i][j]
                dictVal = self.dict[mark]
                if(mark!='-'):
                    val+=dictVal*self.weight[4*i+j]
                    if (rowCnt[i]==3):
                        rowCnt[i] = dictVal*5
                    elif(dictVal*rowCnt[i]<=0):
                        rowCnt[i] = 0
                    rowCnt[i]+=rowCnt[i]
                    if (colCnt[j]==3):
                        colCnt[j] = dictVal*5
                    elif(dictVal*colCnt[j]<=0):
                        colCnt[j] = 0
                    colCnt[j]+=colCnt[j]

        for i in xrange(4):
            if(rowCnt[i]!=3):
                val+=rowCnt[i]
            if(colCnt[i]!=3):
                val+=colCnt[i]

        diag1,diag2 = 3,3
        for i in xrange(4):
                mark = board.block_status[i][i]
                if(mark!='-'):
                    dictVal = self.dict[mark]
                    if(diag1==3):
                        diag1 = dictVal*5
                    elif(dictVal*diag1<=0):
                        diag1 = 0
                    diag1+=diag1
                mark = board.block_status[i][3-i]
                if(mark!='-'):
                    dictVal = self.dict[mark]
                    if(diag2==3):
                        diag2 = dictVal*5
                    elif(dictVal*diag2<0):
                        diag2 = 0
                    diag2+=diag2*dictVal*dictVal

        for i in xrange(4):
            if(diag1!=3):
                val+=diag1
            if(diag2!=3):
                val+=diag2

        # print("val is ",val)
        return val

    def heuristic(self, board):
        final = 0
        # print("Calculating heur")
        for i in xrange(4):
            for j in xrange(4):
                final += self.evaluate(board,i,j)
        final += self.blockEval(board)*15
        # return (50, old_move)
        # print("final is ",final)
        return final

    def alphaBeta(self, board, old_move, flag, depth, alpha, beta):
        # Assuming 'x' to be the maximising player
        hashval = hash(str(board.board_status))
        if(self.trans.has_key(hashval)):
            # print("hash exists")
            bounds = self.trans[hashval]
            if(bounds[0] >= beta):
                return bounds[0],old_move
            if(bounds[1] <= alpha):
                return bounds[1],old_move
            # print("also returning")
            alpha = max(alpha,bounds[0])
            beta = min(beta,bounds[1])

        # print(len(cells), ": length of cells")
        # print("old move is ",old_move,hashval)
        # nodeVal = 0,cells[0]
        # beta = b
        # alpha = a
        #
        # if(board.find_terminal_state()[0] == 'x'):
        #     nodeVal = self.termVal, old_move
        #
        # elif(board.find_terminal_state()[0] == 'o'):
        #     nodeVal = -1*self.termVal, old_move
        #
        # elif(self.trans.has_key(hashval)):
        #     bounds = self.trans[hashval]
        #     if(bounds[0] >= b):
        #         return bounds[0]
        #     if(bounds[1] <= a):
        #         return bounds[1]
        #     a = max(a,bounds[0])
        #     b = min(b,bounds[1])

        # if(board.find_terminal_state()[0] == 'NONE' or depth > self.limit):
        #     print("while returning heur")
        #     # board.print_board()
        #     heurVal = self.heuristic(board)
        #     print("final returned as ",heurVal)
        #     nodeVal = heurVal,old_move
        #     print("hello")

        # random.shuffle(cells)
        # print(cells)

        cells = board.find_valid_move_cells(old_move)
        # random.shuffle(cells) 
        # print(len(cells), ": length of cells")
        if (flag == 'x'):
            nodeVal = -INFINITY, cells[0]
            new = 'o'
            tmp = copy.deepcopy(board.block_status)
            a = alpha

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                  break
                board.update(old_move, chosen, flag)
                # print("chosen ",chosen)
                if (board.find_terminal_state()[0] == 'x'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    nodeVal = self.termVal,chosen
                    break
                elif (board.find_terminal_state()[0] == 'o'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE' or depth >= self.limit):
                    tmp1 = self.heuristic(board)
                else:
                    tmp1 = self.alphaBeta(board, chosen, new, depth+1, a, beta)[0]
                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                if(nodeVal[0] < tmp1):
                    nodeVal = tmp1,chosen
                # print("hi nodeval ",nodeVal)
                a = max(a, tmp1)
                if beta <= nodeVal[0] :
                    break
            del(tmp)

        if (flag == 'o'):
            nodeVal = INFINITY, cells[0]
            new = 'x'
            tmp = copy.deepcopy(board.block_status)
            b = beta

            for chosen in cells :
                if datetime.datetime.utcnow() - self.begin >= self.timeLimit :
                  break
                board.update(old_move, chosen, flag)
                # print("chosen ",chosen)
                if(board.find_terminal_state()[0] == 'o'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    nodeVal = -1*self.termVal,chosen
                    break
                elif(board.find_terminal_state()[0] == 'x'):
                    board.board_status[chosen[0]][chosen[1]] = '-'
                    board.block_status = copy.deepcopy(tmp)
                    continue
                elif(board.find_terminal_state()[0] == 'NONE' or depth >= self.limit):
                    tmp1 = self.heuristic(board)
                else:
                    tmp1 = self.alphaBeta(board, chosen, new, depth+1, alpha, b)[0]
                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                if(nodeVal[0] > tmp1):
                    nodeVal = tmp1,chosen
                b = min(b, tmp1)
                if alpha >= nodeVal[0] :
                    break
            del(tmp)

        # print("return value is ",nodeVal)
        if(nodeVal[0] <= alpha):
            self.trans[hashval] = [-INFINITY,nodeVal[0]]
        if(nodeVal[0] > alpha and nodeVal[0] < beta):
            self.trans[hashval] = [nodeVal[0],nodeVal[0]]
        if(nodeVal[0]>=beta):
            self.trans[hashval] = [nodeVal[0],INFINITY]
        # print(self.trans.items())
        return nodeVal

    def mtd(self,board,old_move,flag,depth,f):
        g = f
        upperbound = INFINITY
        lowerbound = -INFINITY
        while(lowerbound<upperbound):
            # print("new mtd ",lowerbound,upperbound)
            b = max(g,lowerbound+1)
            tmp = self.alphaBeta(board,old_move,flag,depth,b-1,b)
            g = tmp[0]
            # print(g)
            if(g<b):
                upperbound = g
            else:
                lowerbound = g
        return tmp

    def move(self, board, old_move, flag):
        # print("hey")
        self.begin = datetime.datetime.utcnow()
        self.count += 1
        self.trans.clear()
        print(self.trans.items())
        print("entering the move for ", self.count)
        toret = self.mtd(board,old_move,flag,1,-INFINITY)[1]
        # toret = self.alphaBeta(board, old_move, flag, 1, -10000000, 10000000)[1]
        print("toret",toret)
        return toret[0], toret[1]
