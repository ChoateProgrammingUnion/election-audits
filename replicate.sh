# Exact commands that were run for replication purposes

python3 anonymize.py elections/fall-2020-meeting-time/ballots.csv
jsonlint -i results.json
mv results.json elections/fall-2020-meeting-time/results.json
python3 count.py elections/fall-2020-meeting-time/results.json
