#!/bin/bash
for i in {1..3}
do
python ./worker.py  2>&1 &
done