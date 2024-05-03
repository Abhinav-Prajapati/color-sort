import copy
matrix =[[2, 5, 1, 1],
         [2, 5, 2, 3],
         [1, 5, 0, 3],
         [2, 1, 0, 0],
         [0, 3, 5, 3],
         [],
         []]

matrix_2 =[[2,2,4 , 4],
         [2, 4 ,4 , 2],
         []]

def get_valid_moves(mat):
    valid_moves = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j :
                continue
            elif len(mat[i]) == 0 and len(mat[j]) == 0:
                continue
            elif len(mat[i]) == 0 :
                continue
            elif len(mat[j]) == 0 :
                valid_moves.append((i,j))
            elif len(mat[j]) == 4:
                continue
            elif mat[i][0] == mat[j][0]: # fi top element are same
                valid_moves.append((i,j))
            
    return valid_moves

def is_solved(matrix):
    for tube in matrix:
        if not tube:  # If tube is empty it might be solved now check for other tubes
            continue
        if len(tube) == 4 and all(element == tube[0] for element in tube):
            continue
        return False
    return True

def make_move(matrix, move):
    temp = copy.deepcopy(matrix)
    i, j = move
    while temp[i] and (not temp[j] or temp[i][0] == temp[j][0]) and len(temp[j]) < 4:
        element = temp[i].pop(0)
        temp[j].insert(0, element)
    return temp

def print_matrix(list1):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            print(list1[i][j], end=" ")
        print()
    print('---')

def filter_moves(matrix , moves):
    # remove moves in which one tube is solved and ther is empty and it just stuck and pore liquid into each other
    moves_ = []
    for move in moves:
        i , j = move
        if len(matrix[j]) == 0 and all(element == matrix[i][0] for element in matrix[i]):
            continue
        elif len(matrix[i]) == 0 and all(element == matrix[j][0] for element in matrix[j]):
            continue
        else:
            moves_.append(move)
    return moves_

def dfs(matrix):
    if is_solved(matrix):
        print("matrix escaped!!")
        return 
    valid_moves = get_valid_moves(matrix)
    valid_moves = filter_moves(matrix,valid_moves)
    if not valid_moves:
        print("No valid moves left!")
        return

    print(valid_moves)
    for move in valid_moves:
        print("move picked ", move)
        temp = make_move(matrix,move)
        print_matrix(temp)
        dfs(temp)

dfs(matrix)
