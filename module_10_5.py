import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            lines = file.readlines()
            if not lines:
                break
            all_data.append(lines)
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
stop = datetime.datetime.now() - start
print(f"{stop} (линейный)")

# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    stop = datetime.datetime.now() - start
    print(f"{stop} (многопроцессный)")