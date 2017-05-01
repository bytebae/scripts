
#!/bin/bash

duration=500    # number of seconds to load the cpus
instances=24    # number of cpus to load

endtime=$(($(date +%s) + $duration))
for ((i=0; i<instances; i++))
do
    while (($(date +%s) < $endtime)); do :; done &
done
