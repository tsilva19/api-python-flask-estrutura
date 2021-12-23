import logging

from src import app
log = logging.getLogger()
log.setLevel(logging.INFO)

if __name__ == '__main__':

    app.run('0.0.0.0', 8080)
