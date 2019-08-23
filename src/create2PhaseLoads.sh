#!/usr/bin/env bash


# This file divides the load of each customer to two single phase loads, the idea is to repeat the load 
# of the customer on the following phase, i.e., phase += 1, and divide everything by 2. 


awk 'BEGIN {
  FS=" "
  printf(" ! Divide the original single phase loads to two phases. \n")
  printf(" ! Use two single phase loads each with the total load of the \n")
  printf(" ! customer and set the LoadMult=0.5, i.e., do 2 * loadCustomer * 0.5. \n")
  printf(" ! \n")
}
{
  split($0,lineDivideBus, "Bus1=")
  split(lineDivideBus[2],busNameAndPhase, " ")
  split(busNameAndPhase[1], phaseVar, ".") 
  if(phaseVar[2] < 3){newBus = phaseVar[2]+1}
  else {newBus = 1}
  print lineDivideBus[1]
  #for (i=2; i<=length(busNameAndPhase); i++){ printf(" %s", $i)} 
  printf(" \n") 
}
' $1



#  printf("%s", lineDivideBus[1])
#  printf("Bus1=%s.%s", phaseVar[1], newBus)
# for (i in busNameAndPhase) {printf("%s ",busNameAndPhase[i])}

 # printf(" %s %s_%s %s %s.%s ", $1, $2, phaseVar[2], $3, phaseVar[1], phaseVar[2])
 # for (i=5; i<=NF; i++){printf("%s ", $i)}
 # printf("\n")
 # printf(" %s %s_%s %s %s.%s ", $1, $2, newBus, $3, phaseVar[1], newBus)
 # for (i=5; i<=NF; i++){printf("%s ", $i)}
 # printf("\n")
