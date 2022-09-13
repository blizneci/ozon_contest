"""
Собрали сервер из n разнородных процессоров и решили создать для него
простейший планировщик задач.
Сервер состоит из n процессоров. Процессоры разные, достигают одинаковой
скорости работы при разном энергопотреблении.
i-й процессов в нагрузке тратит ai энергии в секунду.
В качестве нагрузки приходит m Задач.
ti и li - момент времени прихода задачи и время ее выполнения в секундах.
В момент прихода задачи выбрать своббодный процессор с min энергопотреблением.
Если к моменту прихода задачи свободных процессоров нет, то задача отбрасывается.
Проц, на котором запущена задача будет занят ровно l секунд, то есть
освободится ровно в момент tj + lj, и в этот же момент уже может быть назначен
на другую задачу.
Нужно определить суммарное энергопотребление серва при обработке m задач.
В простое энергию не потребляют.
Входные данные
    В первой строке даны 2 целых числа n, m - кол-ко процессоров и задач.
    Во второй строке заданы n целых чисел - энергопотребление процессоров под нагрузкой в секунду.
    В следующих строках даны описания задач по одному в строке.
    в j-й строке заданы момент прихода и время выполнения.
Выходных данные
    Вывести число - суммарное энергопотребление сервера.
"""
import io, os, heapq


def gen_string(data):
    for line in data:
        time, time_dur = map(int, line.rstrip().split())
        yield time, time_dur

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
data = input()
n, m = map(int, data[0].rstrip().split())
processors = list(map(int, data[1].rstrip().split()))
a_dict = {}
res = 0
heapq.heapify(processors)
tasks = gen_string(data[2:])
for time, time_dur in tasks:
    print('time is {}, time_dur is {}'.format(time, time_dur))
    print('a_dict is ', a_dict)
    stop_list = [t for t in a_dict if t <= time]
    for t in stop_list:
        tmp = a_dict.pop(t)
        for i in tmp:
            heapq.heappush(processors, a_dict.pop(t))
    try:
        smallest = heapq.heappop(processors)
    except IndexError:
        print('processors is empty')
        continue
    a_dict.setdefault(time + time_dur, []).append(smallest)
    res += smallest * time_dur
print(res)
