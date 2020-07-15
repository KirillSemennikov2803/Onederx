import datetime

"""
Convert js utc timestamp to python datetime.
js code to get utc timestamp:
    Date.now()
"""


def jsts_2_python_datetime(jsts):
    return datetime.datetime.fromtimestamp(jsts / 1000)


"""
Convert python timestamp to js utc timestamp.
"""


def python_datetime_2_jsts(dt):
    return int(int(dt.strftime("%s%f")) / 1000)
