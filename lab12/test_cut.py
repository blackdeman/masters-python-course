import sys

sys.path.append("..")

import cut

print cut.cut("input.txt", [1, 0, 2])

print cut.cut("input-symbol.txt", [0, 1], '%')
