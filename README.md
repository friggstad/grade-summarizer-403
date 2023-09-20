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

    python3 main.py <kattis-username> "<password>" <coursefile>

### Examples

    python3 main.py smith abc123 cmput303.txt

or

    python3 main.py smith abc123 cmput303.txt

### Parameter Explanation
* \<kattis-username\>:
You can see this by logging in to Kattis, clicking on "Profile Settings" in the dropdown upper-right corner, and then looking at "Username".

* \<password\>:
Your Kattis password (it will not be saved anywhere). Put quotes around it (may not be necessary unless you have certain characters like a slash).

* \<coursefile\>:
One of cmput398.txt or cmput403.txt, depending on which version of the course you are registered in.

* \<project-grade\> OPTIONAL:
Only for 403 students. Given as a score between 0.0 and 20.0. If not provided, a value of 0.0 will be used by default.
