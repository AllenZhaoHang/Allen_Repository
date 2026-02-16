#!/bin/bash

make -s

SCHEMES="fcfs sjf psjf pri ppri rr1 rr2 rr4"
PROCS="proc1 proc2"

for proc in $PROCS; do
    for scheme in $SCHEMES; do
        echo "Testing $scheme on examples/$proc.csv..."
        ./simulator $scheme examples/$proc.csv > my_${proc}_${scheme}.out
        
        # Compare last 5 lines ignoring whitespace differences
        diff -w <(tail -n 5 my_${proc}_${scheme}.out) <(tail -n 5 examples/${proc}-${scheme}.out)
        
        if [ $? -eq 0 ]; then
            echo "PASS"
        else
            echo "FAIL"
            echo "Expected:"
            tail -n 5 examples/${proc}-${scheme}.out
            echo "Got:"
            tail -n 5 my_${proc}_${scheme}.out
        fi
        echo "--------------------------------"
    done
done
