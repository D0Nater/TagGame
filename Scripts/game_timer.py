# -*- coding: utf-8 -*-

from datetime import datetime
from time import gmtime, time as time_time


class GameTimer:
    def __init__(self, game_canvas, x_cord=10, y_cord=10, text_size=14):
        self.game_canvas = game_canvas
        self.text_size = text_size

        self.x_cord = x_cord
        self.y_cord = y_cord

        self._time = 0.0
        self._systime = None
        self.is_running = False

        self.default_time()

    def start_timer(self):
        self.is_running = True
        self._systime = time_time()

    def pause_timer(self):
        self.is_running = False

        self._time = self.get_time()
        self._systime = None

    def stop_timer(self):
        self.pause_timer()
        date_time = datetime.fromtimestamp(self._time)
        self.finish_time_str = date_time.strftime("%M:%S.%f")

    def get_time(self):
        """ Get the elapsed time """
        if self._systime is None:
            return self._time

        return time_time() - self._systime + self._time

    def default_time(self):
        self._time = 0.0
        self._systime = None
        self.finish_time_str = str(gmtime(self._time))

    # def start_timer(self):
    #     self.is_running = True
    #     self.start_time = time_time()

    # # def pause_timer(self):
    # #     self.time_now += self.start_time-self.time_now

    # def stop_timer(self):
    #     self.is_running = False
    #     self.finish_time = self.start_time-self.time_now
    #     self.finish_time_str = strftime("%M:%S", gmtime(self.finish_time))
