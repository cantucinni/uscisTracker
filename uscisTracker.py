#!/usr/bin/python
import requests
import re
import os

def PostData(caseid):

    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'

    payload = {
        "appReceiptNum": caseid}

    r = requests.post(url, data=payload)

    if 200 != r.status_code:
        return None
    m = re.search("<h1>(.+?)</h1>\s+<p>(.+?)</p>", r.text)
    if m:
        #return "{0}<br>{1}".format(m.group(1), m.group(2))
        return "{0}".format(m.group(1))

    return None

def DoMyStuff():

    if not os.path.exists("cases.txt"):
        print("Cases.txt does not exist. Please add USCIS cases in cases.txt (one case per line)")
        return

    cases = [a.strip() for a in open("cases.txt").readlines()]

    if len(cases) == 0:
        print("No cases found. Please add USCIS cases in cases.txt (one case per line)")
        return

    for case in cases:
        ret = PostData(case)
        txt = ""
        if None == ret:
            print("Case {0}: [error]".format(ret))
        else:
            print("Case {0}: {1}".format(case, ret))

    print("\nDone.")

if __name__ == '__main__':
    DoMyStuff()