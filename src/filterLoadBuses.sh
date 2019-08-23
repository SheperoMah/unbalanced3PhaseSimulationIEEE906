#!/usr/bin/env bash


BusNumbers=`sed 's/^.*Bus1=\([0-9]*\)\..*/\1/' ../Loads.txt | sort -u`

monitorsFile="!Monitors"
exportingFile="!Export Monitors"
# For loop on the bus numbers of the loads
for i in $BusNumbers; do
    busString="Bus2="
    searchString="$busString$i\s"
    lineString=`grep $searchString Lines.txt`
    lineCode=`echo $lineString | sed 's/^[^\.]*\.\([^ ]*\) .*/\1/'`
    monitorName="Bus_$i"
    monitorString="New Monitor.$monitorName Line.$lineCode Terminal=2 Mode=0"
    monitorsFile=$(cat << EOF 
$monitorsFile
$monitorString
EOF
)

    exportString="Export Monitors $monitorName"
    exportingFile=$(cat << EOF
$exportingFile
$exportString
EOF
)
done

echo -e "$monitorsFile" > ../Monitors.txt
echo -e "$exportingFile" > ../Exporting.txt
