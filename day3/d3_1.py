import sys
from pathlib import Path


class PowerData:
    def __init__(self, input):
        self.input = input
        self.binary_length = len(input[0])
        self.bit_frequency = {"0": {}, "1": {}}
        self.gamma = ""
        self.epsilon = ""
        self.power_consumption = 0

    def analyze(self):
        self._calculate_freq()
        self._find_gamma_and_epsilon()
        self._calculate_power_consumption()
        print(f"Power consumption is {self.power_consumption}")

    def _calculate_freq(self):
        for binary_num in self.input:
            for position, bit in enumerate(binary_num):
                try:
                    self.bit_frequency[bit][f"{position}"] += 1
                except KeyError:
                    self.bit_frequency[bit][f"{position}"] = 1

    def _find_gamma_and_epsilon(self):
        for position in range(self.binary_length):
            zero_freq = self.bit_frequency["0"][str(position)]
            one_freq = self.bit_frequency["1"][str(position)]
            if zero_freq > one_freq:
                self.gamma += str(0)
                self.epsilon += str(1)
            else:
                self.gamma += str(1)
                self.epsilon += str(0)

    def _calculate_power_consumption(self):
        dec_gamma = int(self.gamma, 2)
        dec_epsilon = int(self.epsilon, 2)
        self.power_consumption = dec_gamma * dec_epsilon


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        with Path(file).open() as f:
            powerData = PowerData(f.read().splitlines())
            powerData.analyze()
    else:
        raise TypeError("This is not a file")
