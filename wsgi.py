from application import create_app, db
from flask_migrate import Migrate


answer = create_app()
app = answer[0]
db = answer[1]
migrate = Migrate(app, db)


if __name__ == "__main__":

    print("sweet")
    app.run()
