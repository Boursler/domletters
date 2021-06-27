#!/bin/bash

files=("swift" "sentence" "97")

sol=(71 20 1)
for i in ${!sol[@]};
    do
        out=$(./domletters.py <${files[$i]}.txt)
        if [[ $out -eq ${sol[$i]} ]]
        then
              echo "pass test $i $out == ${sol[$i]}"
        else
            echo "fail test $i $out != ${sol[$i]}"
        fi
done
