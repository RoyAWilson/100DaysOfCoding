from turtle import Turtle, Screen
import time


class Snake():
    '''
    Class to draw the snake and to move the snake around the screen
    '''

    def __init__(self) -> None:
        self.STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
        self.segments = []
        self.create_snake()
        self.MOVE_DISTANCE = 20
        self.HEAD = self.segments[0]
        self.UP = 90
        self.DOWN = 270
        self.RIGHT = 0
        self.LEFT = 180

    def create_snake(self):
        '''
        Create the snake and set tp starting positions
        '''
        for position in self.STARTING_POSITIONS:

            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        '''
        To draw and move the snake forward by 20 paces continuously
        '''
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(self.MOVE_DISTANCE)

    def up(self) -> None:
        '''
        Move snake to face North
        '''
        if self.HEAD.heading() != self.DOWN:
            self.HEAD.setheading(self.UP)

    def down(self) -> None:
        '''
        Move snake to face south
        '''
        if self.HEAD.heading() != self.UP:
            self.HEAD.setheading(self.DOWN)

    def left(self) -> None:
        '''
        Move snake to face west
        '''
        if self.HEAD.heading() != self.RIGHT:
            self.HEAD.setheading(self.LEFT)

    def right(self) -> None:
        '''
        Move snake to face east
        '''
        if self.HEAD.heading() != self.LEFT:
            self.HEAD.setheading(self.RIGHT)
