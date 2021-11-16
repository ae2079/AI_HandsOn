from copy import deepcopy
import pygame

ROWS, COLS = 8, 8
MAX = 1000

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, maxPlayer, game):
    # Your Code Goes Here
    board = position
    #################
    #for row in board.board:
    #    print(row)
    #print(depth)
    ##################
    if depth <= 0:
        #print("here")
        return board.evaluate(), board
    if maxPlayer:
        color = WHITE
    else:
        color = RED
    all_moves = getAllMoves(board, color, game)
    best_moves = []
    for piece in all_moves:
        for move in all_moves[piece]:
            new_board = deepcopy(board)
            simulateMove(piece, move, new_board, game, all_moves[piece][move])
            score, new_board = minimax(new_board, depth-1, not maxPlayer, game)
            best_moves.append([new_board, score])

    best_move = board
    if(maxPlayer):
        best_score = -MAX
        for move in best_moves:
            if move[1] > best_score:
                best_score = move[1]
                best_move = move[0]
    else:
        best_score = MAX
        for move in best_moves:
            if move[1] < best_score:
                best_score = move[1]
                best_move = move[0]

    return best_score, best_move
        

def simulateMove(piece, move, board, game, skip):
    # Your Code Goes Here
    board.remove(skip)
    board.move(piece, move[0], move[1])


def getAllMoves(board, color, game):
    # Your Code Goes Here
    moves = {}
    pieces = board.getAllPieces(color)
    for piece in pieces:
        curr_moves = board.getValidMoves(piece)
        moves[piece] = curr_moves
    return moves