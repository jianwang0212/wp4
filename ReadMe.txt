################## Installing python 3 on a new server ##################


1. sudo apt-get update
2. sudo apt-get install python3-pip
3. sudo apt install python3-venv
4. git clone https://github.com/jianwang0212/wp4.git
5. python3 -m venv /root/wp4/venv
6. source venv/bin/activate && pip install --upgrade pip
7. cd wp4 && pip3 install -r requirements.txt
8.(freeze a requirement) pip freeze --local > requirement.txt
9. deactivate

ps aux| grep python
kill -9 'the python'
cd wp4
export FLASK_APP=run.py
/root/wp4/venv/bin/python3 /root/wp4/venv/bin/flask run --host=0.0.0.0
http://173.230.137.72:5000/
nohup /root/wp4/venv/bin/python3 /root/wp4/venv/bin/flask run --host=0.0.0.0

################## reset database ##################
/root/wp4/venv/bin/python3 /root/wp4/reset_dt.py

rm /root/wp4/flaskblog/site.db

################## In local mac: ##################

1. python3 -m venv /Users/Zi/Google\ Drive/wp4/venv
2. pip3 install -r requirements.txt  && pip install --upgrade pip
3. cd /Users/Zi/Google\ Drive/wp4

debug mode: ## don't use virtual environment
python run.py

export FLASK_APP=run.py
flask run --host=0.0.0.0

################## transfer data from server ##################
rsync -avz -e ssh root@173.230.137.72:/root/wp4/flaskblog/29_dec_site.db /Users/Zi/Downloads --exclude='env' --exclude='*.py'


#### Get a look at the db ###
sqlite3 site.db
select * from test;

reference instruction:
https://www.youtube.com/watch?v=goToXTC96Co
