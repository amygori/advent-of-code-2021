import sys
from pathlib import Path
import pprint


class PowerData:
    def __init__(self, input):
        self.input = input
        self.oxygen_generator_rating = 0
        self.co2_scrubber_rating = 0
        self.life_support_rating = 0

    def analyze(self):
        self._find_values(self.input, "co2_scrubber")
        self._find_values(self.input, "oxygen_generator")
        self._calculate_life_support_rating()

    def print_report(self):
        self.analyze()
        print(
            f"""
            Life support rating is {self.life_support_rating}
            """
        )

    def _find_values(self, values, rating_type, bit_position=0):
        if len(values) == 1:
            if rating_type == "co2_scrubber":
                self.co2_scrubber_rating = int(values[0], 2)
            elif rating_type == "oxygen_generator":
                self.oxygen_generator_rating = int(values[0], 2)
            return

        revised_list = []
        bits = [bit for value in values for bit in value[bit_position]]
        most_common_bit = max(bits, key=bits.count)
        least_common_bit = min(bits, key=bits.count)
        if rating_type == "oxygen_generator":
            if bits.count(most_common_bit) == bits.count(least_common_bit):
                criterion = "1"
            else:
                criterion = most_common_bit
        elif rating_type == "co2_scrubber":
            if bits.count(most_common_bit) == bits.count(least_common_bit):
                criterion = "0"
            else:
                criterion = least_common_bit
        for value in values:
            if value[bit_position] == criterion:
                revised_list.append(value)

        self._find_values(revised_list, rating_type, bit_position + 1)

    def _calculate_life_support_rating(self):
        self.life_support_rating = (
            self.co2_scrubber_rating * self.oxygen_generator_rating
        )


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        powerData = PowerData(Path.read_text(file).splitlines())
        powerData.print_report()
    else:
        raise TypeError("This is not a file")
