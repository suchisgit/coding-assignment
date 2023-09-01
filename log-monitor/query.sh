#!/bin/bash

if [[ $# -ne 1 ]]; then
  echo "Invalid number of arguments"
  exit 1
fi;
path=$1
# echo $path
while [ 2 -gt 1 ];
do
  echo -ne ">"
  read -r var
  # echo $var
  reg=QUERY*
  if [[ "$var" = "EXIT" ]];
  then
      exit 0
  elif [[ "$var" =~ $reg ]];
  then
      arrArgs=(${var// / }) #spliting with space
      if [[ ${#arrArgs[@]} -eq 7 ]]; then
        python3 filterLog.py ${arrArgs[1]} ${arrArgs[2]} ${arrArgs[3]} ${arrArgs[4]} ${arrArgs[5]} ${arrArgs[6]} $path
      else
        echo "Invalid command!!!"
      fi;
  else
      echo "Invalid Option"
  fi;
done
