import os
import api
import time
from api import flask_app

if __name__ == '__main__':
    time.sleep(10) #TODO find a better solution
    flask_app.run(host='0.0.0.0', port=8393, debug=True)
