from collections.abc import Sequence

class SparseArray:
    def __init__(self, seq):
        if isinstance(seq, Sequence):
            self.values = dict()
            for _ in range(len(seq)):
                if (seq[_] !=0): self.values[_] = seq[_]
        else:
            raise TypeError('Not a Sequence')

    def append(self, value):
        self.values[self.length()] = value

    def lenght(self):
        values = []
        for key in self.values: values.append(int(key))
        values.sort()
        return values[-1] + 1

    def __len__(self):
        return self.lenght()

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                key += self.lenght()
            if key in self.values:
                return self.values[key]
            elif (0 <= key < self.lenght()):
                return 0
            else:
                raise IndexError('Index out of range')

        elif isinstance(key, slice):
            values = []
            slice_val = [key.start, key.stop, key.step]
            for _ in range(2):
                if slice_val[_] == None: slice_val[_] = 0
            if slice_val[2] == None: slice_val[2] = 1
            for _ in range(slice_val[0], slice_val[1], slice_val[2]):
                if _ in self.values:
                    values.append(self.values[_])
                elif _ < self.lenght():
                    values.append(0)
            return values

    def __setitem__(self, key, value):
        if value != 0:
            self.values[key] = value

    def __delitem__(self, key):
        if key in self.values:
            del self.values[key]


sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
