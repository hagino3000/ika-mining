#!/bin/bash

for id in {500000..1027674};do
    http GET https://stat.ink/api/v1/battle?id=${id} | gzip > ../data/${id}.json.gz
    echo ${id}
    sleep 1
done
