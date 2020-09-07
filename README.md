## Election Audits
Tools and ways to independently verify the results of CPU elections. Currently only the meeting time balloting has been implemented.

## Independent Auditing
To verify that your ballot was counted and included, run:
`check.py [email] [results json filename]`
where `[email]` is your email and `[results json filename]` is something like `elections/fall-2020-meeting-time/results.json`

For example, this is what Max's auditing step would look like:
```
python3 check.py mfan21@choate.edu elections/fall-2020-meeting-time/results.json
```

Check if the output corresponds to the choices you indicated on the form.

Now that you know that your ballot has not been tampered with, you can check if all the ballots were counted properly.

To do this, you can try to calculate the winner by hand or use some other method of your choosing.
The exact method is left up to the auditor.

Finally, you can take a look at the replication script `replicate.sh` to see the exact commands that were run to generate the election results.
This does not provide any security guarantees, but is helpful when debugging/trying to understand how everything worked.

## Results
https://www.condorcet.vote/Vote/8861A68EDA/

## Flaws
This does not prevent blatant vote-stuffing nor does it perfectly protect your privacy (don't worry, the leadership elections will be done differently) .
However, it does show that *your* vote was counted and weighted equally among all other ballots and gives you an idea of what meeting time works best for the club in general.

Given that people's meeting time preferences is not sensitive data, implementation time was prioritized over perfect theoretical election properties. 
Pull requests are welcome, though!


