# !/bin/bash
# python benchmark_prefill.py --batch-size from 1 to 2000
for i in {1..2000}
do
    echo "$i"
    python benchmark_prefill.py --batch-size $i &> prefill.log
done
```