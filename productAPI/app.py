import time
time.sleep(5) #TODO find a better solution

import os
import api
from api import flask_app

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8393, debug=True)
