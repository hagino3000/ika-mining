#!/bin/bash


echo start

for id in {500000..650000};do
    scp sakura:~/dev/ika/data/${id}.json.gz ../data/
    echo ${id}
done

echo END

