from pygame.locals import MOUSEBUTTONUP,MOUSEBUTTONDOWN
from chess_pawns import *

Mousedown = False
Mouseup = False
Mousereleased = False
TargetPiece = None

# game loop
drawboard()
running = True
while running:

    drawboard()
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

        if distance_formula(cursor, piece.rect.center) <= 640 / 16:
            TargetPiece = piece


    if Mousedown and TargetPiece:
        TargetPiece.drag(cursor)

    if Mousereleased:
        Mousereleased = False

        if TargetPiece:
            pos1 = TargetPiece.rect.center
            for square in square_boxes:
                if distance_formula(pos1, square.center) < 640 / 16:  # half width of square
                    newspot = square

            TargetPiece.update(newspot)
            TargetPiece = None

    piece.draw(game_window)

    pygame.display.flip()