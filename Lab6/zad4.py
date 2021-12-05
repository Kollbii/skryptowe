import sys
from itertools import groupby

# tab = [num.split()[0] for num in sys.stdin.read().replace(",", "").replace("\n", "")]
# print(tab)
# print([list(g) for k, g in groupby(tab)])

print(
    [list(int(g)) if type(g) == int else list(g) for k, g in groupby(
                [num.split()[0] for num in sys.stdin.read().replace(",", "").replace("\n", "")]
            )
    ]
)

# python -c "import sys;from itertools import groupby;"