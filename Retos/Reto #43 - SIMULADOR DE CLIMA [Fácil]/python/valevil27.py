from random import random


class Climate:
    def __init__(self, temp: int, rainprob: float) -> None:
        self.temp = temp
        self.rainprob = rainprob
        self.rain = False

    def simulate_day(self):
        # * Today
        if random() < self.rainprob:
            self.rain = True
        else:
            self.rain = False
        today = (self.temp, self.rain)

        # * Tomorrow
        self.set_rainprob()
        self.set_temp()

        return today

    def set_rainprob(self):
        if self.temp > 25:
            self.rainprob = min(self.rainprob + 0.2, 1)
        elif self.temp < 5:
            self.rainprob = max(self.rainprob - 0.2, 0)

    def set_temp(self):
        if self.rain:
            self.temp -= 1
        if (x := random()) < 0.1:
            if x < 0.05:
                self.temp -= 2
            else:
                self.temp += 2

    def __repr__(self) -> str:
        return f"Temperature: {self.temp:3d}ºC | Rain: {self.rain:1} | Rainprob: {self.rainprob:.0%}"


def simulate(days: int, initial_temp: int, initial_rainprob: float):
    climate = Climate(initial_temp, initial_rainprob)
    reports = []
    for day in range(days):
        print(f"[#] Day {day+1:4d}: {climate}")
        reports.append(climate.simulate_day())
    print(
        f"""[!] Report for {days} days simmulation:
\t - Maximum Temperature: {max(r[0] for r in reports)}ºC
\t - Minimum Temperature: {min(r[0] for r in reports)}ºC
\t - Total Rain Days:     {sum(r[1] for r in reports)}"""
    )


if __name__ == "__main__":
    simulate(100, 24, 0.2)
