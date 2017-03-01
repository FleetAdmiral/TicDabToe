
move_ret = (1,3)

block_no = (move_ret[0]/3)*3 + move_ret[1]/3
print block_no

class Board:
    def __init__(self):

        self.block_status = [['-' for i in range(4)] for j in range(4)]


board = Board()


if ((board.block_status[0][0%4]== board.block_status[1/4][1%4] and board.block_status[1/4][1%4]==board.block_status[2/4][2%4] and board.block_status[2/4][2%4]==board.block_status[3/4][3%4] and board.block_status[1/4][1%4]!='-' and board.block_status[1/4][1%4]!='d') or (board.block_status[4/4][4%4]== board.block_status[5/4][5%4] and board.block_status[5/4][5%4]==board.block_status[6/4][6%4] and board.block_status[6/4][6%4]==board.block_status[7/4][7%4] and board.block_status[4/4][4%4]!='-' and board.block_status[4/4][4%4]!='d') or (board.block_status[8/4][8%4]== board.block_status[9/4][9%4] and board.block_status[9/4][9%4]==board.block_status[10/4][10%4] and board.block_status[10/4][10%4]==board.block_status[11/4][11%4] and board.block_status[8/4][8%4]!='-' and board.block_status[8/4][8%4]!='d') or (board.block_status[12/4][12%4]== board.block_status[13/4][13%4] and board.block_status[13/4][13%4]==board.block_status[14/4][14%4] and board.block_status[14/4][14%4]==board.block_status[15/4][(15%4)] and board.block_status[12/4][12%4]!='-' and board.block_status[12/4][12%4]!='d')):
    print "a"