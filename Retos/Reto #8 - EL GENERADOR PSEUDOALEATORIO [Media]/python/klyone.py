#!/usr/bin/env python3

import os
import psutil
import time

class RandomGenerator:
    def __init__(self):
        self.__regenerate_seed()

    def __regenerate_seed(self):
        current_system_time = round(time.time_ns())
        self.seed = int((current_system_time * 77) / 51)

    def __assign_seed(self, seed):
        self.seed = seed

    def generate_number(self, min_value, interval_length):
        current_system_time = round(time.time_ns())
        _, _, load = psutil.getloadavg()
        cpu_usage = (load/os.cpu_count()) * 100
        ram_usage = psutil.virtual_memory()[2]
        network_data = psutil.net_io_counters()
        data_sent = network_data.bytes_sent
        data_recv = network_data.bytes_recv
        disk_data = psutil.disk_io_counters(perdisk=False)
        disk_sent = disk_data.write_bytes
        disk_recv = disk_data.read_bytes

        current_seed = int(current_system_time + cpu_usage)
        current_seed = current_seed + int(ram_usage)
        current_seed = current_seed * (data_sent + data_recv)
        current_seed = current_seed + int(disk_sent * disk_recv)
        current_seed = int(self.seed * current_seed)

        self.__assign_seed(current_seed)

        return min_value + (current_seed % (interval_length))

if __name__ == "__main__":
    generator = RandomGenerator()
    print(generator.generate_number(1, 100))
