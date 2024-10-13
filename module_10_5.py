from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readlines()
        all_data.append(line)


filenames = [f'./files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов:
    start = datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.now()
    print(f'Линейный вызов занимает {end - start} сек.')

    # Многопроцессный вызов:
    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов занимает {end - start} сек.')
