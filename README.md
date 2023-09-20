# CMPUT 303/403 Grade Summarizer

Produces a grade summary for your progress so far.

Developed by Ian DeHaan and Zac Friggstad, curated by TAs.

## STILL IN THE TESTING PHASE!
Please report any issues to the course instructor by email.

## Features
The reporter will report the status of all problems from the weekly problem sets and open pools using the message ACCEPTED, ACCEPTED (LATE), or UNSOLVED. It will only report the ACCEPTED problems from the open pools to keep the clutter down.

The reporter currently does *not* account for:
* Missing headers (planned for a future version)
* Any accommodations (e.g. extensions for "excused absences")

This does not report project scores or seminar scores.

## Known issue!
It seems for some the submission time is reported in Sweden Time (Kattis home) and for others it is in Mountain Time. So if you see problems that are reported LATE but you know you solved them in time, it may be for this reason. This tool is unofficial and is only to help you track your progress in the course, we will ensure the final grades that are submitted are based on correct submission times. A future version of the tool will accept another command-line parameter to correct the reporting if the times seem off.

## Requirements

Required nonstandard libraries:
* bs4
* requests

### Usage

    python3 main.py <kattis-username> "<password>" <coursefile> [<seminar-total>] [<project-total>]

### Examples

    python3 main.py smith abc123 cmput303.txt

or

    python3 main.py smith abc123 cmput403.txt 8 13.5

### Parameter Explanation
* \<kattis-username\>:
You can see this by logging in to Kattis, clicking on "Profile Settings" in the dropdown upper-right corner, and then looking at "Username".

* \<password\>:
Your Kattis password (it will not be saved anywhere). Put quotes around it (may not be necessary unless you have certain characters like a slash).

* \<coursefile\>:
One of cmput303.txt or cmput403.txt, depending on which version of the course you are registered in.

* \<seminar-total\>:
Your total marks (out of 10) for the seminars. This is an optional parameter for CMPUT 403 students. It is not scraped.

* \<project-total\>:
Your total marks (out of 15) for the project. This is an optional parameter for CMPUT 403 students. It is not scraped. To use this optional parameter, you **must** have provided the seminar total option as well.
