from datetime import datetime
from threading import Thread
from time import sleep

def wite_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start_time = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end_time = datetime.now()
time_shift = end_time - start_time
print(time_shift)

thr_start_time = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

thr_end_time = datetime.now()
thr_time_shift = thr_end_time - thr_start_time
print(thr_time_shift)