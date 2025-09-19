# CMPUT 303/403 Grade Summarizer

Produces an unofficial grade summary for your progress so far.

Developed by Ian DeHaan and Zac Friggstad.

## STILL IN THE TESTING PHASE!
Please report any issues to the course instructor by email.

## Features
The reporter will report the status of all problems from the weekly problem sets using the message ACCEPTED, ACCEPTED (LATE), or UNSOLVED. It will only report the ACCEPTED problems from the open pools to keep the clutter down.

## IMPORTANT: Differences between this unofficial tool and your final grade

This unofficial tool does not look at the code in your submissions, so it reports your score assuming headers are there. It is your responsibility to ensure the header is in your code!

It also does not take into account any accommodations you might have received.

It scrapes all of your ualberta.kattis.com submissions. If you were able to submit to a problem outside of the "contest" link for that assignment (e.g. directly to ualberta.kattis.com/problems/andrewant instead of the link from the Weekly Assignment 1 page) then this tool will count it as submitted even though the final grade you receive only looks at the submissions made through the assignment page.

Finally, it does not "scrape" your project score since that will only appear on Canvas nor does it scrape your seminar score since it does not know about the teams that were formed. You will have to enter these manually into the command line arguments if you want them to factor in the reported grade summary.

## Instructions for Running

Required nonstandard libraries:
* bs4
* requests

### Usage

    python3 main.py <kattis-username> "<password>" <coursefile> [<seminar-score> <project-score>]

### Examples

    python3 main.py smith abc123 c303.txt

or

    python3 main.py smith abc123 c403.txt 8 12.5

### Parameter Explanation
* \<kattis-username\>:
You can see this by logging in to Kattis, clicking on "Profile Settings" in the dropdown upper-right corner, and then looking at "Username".

* \<password\>:
Your Kattis password (it will not be saved anywhere). Put quotes around it (may not be necessary unless you have certain characters like a slash).

* \<coursefile\>:
One of cmput303.txt or cmput403.txt, depending on which version of the course you are registered in.

* \<seminar-score\> OPTIONAL:
Only for 403 students. Given as a score between 0.0 and 10.0. If not provided, a value of 0.0 will be used by default.

* \<project-score\> OPTIONAL:
Only for 403 students. Given as a score between 0.0 and 15.0. If not provided, a value of 0.0 will be used by default.

### Known Issues
* Sometimes reports a problem as "LATE" for problems submitted close to the deadline.
  * SOLUTION: Go to your Kattis profile and change your preferred timezone to "America/Edmonton". You might also have to switch to a different timezone first, then switch back to Edmonton time.
We guarantee your final grade will be calculated with the correct submission times. Again, this is an unofficial tool for you to use.