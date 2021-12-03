import sys
from pathlib import Path

def count_increases(input):
  data = list(input.split())
  print(len(data))
  count = 1
  for idx, num in enumerate(data):
    if idx==0:
      continue
    if num < data[idx-1]:
      continue
    count+=1
  print(count)

if __name__ == "__main__":
  file = Path(sys.argv[1])
  if Path.is_file(file):
    count_increases(Path.read_text(file))
  else:
    raise TypeError("This is not a file")
