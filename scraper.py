from bs4 import BeautifulSoup
import requests
import datetime
import os
import json


_HEADERS = {'User-Agent': 'kattis-scraper'}
loginurl = "https://open.kattis.com/login"

def login(s, login_url, username, password=None, token=None):
    """Log in to Kattis.
    At least one of password or token needs to be provided.
    Returns a requests.
    Response with cookies needed to be able to submit.
    """
    login_args = {'user': username, 'script': 'true'}
    if password:
        login_args['password'] = password
    if token:
        login_args['token'] = token

    return s.post(login_url, data=login_args, headers=_HEADERS)

def getSolvedProblems(session, user, course_start):
    current_day = datetime.date.today()

    url = "https://ualberta.kattis.com/users/" + user

    print("scraping", url)
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    out = dict()
    while True:
        trs = soup.findAll('tr')

        for problem in trs:
            # print("tr:", problem)

            status_td = problem.find("div", {"class": "status is-status-accepted"})
            if not status_td:
                # either the row is not for a submission or the
                # submission was not accepted
                continue

            problem_title_td = problem.find("td", {"data-type": "problem"})

            # if not problem_title_td:
            #     # this can happen for multiple reasons
            #     # in general just use this to skip junk trs
            #     continue

            # there is probably a better way to do this
            for element in problem_title_td:
                problem_id = element["href"].split("/")[-1]

            # problem_title = problem_title_td.find("a").string

            time_formatted = problem.find("td", {"data-type": "time"}).string.strip()
            try:
                date_time = datetime.datetime.strptime(time_formatted, "%Y-%m-%d %H:%M:%S")
            except:
                # kattis sometimes does not display the date if submission was recent enough
                time_formatted = str(current_day) + " " + time_formatted
                date_time = datetime.datetime.strptime(time_formatted, "%Y-%m-%d %H:%M:%S")

            if date_time < course_start:
                continue

            if problem_id not in out:
                out[problem_id] = date_time
            out[problem_id] = min(out[problem_id], date_time)

        # determine if there is a "next" page
        buttons = soup.findAll('a', {'id': 'problem_list_previous'})
        next_url = None
        for button in buttons:
            if button.text == "Next":
                # lazy way to check if "href" is in the button
                # (if not, then this is the unclickable greyed out button)
                try:
                    next_url = button["href"]
                except:
                    pass

        if next_url:
            link = url + "/" + next_url

            print("scraping", link)
            r = session.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')
        else:
            break

    return out

def getAllSolvedProblems(username, password, course_start):
    # IMPORTANT: This won't check for recency of data, so make sure to delete
    # cache if you previously ran this before the end of the course.
    session = requests.Session()
    if login(session, loginurl, username, password).text != "Login successful":
        print("Couldn't log you in. Are you sure you're using the right username/password?")
        quit()

    print("successfully logged in")
    print("retrieving submissions...")

    solved = getSolvedProblems(session, username, course_start)

    return solved
