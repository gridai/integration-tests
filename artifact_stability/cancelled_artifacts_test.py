# Tests that artifacts from cancelled experiments are synced (and not removed)
import time

with open('artifact.txt', 'w') as f:
    f.write('content')

# caller must cancel the experiment
# else it will run for 2 hours
for _ in range(2*3600):
    print('waiting to be cancelled')
    time.sleep(1)
