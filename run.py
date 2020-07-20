from app import app


#if not os.path.exists('data.sqlite'):
#    db.create_all()

from app import routes

if __name__ == '__main__':
    app.run()