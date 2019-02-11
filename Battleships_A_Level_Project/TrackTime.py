import time

class TrackTime(object):
    """description of class"""
    def __init__(self):
        self._timer_total_1 = 0
        self._timer_total_2 = 0

        self._current_timer1 = 0
        self._current_timer2 = 0

    def start_timer_1(self):
        self._current_timer1 = time.time()

    def start_timer_2(self):
        self._current_timer2 = time.time()

    def stop_timer_1(self):
        t = time.time() - self._current_timer1
        self._timer_total_1 = self._timer_total_1 + t
        self._current_timer1 = 0

    def stop_timer_2(self):
        t = time.time() - self._current_timer2
        self._timer_total_2 = self._timer_total_2 + t
        self._current_timer1 = 0

    def get_overall_time_for_timer_1(self):
        s = time.strftime("%H:%M:%S", time.localtime(self._timer_total_1))
        return s

    def get_overall_time_for_timer_2(self):
        s = time.strftime("%H:%M:%S", time.localtime(self._timer_total_2))
        return s






