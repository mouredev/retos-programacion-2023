import random

class WeatherSimulator:
    """Simulates weather conditions for a specified number of days."""

    def __init__(self):
        """Initialize the WeatherSimulator."""
        self.days_predicted = self.get_days()
        self.initial_temperature, self.initial_rain_probability = self.get_initial_conditions()
        self.days_rain = 0
        self.temperatures = []

        print("\nWelcome to the Weather Simulator!")
        self.simulate_weather(1, self.initial_temperature, self.initial_rain_probability)

    def get_days(self):
        """Get the number of days for weather prediction from the user."""
        while True:
            try:
                days = int(input("\nHow many days do you want to predict? (Enter an integer greater than 0): "))
                if days > 0:
                    return days
                else:
                    print("Please enter a valid number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_initial_conditions(self):
        """Get initial temperature and rain probability from the user."""
        temp = self.get_integer_input("Enter the initial temperature: ")
        rain_prob = self.get_float_input("Enter the initial rain probability (0-1): ", 0, 1)
        return temp, rain_prob

    def get_integer_input(self, prompt):
        """Get integer input from the user."""
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_float_input(self, prompt, min_value, max_value):
        """Get float input from the user within a specified range."""
        while True:
            try:
                value = float(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Please enter a value between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def simulate_weather(self, day_number, temp, rain_prob):
        """Simulate weather conditions for each day."""
        if day_number <= self.days_predicted:
            change_of_temperature = [False, False]

            next_day_data = [temp, rain_prob]

            if random.random() < 0.1:
                change_of_temperature[0], change_of_temperature[1] = True, random.choice([0, 1])
                if change_of_temperature[1] == 0:
                    temp -= 2
                else:
                    temp += 2

            self.temperatures.append(temp)

            print(f"\nDay {day_number}:\n")
            print(f"Temperature: {temp}")

            if random.randint(0, 9) in [number for number in range(int(rain_prob * 10))]:
                self.days_rain += 1
                print("Today it will rain.")
                next_day_data[0] += 1
            else:
                print("Today it won't rain")

            if temp > 25:
                next_day_data[1] += 0.2

            if temp < 5:
                next_day_data[1] -= 0.2

            self.simulate_weather(day_number + 1, next_day_data[0], next_day_data[1])

        else:
            print(f"\nMinimum temperature during the prediction will be {min(self.temperatures)}°C.")
            print(f"Maximum temperature during the prediction will be {max(self.temperatures)}°C.")
            print(f"Total rainy days: {self.days_rain}.")

if __name__ == "__main__":
    while True:
        WeatherSimulator()
        restart = input("\nDo you want to start a new prediction? (Enter 'yes' or 'no'): ")
        if restart.lower() != 'yes':
            break
