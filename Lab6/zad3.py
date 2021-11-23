import sys
import functools

print(
    len(
        list(
            filter(lambda x: int(x)%2==0,
                functools.reduce(
                    lambda x, y: x + y, list(
                        open(file, 'r').read().replace('\n', ' ').split() for file in sys.argv[1:]
                    )
                )
            )
        )
    )
)
#$> python -c "import sys;import functools;print(len(list(filter(lambda x: int(x)%2==0,functools.reduce(lambda x, y: x + y, list(open(file, 'r').read().replace('\\n', ' ').split() for file in sys.argv[1:]))))))" plik1.txt plik2.txt
