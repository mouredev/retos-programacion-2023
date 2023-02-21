import os
import time
import psutil


class Random:
    def __init__(self):
        # To get one number between object creation and random() call
        self._seed = int(str(time.time_ns())[-10:])

    def _current_seed(self):
        ram_usage = psutil.virtual_memory()[2]
        network_data = psutil.net_io_counters()
        data_sent = network_data.bytes_sent
        data_recv = network_data.bytes_recv

        current_seed = (self._seed + int(str(time.time_ns())[-10:])) / 2

        current_seed = current_seed + int(ram_usage)
        current_seed = current_seed * (data_sent + data_recv)
        current_seed = current_seed + sum([ord(i) for i in os.getlogin()])
        return current_seed

    def random(self, max=100, min=1, ):
        pseudorandom_value = (self._current_seed()) % 2147483647
        return pseudorandom_value % (max-min + 1) + min


if __name__ == '__main__':
    random = Random()
    for _ in range(1000):
        print(random.random())
