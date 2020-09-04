from Requried_functions import *

class chess_piece(pygame.sprite.Sprite):


    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.team = team
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(70,70))
        self.position = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position.topleft
        self.rect.center = position.center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def drag(self, cursor):
        self.rect.center = cursor

    def update(self, position):
        self.position = position
        self.rect.center = position.center


class King(chess_piece):
    def __init__(self,image, position, team):
        chess_piece.__init__(self,image,position,team)
        self.non_moves = []
        self.checkpath = []
    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[0,pi,pi/2,-pi/2,pi/4,-pi/4,3*pi/4,-3*pi/4])
        move_list = []
        for pos in elgible_moves_if_no_blocls:
            if distance_formula(self.position, pos[0])<= 113.137084989848:
                move_list.append(pos[0])

        for piece in pieces:
            if piece.team == self.team and piece.position in move_list:
                    move_list.remove(piece.position)


        return move_list

    def undercheck(self):
        for piece in pieces:
            if self.position in piece.elgible_moves() and piece.team != self.team:
                dx = self.position.centerx - piece.position.centerx
                dy = self.position.centery - piece.position.centery
                check_angle = math.atan2(-dy, dx)
                check_path_list = movable_squares(self.position, square_boxes, [check_angle])
                for (x,y) in check_path_list:
                    if distance_formula(self.position,x) <= distance_formula(self.position,piece.position):
                        self.checkpath.append(x)

                    if distance_formula(self.position, x) <= 113.137084989848 and x!=piece.position:
                        self.non_moves.append(x)

                return True
            else:
                self.checkpath = []
        return False

    def killcheck(self):
        for piece in pieces:
            if self.position in piece.elgible_moves() and piece.team != self.team:
                checkpiece = piece
        for piece in pieces:
            if piece.team == checkpiece.team and piece!= checkpiece and checkpiece.position in piece.elgible_moves():
                return True


    def checkforcheckmate(self):
        for move in self.checkpath:
            for piece in pieces:
                if piece.team== self.team and type(piece)!=King :
                    for mov in piece.elgible_moves():
                        if mov == move:
                            return False
        return True

class Queen(chess_piece):

    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[0,pi,pi/2,-pi/2,pi/4,-pi/4,3*pi/4,-3*pi/4])

        move_list = []
        remove_from_movelist = []
        for item in elgible_moves_if_no_blocls:
            move_list.append(item[0])
            for piece in pieces:
                if piece.position == item[0] :
                    remove_from_movelist.append(item)

        for (a, b) in elgible_moves_if_no_blocls:
            for(x,y) in remove_from_movelist:
                if(isfarther(self.position,a,x) and y==b and a in move_list):
                    move_list.remove(a)

        return move_list

class Rook(chess_piece):

    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[0,pi,pi/2,-pi/2])
        move_list = []
        remove_from_movelist = []
        for item in elgible_moves_if_no_blocls:
            move_list.append(item[0])
            for piece in pieces:
                if piece.position == item[0] and item[0]!= self.position:
                    remove_from_movelist.append(item)
        for (a, b) in elgible_moves_if_no_blocls:
            for (x, y) in remove_from_movelist:
                if (isfarther(self.position, a, x) and y == b and a in move_list):
                    move_list.remove(a)
        return move_list

class Knight(chess_piece):

    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[
            math.atan2(1, 2),
            math.atan2(2, 1),
            math.atan2(1, -2),
            math.atan2(-2, 1),
            math.atan2(-1, -2),
            math.atan2(-2, -1),
            math.atan2(-1, 2),
            math.atan2(2, -1),
        ])
        move_list = []
        dis = distance_formula(square_boxes[0], square_boxes[10])
        for pos in elgible_moves_if_no_blocls:
            if distance_formula(self.position, pos[0])== dis:
                move_list.append(pos[0])
        return move_list

class Bishop(chess_piece):

    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[pi/4,-pi/4,3*pi/4,-3*pi/4])
        move_list = []
        remove_from_movelist = []
        for item in elgible_moves_if_no_blocls:
            move_list.append(item[0])
            for piece in pieces:
                if piece.position == item[0]:
                    remove_from_movelist.append(item)
        for (a, b) in elgible_moves_if_no_blocls:
            for (x, y) in remove_from_movelist:
                if (isfarther(self.position, a, x) and y == b and a in move_list):
                    move_list.remove(a)
        return move_list

