python make-big-birdlist.py
grep -i october long-birds.csv | grep -i michigan | sort -k 1 -t, -n > michigan_october.txt && cat michigan_october.txt
