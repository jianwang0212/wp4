Installing python 3 on a new server

1. sudo apt-get update
2. sudo apt-get install python3-pip
3. sudo apt install python3-venv
4. git clone https://github.com/jianwang0212/wp4.git
5. python3 -m venv /root/wp4/venv
6. source venv/bin/activate && pip install --upgrade pip
7. cd wp4 && pip3 install -r requirements.txt 

export FLASK_APP=run.py
nohup flask run --host=0.0.0.0



In local mac:

1. python3 -m venv /Users/Zi/Google\ Drive/wp4/venv
2. pip3 install -r requirements.txt  && pip install --upgrade pip
3. cd /Users/Zi/Google\ Drive/wp4


export FLASK_APP=run.py
flask run --host=0.0.0.0


reference instruction:
https://www.youtube.com/watch?v=goToXTC96Co