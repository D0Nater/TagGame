# -*- coding: utf-8 -*-

from win32api import GetSystemMetrics

""" Interface """
from Scripts.game_menu import GameMenu
from Scripts.game_header import GameHeader
from Scripts.create_main_canvas import GameCanvas

from Scripts.game_timer import GameTimer
from Scripts.Game.create_map import CreateMap

""" Other """
from Scripts.var_storage import *
from config import *


class TagGames:
    def __init__(self, width_space=0, height_space=0,
                resizable_width=True, resizable_height=True):

        Main.ROOT = Tk()

        # Window Settings #
        Main.ROOT.title(GAME_NAME)
        Main.ROOT.geometry(f"{window_width}x{window_height}+{width_space}+{height_space}")
        Main.ROOT.resizable(width=resizable_width, height=resizable_height)

        Main.GAME_HEADER = GameHeader()

        Main.GAME_CANVAS = GameCanvas()

        Main.GAME_MENU = GameMenu()
        Main.GAME_MENU.draw_menu()

        Main.GAME_TIMER = GameTimer(Main.MAIN_CANVAS)
        Main.CREATE_MAP = CreateMap()

    def win_center(self):
        x = int(GetSystemMetrics(0)/2) - int(window_width/2)
        y = int(GetSystemMetrics(1)/2) - int(window_height/2)

        Main.ROOT.geometry(f"+{x}+{y}")

    def start_game(self):
        Main.ROOT.mainloop()


if __name__ == "__main__":
    game = TagGames(
        resizable_width=False, resizable_height=False
    )

    game.win_center()

    game.start_game()
