for x in {1..$1}
do
    echo $x
    python long-birds.csv
    grep -i michigan long-birds.csv | grep -i october |sort -k 1 -t,
done > newfile2.txt && cat newfile2.txt
