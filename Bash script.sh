#!/bin/bash
for ((i=1;i<101;i++)); do
        mkdir DDM$i
        cd DDM$i
        echo "nanoseconds since 1970-01-01 00:00:00 UTC: " > time_till_now.txt
        date "+%s" >> time_till_now.txt
        cd ..
done