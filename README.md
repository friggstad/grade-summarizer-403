# CMPUT 398/403 Grade Summarizer

Produces a grade summary for your progress so far.

Developed by Ian DeHaan and Zac Friggstad.

## STILL IN THE TESTING PHASE!
Please report any issues to the course instructor by email.

## Features
The reporter will report the status of all problems from the weekly problem sets using the message ACCEPTED, ACCEPTED (LATE), or UNSOLVED. It will only report the ACCEPTED problems from the open pools to keep the clutter down.

The reporter does *not* account for:
* Missing headers
* Any accommodations (i.e. extensions for "excused absences" reasons)

It will also never scrape your project score (for 403 students) since that will only appear on eClass. You will have to enter it manually.

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
