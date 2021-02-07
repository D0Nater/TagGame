# -*- coding: utf-8 -*-

from Scripts.var_storage import *
from config import *


class GameHeader:
    def __init__(self):
        Main.HEADER_CANVAS = Canvas(Main.ROOT, width=window_width, height=header_height, bg="grey60", highlightthickness=0)
        Main.HEADER_CANVAS.pack()


        self.menu_button = Button(
            bd=0,
            relief=RIDGE,

            font="Verdana 14",
            text="Меню",

            command=lambda: Main.GAME_MENU.draw_menu()
        )

        self.menu_button_draw = Main.HEADER_CANVAS.create_window(
            20,
            20,
            window=self.menu_button,
            anchor=NW
        )

        self.restart_button = Button(
            bd=0,
            relief=RIDGE,

            font="Verdana 14",
            text="Заново",

            command=lambda: Main.GAME_CANVAS.start_game()
        )

        self.tag_button_draw = Main.HEADER_CANVAS.create_window(
            window_width-100,
            20,
            window=self.restart_button,
            anchor=NW
        )
