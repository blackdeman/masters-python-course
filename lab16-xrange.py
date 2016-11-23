from collections import Sequence, Iterator


class xrangep(object):

    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError('xrange() requires 1-3 int arguments')

        try:
            start, stop, step = int(start), int(stop), int(step)
        except ValueError:
            raise TypeError('an integer is required')

        if step == 0:
            raise ValueError('xrange() arg 3 must not be zero')
        elif step < 0:
            stop = min(stop, start)
        else:
            stop = max(stop, start)

        self._start = start
        self._stop = stop
        self._step = step
        self._len = (stop - start) // step + bool((stop - start) % step)

    def __repr__(self):
        if self._start == 0 and self._step == 1:
            return 'xrangep(%d)' % self._stop
        elif self._step == 1:
            return 'xrangep(%d, %d)' % (self._start, self._stop)
        return 'xrangep(%d, %d, %d)' % (self._start, self._stop, self._step)

    def __eq__(self, other):
        return isinstance(other, xrange) and \
               self._start == other._start and \
               self._stop == other._stop and \
               self._step == other._step

    def __len__(self):
        return self._len

    def __reversed__(self):
        sign = self._step / abs(self._step)
        last = self._start + ((self._len - 1) * self._step)
        return xrangep(last, self._start - sign, -1 * self._step)

    def __getitem__(self, index):
        if index < 0:
            index += self._len
        if index < 0 or index >= self._len:
            raise IndexError('xrange object index out of range')
        return self._start + index * self._step

    def __iter__(self):
        return xrangeiterator(self)


class xrangeiterator(Iterator):

    def __init__(self, xrangeobj):
        self._xrange = xrangeobj

        self._last = self._xrange._start - self._xrange._step
        self._count = 0

    def __iter__(self):
        return self

    def next(self):
        self._last += self._xrange._step
        self._count += 1
        if self._count > self._xrange._len:
            raise StopIteration()
        return self._last

print list(reversed(xrangep(1, 10, 2)))