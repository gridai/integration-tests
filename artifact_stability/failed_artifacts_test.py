# Tests that artifacts generated before a failure are synced (and not removed)

with open('artifact.txt', 'w') as f:
    f.write('content')

raise Exception()
