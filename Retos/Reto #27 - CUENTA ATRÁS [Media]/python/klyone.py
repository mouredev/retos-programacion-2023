#!/usr/bin/env python3

import time

class Countdown:
    def __init__(self, init_value, interval_in_secs):
        if init_value <= 0 or interval_in_secs <= 0:
            raise Exception()

        self.init_value = init_value
        self.interval_in_secs = interval_in_secs

    def start(self):
        self.current_value = self.init_value

        while self.current_value > 0:
            print(self.current_value)
            time.sleep(self.interval_in_secs)
            self.current_value = self.current_value - 1
        print("Countdown finished!")

if __name__ == "__main__":
    counter = Countdown(10, 1)
    counter.start()

    counter = Countdown(100, 2)
    counter.start()
