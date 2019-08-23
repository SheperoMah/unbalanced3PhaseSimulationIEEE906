#!/usr/bin/env bash


sed 's/.* Bus1=\([0-9]*\).* Bus2=\([0-9]*\) .*/\1 \2/' ../Lines.txt > lineBuses.txt
sed 's/.* Load.\(.*\) .* Bus1=\([0-9]*\)\.\([0-9]\).*/\1 \2 \3/' ../Loads.txt > loadInfo.txt



./plotGrid.py ../Buscoords.txt lineBuses.txt loadInfo.txt






rm -f lineBuses.txt
rm -f loadInfo.txt
