# -*- coding: utf-8 -*-

from Scripts.var_storage import *
from config import *


class GameTag:
    def __init__(self,
                tag_x, tag_y,
                tag_row, tag_num,
                tag_name, tag_img=None,
                tag_width=50, tag_height=50,
                tag_color="grey50", tag_text_color="white"):

        self.tag_x = tag_x
        self.tag_y = tag_y

        self.tag_row = tag_row
        self.tag_num = tag_num

        self.tag_name = tag_name
        self.tag_img = tag_img if tag_img else PhotoImage(width=1, height=1)

        self.tag_width = tag_width
        self.tag_height = tag_height

        self.tag_color = tag_color
        self.tag_text_color = tag_text_color

        self.move_tag_pos = [0, 0, 0, 0] # up, right, down, left

    def move_tag(self):
        def is_win():
            if Main.GAME_MAP == default_game_map:
                return True

        if self.move_tag_pos[0]: # up
            self.tag_y = self.tag_y - self.tag_height - 6

        elif self.move_tag_pos[1]: # right
            self.tag_x = self.tag_x + self.tag_width + 6

        elif self.move_tag_pos[2]: # down
            self.tag_y = self.tag_y + self.tag_height + 6

        elif self.move_tag_pos[3]: # left
            self.tag_x = self.tag_x - self.tag_width - 6

        Main.MAIN_CANVAS.delete(self.tag_button_draw)

        self.tag_button_draw = Main.MAIN_CANVAS.create_window(
            self.tag_x,
            self.tag_y,
            window=self.tag_button,
            anchor=NW
        )

        self.move_tag_pos = [0, 0, 0, 0]

        Main.STAPS += 1

        if is_win():
            Main.GAME_CANVAS.win_game()

    def click_tag(self):
        def check_pos(row, num):
            try:
                if (row >= 0) and (num >= 0) and (Main.GAME_MAP[row][num] is " "):
                    Main.GAME_MAP[self.tag_row][self.tag_num] = " "
                    Main.GAME_MAP[row][num] = self.tag_name

                    self.tag_row = row
                    self.tag_num = num
                    return True
                else:
                    return False
            except:
                return False

        if check_pos(self.tag_row-1, self.tag_num):
            self.move_tag_pos[0] = 1

        elif check_pos(self.tag_row, self.tag_num+1):
            self.move_tag_pos[1] = 1

        elif check_pos(self.tag_row+1, self.tag_num):
            self.move_tag_pos[2] = 1

        elif check_pos(self.tag_row, self.tag_num-1):
            self.move_tag_pos[3] = 1

        if 1 in self.move_tag_pos:
            self.move_tag()

    def draw_tag(self):
        self.tag_button = Button(
            bd=0,
            image=self.tag_img,
            relief=RIDGE,

            font="Verdana 14",
            text=self.tag_name,

            width=self.tag_width,
            height=self.tag_height,

            bg=self.tag_color,
            fg=self.tag_text_color,

            compound="c",

            command=lambda: self.click_tag()
        )

        self.tag_button_draw = Main.MAIN_CANVAS.create_window(
            self.tag_x,
            self.tag_y,
            window=self.tag_button,
            anchor=NW
        )
