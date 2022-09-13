import io, os


def gen_idxs(data, n_sets, i=1):
    for _ in range(n_sets):
        cnt = int(data[i])
        idx = i + 1
        i = idx + cnt
        yield idx, cnt

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
data = input()