from flaskblog import db
from flaskblog.models import Keyword

dt = Keyword.query.all()

print(dt)
