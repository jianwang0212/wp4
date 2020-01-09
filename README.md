# WP4 -  [Oxford University AI Project](https://www.law.ox.ac.uk/unlocking-potential-artificial-intelligence-english-law)

## Unlocking the Potential of Artificial Intelligence for English Law

A project funded by the Industrial Strategy Challenge Fund's (ISCF) Next Generation Services Research Programme
and UK Research and Innovation (UKRI), run by researchers in the Oxford departments and faculties of Law, Economics,
Computer Science, Education and the Said Business School, in 2019 and 2020.

## Description
Web tool for machine learning annotation
1. Display JobText
2. Add/delete labels/keywords for each JobID
3. Add/delete category for the future RA to annotate
4. Show table of frequency of keywords
5. Dynamicly highlithing all the keywords


## Install & Run
'''shell
1. sudo apt-get update
2. sudo apt-get install python3-pip
3. sudo apt install python3-venv
4. git clone https://github.com/jianwang0212/wp4.git
5. python3 -m venv /root/wp4/venv
6. source venv/bin/activate && pip install --upgrade pip
7. cd wp4 && pip3 install -r requirements.txt
8.(freeze a requirement) pip freeze --local > requirement.txt
9. deactivate
10. cd wp4
11. export FLASK_APP=run.py
12. /root/wp4/venv/bin/python3 /root/wp4/venv/bin/flask run --host=0.0.0.0
'''
