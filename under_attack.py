#* queen problem with recurison
BOARD_SIZE = 8

def under_attack(col, queens):
   left = right = col
   for r, c in reversed(queens):
 #左右有冲突的位置的列号
       left, right = left - 1, right + 1

       if c in (left, col, right):
           return True
   return False

