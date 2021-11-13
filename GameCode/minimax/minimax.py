from copy import deepcopy
import pygame

ROWS, COLS = 8, 8
MAX = 1000

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, maxPlayer, game):
    # Your Code Goes Here
    board = game.getBoard()
    if depth <= 0:
        return board.evaluate(), board
    if maxPlayer:
        color = WHITE
    else:
        color = RED
    all_moves = getAllMoves(game.board, color, game)
    best_moves = []
    for move in all_moves:
        new_game = deepcopy(game)
        simulateMove(move, new_game.board, new_game)
        score, new_boad = minimax(position, depth-1, not maxPlayer, new_game)
        best_moves.append([move, score])

    best_move = board
    if(maxPlayer):
        best_score = 0
        for move in best_moves:
            if move[1] >= best_score:
                best_score = move[1]
                best_move = move[0]
    else:
        best_score = MAX
        for move in best_moves:
            if move[1] <= best_score:
                best_score = move[1]
                best_move = move[0]

    return best_score, best_move
        

def simulateMove(piece, move, board, game, skip):
    # Your Code Goes Here
    game._move(move)

def getAllMoves(board, color, game):
    # Your Code Goes Here
    moves = {}
    pieces = board.getAllPieces(color)
    for piece in pieces:
        curr_moves = board.getValidMoves(piece)
        moves.update(curr_moves)
    return moves