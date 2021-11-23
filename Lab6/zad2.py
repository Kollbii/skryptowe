import sys
import collections

print(
    dict(
        sorted(collections.Counter(
            [len(x) for x in sys.stdin.read().split()]).items()
        )
    )
)

# $> python -c "import sys; import collections; print(dict(sorted(collections.Counter([len(x) for x in sys.stdin.read().split()]).items())))"