from run import app

if __name__ == "__main__":
    app.run()
else:
    gunicorn_app = app