class Pawn(chess_piece):
    def __init__(self,image, position, team):
        chess_piece.__init__(self,image,position,team)
        self.step_no = 0
    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position, square_boxes, [pi / 2])
        elgible_moves_if_takes_blocls = movable_squares(self.position, square_boxes, [pi / 4, 3 * pi / 4])

        move_list = []
        removeupto = []
        one_half = distance_formula(square_boxes[1], square_boxes[8])
        two = distance_formula(square_boxes[1], square_boxes[3])
        one = distance_formula(square_boxes[1], square_boxes[2])

        if self.step_no == 0:
            for pos in elgible_moves_if_no_blocls:
                if distance_formula(self.position, pos[0]) <= two:
                    move_list.append(pos[0])


        else:
            for pos in elgible_moves_if_no_blocls:
                if distance_formula(self.position, pos[0]) == one:
                    move_list.append(pos[0])

        for piece in pieces:
            for item in elgible_moves_if_no_blocls:
                if piece.position == item[0]:
                    removeupto.append(item)
                    if item[0] in move_list:
                        move_list.remove(item[0])

        for (block, angle) in elgible_moves_if_takes_blocls:
            # if not block.colliderect(self.position) and distance_formula(block, self.position) == one_half:
            for piece in pieces:
                if piece.position == block and distance_formula(block, self.position) == one_half:
                    move_list.append(block)
        return move_list






class White_Pawn(chess_piece):
    def __init__(self,image, position, team):
        chess_piece.__init__(self,image,position,team)
        self.step_no = 0
    def elgible_moves(self):
        elgible_moves_if_no_blocls = movable_squares(self.position,square_boxes,[-pi/2])
        elgible_moves_if_takes_blocls = movable_squares(self.position,square_boxes,[-pi/4,-3*pi/4])
        move_list = []
        removeupto = []
        one_half = distance_formula(square_boxes[1], square_boxes[8])
        two = distance_formula(square_boxes[1], square_boxes[3])
        one = distance_formula(square_boxes[1], square_boxes[2])

        if self.step_no ==0:
            for pos in elgible_moves_if_no_blocls:
                if distance_formula(self.position, pos[0])<= two:
                    move_list.append(pos[0])


        else:
            for pos in elgible_moves_if_no_blocls:
                if distance_formula(self.position, pos[0]) == one:
                    move_list.append(pos[0])

        for piece in pieces:
            for item in elgible_moves_if_no_blocls:
                if piece.position == item[0]:
                    removeupto.append(item)
                    if item[0] in move_list:
                        move_list.remove(item[0])


        for (block, angle) in elgible_moves_if_takes_blocls:
            #if not block.colliderect(self.position) and distance_formula(block, self.position) == one_half:
            for piece in pieces:
                if piece.position == block and distance_formula(block, self.position) == one_half:
                    move_list.append(block)
        return move_list


drawboard()
# This function is called to initialise the following chess pieces with in the square boxes defined in the function

pieces = [
    White_Pawn("Media\wpawn.jpeg", square_boxes[48], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[49], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[50], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[51], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[52], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[53], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[54], 'White'),
    White_Pawn("Media\wpawn.jpeg", square_boxes[55], 'White'),
    Pawn("Media\pawn.jpeg", square_boxes[8], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[9], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[10], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[11], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[12], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[13], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[14], 'Black'),
    Pawn("Media\pawn.jpeg", square_boxes[15], 'Black'),
    Bishop("Media\wcamel.jpeg", square_boxes[58], 'White'),
    Bishop("Media\wcamel.jpeg", square_boxes[61], 'White'),
    Bishop("Media\camel.jpeg", square_boxes[5], 'Black'),
    Bishop("Media\camel.jpeg", square_boxes[2], 'Black'),
    Knight("Media\whorse.jpeg", square_boxes[57], 'White'),
    Knight("Media\whorse.jpeg", square_boxes[62], 'White'),
    Knight("Media\horse.jpeg", square_boxes[1], 'Black'),
    Knight("Media\horse.jpeg", square_boxes[6], 'Black'),
    Rook("Media\wele.jpeg", square_boxes[56], 'White'),
    Rook("Media\wele.jpeg", square_boxes[63], 'White'),
    Rook("Media\ele.jpeg", square_boxes[0], 'Black'),
    Rook("Media\ele.jpeg", square_boxes[7], 'Black'),
    King("Media\king.jpeg", square_boxes[4], 'Black'),
    King("Media\wking.jpeg", square_boxes[60], 'White'),
    Queen("Media\queen.jpeg", square_boxes[3], 'Black'),
    Queen("Media\wqueen.jpeg", square_boxes[59], 'White'),
]

