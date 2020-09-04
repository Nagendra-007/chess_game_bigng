from pygame.locals import MOUSEBUTTONUP,MOUSEBUTTONDOWN
from chess_pawns import *
from tkinter import Tk, messagebox

pygame.Surface = Tk()

Mousedown = False
Mouseup = False
Mousereleased = False
TargetPiece = None

# game loop
drawboard()
running = True
teams = ["White", "Black"]
index = 0
one = distance_formula(square_boxes[1], square_boxes[2])
one_half = distance_formula(square_boxes[1], square_boxes[8])
two = distance_formula(square_boxes[1], square_boxes[3])
def check_for_checkcondition():
    for piece in pieces:
        if piece.team != TargetPiece.team and type(piece) == King and piece.undercheck():
            checkmate= piece.checkforcheckmate()
            non_moves = 0
            killcheck = piece.killcheck()
            for mov in piece.elgible_moves():
                if mov in piece.non_moves:
                    non_moves += 1

            if len(piece.elgible_moves()) == non_moves and TargetPiece.position not in piece.elgible_moves() and checkmate:
                print(TargetPiece.team,"s won the game")
                Tk().wm_withdraw()
                messagebox.showinfo("CheckMate", TargetPiece.team + " wins!")

            elif TargetPiece.position in piece.elgible_moves() and len(piece.elgible_moves()) == non_moves+1 and killcheck:
                print(TargetPiece.team,"s won the game")
                Tk().wm_withdraw()
                messagebox.showinfo("CheckMate", TargetPiece.team + " wins!")
            else:
                print(piece.team, "'s king is under check")


while running:
    drawboard()
    team = teams[index]
    cursor = pygame.mouse.get_pos()
    # Event Handling---------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            Mousedown = True
        if event.type == MOUSEBUTTONUP:
            Mousedown = False
            Mousereleased = True



    if Mousedown and not TargetPiece:

        for piece in pieces:
            if distance_formula(cursor, piece.rect.center) <= 640 / 16:
                TargetPiece = piece
    if TargetPiece:
        OriginalPlace = TargetPiece.position

    if Mousedown and TargetPiece:
        TargetPiece.drag(cursor)

    if Mousereleased:
        Mousereleased = False
        if TargetPiece:
            if TargetPiece.team==team:
                pos1 = TargetPiece.rect.center
                for Square in square_boxes:
                    if distance_formula(pos1, Square.center) < 640 / 16:  # half width of square
                        newspot = Square
                        otherpiece = nearest_piece(newspot.center, pieces)
                        break

                if newspot in TargetPiece.elgible_moves():

                    if otherpiece.position.colliderect(newspot) and otherpiece.team == TargetPiece.team:
                        TargetPiece.update(OriginalPlace)
                        print("collides with other pawns of your team")

                    # updating in newspot by killing opposite pawn
                    elif otherpiece.position.colliderect(newspot) and otherpiece.team != TargetPiece.team:
                        for piece in pieces:
                            # if your king is under check before or after making a move
                            if piece.team == TargetPiece.team and type(piece) == King:
                                TargetPiece.update(newspot)
                                # here update is done without checking check condition because, we have to check the condition in new spot as well.
                                index = (index - 1) * -1
                                pieces.remove(otherpiece)
                                if piece.undercheck():
                                    TargetPiece.update(OriginalPlace)
                                    pieces.append(otherpiece)
                                    index = (index - 1) * -1
                                    print("Your king will be under check can't let it under check")
                                else:
                                    print("opponent killed")

                    else: # update in new spot without killing any pawn
                        for piece in pieces:
                            # if your king is under check before or after making a move
                            if piece.team == TargetPiece.team and type(piece) == King:
                                TargetPiece.update(newspot)
                                # here update is done without checking check condition because, we have to check the condition in new spot as well.
                                index = (index - 1) * -1
                                if piece.undercheck():
                                    TargetPiece.update(OriginalPlace)
                                    index = (index - 1) * -1
                                    print("Your king will be under check can't let it under check")


                    if type(TargetPiece == White_Pawn) or type(TargetPiece == Pawn):
                        TargetPiece.step_no = 1

                    # checking for the status of opposite team's king after we make a move
                    check_for_checkcondition()




                else: # if the newspot not in movelist.
                    TargetPiece.update(OriginalPlace)
                    print("not in move list")

            else: #if not valid turn
                TargetPiece.update(OriginalPlace)
                print("It's not your turn")

            TargetPiece = None

    for piece in pieces:
        piece.draw(game_window)

    pygame.display.flip()