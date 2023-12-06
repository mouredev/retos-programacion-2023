from typing import NoReturn, Protocol, Iterable, NamedTuple
import random
import functools
import time
import dataclasses
import abc


type Number = float | int
type Seconds = Number


class InvalidNumberException(Exception):
    pass


class ProbabilityOutOfRangeException(Exception):
    pass


def raise_invalid_number_exception(msg: str) -> NoReturn:
    raise InvalidNumberException(msg)


def raise_probability_out_of_range_exception(msg: str) -> NoReturn:
    raise ProbabilityOutOfRangeException(msg)


class ITemperatureDataStorage[T](abc.ABC):
    def __init__(self) -> None:
        self._data: Iterable[T] = []

    @property
    @abc.abstractmethod
    def data(self) -> Iterable[T]:
        pass

    @data.setter
    @abc.abstractmethod
    def data(self, *new_data: T) -> None:
        pass

    def __getitem__(self, index: int) -> T:
        if index >= self.__len__():
            raise IndexError("Index out of range")

        return self._data[index]

    def __len__(self) -> int:
        return len(list(self._data))


class TemperatureDataStorageInMemory(ITemperatureDataStorage[Number]):
    @property
    def data(self) -> Iterable[Number]:
        return self._data

    @data.setter
    def data(self, *new_data: Number) -> None:
        self._data = new_data


@dataclasses.dataclass(frozen=True)
class UserSetup:
    initial_temp: Number
    probability_rain: Number
    days_prediction: int


@dataclasses.dataclass(frozen=True)
class Setup:
    temperature_storage: ITemperatureDataStorage[Number]


class ClimateSimulatorFn(Protocol):
    def __call__(self, user_setup: UserSetup, setup: Setup) -> None:
        ...


@functools.lru_cache
def get_cities() -> list[str]:
    return [
        "Bogotá",
        "Medellín",
        "Cali",
        "Barranquilla",
        "Cartagena",
        "Bucaramanga",
        "Santa Marta",
        "Manizales",
        "Villavicencio",
    ]


def choice_random_city() -> str:
    cities = get_cities()

    return random.choice(cities)


def start_day_simulation(duration_seconds: Seconds) -> None:
    time.sleep(duration_seconds)


def calculate_probability(probability: Number = 10) -> bool:
    if probability > 1:
        probability = probability / 100

    if probability > 100:
        probability = 100

    return random.random() <= probability


change_temperature_with_10_percent_probability_partial_fn = functools.partial(
    calculate_probability, probability=10
)

is_raining_partial_fn = functools.partial(calculate_probability)


class TemperatureOperationFn(Protocol):
    def __call__(self, initial_value: Number, quantity: Number) -> Number:
        pass


class TemperatureOperationPartialFn(Protocol):
    def __call__(self, initial_value: Number) -> Number:
        pass


def increment(initial_value: Number, quantity: Number) -> Number:
    return initial_value + quantity


def decrement(initial_value: Number, quantity: Number) -> Number:
    return initial_value - quantity


increase_temperature_by_2_partial_fn = functools.partial(increment, quantity=2)
decrease_temperature_by_2_partial_fn = functools.partial(decrement, quantity=2)
decrease_temperature_by_1_partial_fn = functools.partial(decrement, quantity=1)
decrease_days_by_1_partial_fn = functools.partial(decrement, quantity=1)
increase_rainy_days_by_1_partial_fn = functools.partial(increment, quantity=1)

increase_rain_probability_by_20_partial_fn = functools.partial(increment, quantity=20)
decrease_rain_probability_by_20_partial_fn = functools.partial(decrement, quantity=20)


def random_temperature_operation() -> TemperatureOperationPartialFn:
    temperature_operations = [
        increase_temperature_by_2_partial_fn,
        decrease_temperature_by_2_partial_fn,
    ]

    return random.choice(temperature_operations)


def determinate_actual_temperature(
    temperature: Number, probability_rain: Number
) -> Number:
    actual_temperature = temperature
    temperature_operation = random_temperature_operation()

    if change_temperature_with_10_percent_probability_partial_fn():
        actual_temperature = temperature_operation(initial_value=actual_temperature)

    if probability_rain == 100:
        actual_temperature = decrease_temperature_by_1_partial_fn(
            initial_value=actual_temperature
        )

    return actual_temperature


def determinate_probability_rain(
    temperature: Number, probability_rain: Number
) -> Number:
    actual_temperature = temperature
    probability_rain = probability_rain

    if actual_temperature > 25:
        probability_rain = increase_rain_probability_by_20_partial_fn(
            initial_value=probability_rain
        )

    if actual_temperature < 5:
        probability_rain = decrease_rain_probability_by_20_partial_fn(
            initial_value=probability_rain
        )

    return probability_rain


