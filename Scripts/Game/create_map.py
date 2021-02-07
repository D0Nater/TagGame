# -*- coding: utf-8 -*-

from random import choice as randchoice

from Scripts.Game.draw_tag import GameTag
from Scripts.var_storage import *
from config import *


class CreateMap:
    def __init__(self):
        pass

    def draw_game_map(self):
        Main.MAIN_CANVAS.delete("all")

        tag_x_default = 130

        tag_x = tag_x_default
        tag_y = 50

        for row in range(len(Main.GAME_MAP)):
            for num in range(4):
                try:
                    new_tag = GameTag(
                        tag_row=row, tag_num=num,
                        tag_x=tag_x, tag_y=tag_y,
                        tag_name=Main.GAME_MAP[row][num]
                    )
                    new_tag.draw_tag()

                    Main.TAG_ARRAY.append(new_tag)

                    tag_x += new_tag.tag_width+6

                except IndexError:
                    Main.GAME_MAP[-1].append(" ")
                    break

            tag_x = tag_x_default
            tag_y += new_tag.tag_height+6

    def create_new_game_map(self):
        all_nums = [
            "1", "2", "3", "4",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "13", "14", "15"
        ]

        Main.GAME_MAP = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", ""]
        ]

        for row in range(len(Main.GAME_MAP)):
            for num in range(4):
                try:
                    randnum = randchoice(all_nums)
                    Main.GAME_MAP[row][num] = randnum
                    all_nums.remove(randnum)
                except IndexError:
                    break

        self.draw_game_map()
