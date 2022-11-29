from datetime import datetime
import json


def write_log(msq):
    """
    {'datetime': 'dt',
    'event': 'msq'
    }
    """
    log = {'datetime': datetime.now(),
           'event': msq
           }

    with open('logs.json', 'a+') as f:
        json.dump(log, f)
    return print('saved')