class Probabilities(NamedTuple):
    actual_temperature: Number
    probability_rain: Number


def determinate_probabilities(
    temperature: Number, probability_rain: Number
) -> Probabilities:
    actual_temperature = determinate_actual_temperature(temperature, probability_rain)
    probability_rain = determinate_probability_rain(temperature, probability_rain)

    return Probabilities(
        actual_temperature=actual_temperature, probability_rain=probability_rain
    )


def calculate_min_temperature(temperatures: Iterable[Number]) -> Number:
    return min(temperatures, default=None)


def calculate_max_temperature(temperatures: Iterable[Number]) -> Number:
    return max(temperatures, default=None)


def validate_climate_simulator_fn(fn: ClimateSimulatorFn) -> ClimateSimulatorFn:
    @functools.wraps(fn)
    def wrapper(user_setup: UserSetup, setup: Setup) -> None:
        if not isinstance(user_setup, UserSetup):
            raise TypeError("setup debe ser una instancia de UserSetup")

        if not isinstance(setup, Setup):
            raise TypeError("setup debe ser una instancia de Setup")

        if 0 < user_setup.probability_rain > 100:
            raise_probability_out_of_range_exception(
                msg="La probabilidad de lluvia debe estar entre 0 y 100"
            )
        if not isinstance(user_setup.days_prediction, int):
            raise_invalid_number_exception(
                msg="El número de días de predicción debe ser un número entero"
            )

        if not isinstance(user_setup.initial_temp, (int, float)):
            raise_invalid_number_exception(
                msg="La temperatura inicial debe ser un número de punto flotante o entero"
            )

        fn(user_setup=user_setup, setup=setup)

    return wrapper


def print_temperatures(min_temperature: Number, max_temperature: Number) -> None:
    print(f"la temperatura máxima es: {max_temperature}")
    print(f"la temperatura mínima es: {min_temperature}")


def print_rainy_days(days: int) -> None:
    print(f"hay {days} dias de lluvia")


@dataclasses.dataclass(frozen=True)
class ClimateSimulatorResult:
    rainy_days: int
    days_prediction: int
    min_temperature: Number
    max_temperature: Number


def print_climate_simulator_result(result: ClimateSimulatorResult) -> None:
    if result.days_prediction == result.rainy_days:
        print_rainy_days(days=result.rainy_days)

    print_temperatures(
        min_temperature=result.min_temperature, max_temperature=result.max_temperature
    )
    print(f"hay {result.rainy_days} dias de lluvia")


@validate_climate_simulator_fn
def climate_simulator(user_setup: UserSetup, setup: Setup) -> None:
    days = user_setup.days_prediction
    actual_temp = user_setup.initial_temp
    probability_rain = user_setup.probability_rain
    rainy_days = 0

    temperature_storage = setup.temperature_storage
    max_temp = calculate_max_temperature(temperatures=temperature_storage.data)
    min_temp = calculate_min_temperature(temperatures=temperature_storage.data)
    city = choice_random_city()

    while days > 0:
        print(f"la temperatura de hóy es: {actual_temp} en {city}")
        start_day_simulation(duration_seconds=10)

        actual_temp, probability_rain = determinate_probabilities(
            temperature=actual_temp, probability_rain=probability_rain
        )
        temperature_storage.data = actual_temp

        if is_raining_partial_fn(probability=probability_rain):
            print("lloviendo")
            actual_temp = decrease_temperature_by_1_partial_fn(
                initial_value=actual_temp
            )
            rainy_days = increase_rainy_days_by_1_partial_fn(initial_value=rainy_days)

        days = decrease_days_by_1_partial_fn(initial_value=days)

    print_climate_simulator_result(
        ClimateSimulatorResult(
            rainy_days=rainy_days,
            days_prediction=days,
            min_temperature=min_temp,
            max_temperature=max_temp,
        )
    )


class Config(NamedTuple):
    user_setup: UserSetup
    setup: Setup


def execute(simulator: ClimateSimulatorFn, config: Config) -> None:
    simulator(user_setup=config.user_setup, setup=config.setup)


def main() -> None:
    user_setup = UserSetup(initial_temp=23, probability_rain=60, days_prediction=5)
    setup = Setup(temperature_storage=TemperatureDataStorageInMemory())
    config = Config(user_setup=user_setup, setup=setup)
    execute(simulator=climate_simulator, config=config)


if __name__ == "__main__":
    main()
