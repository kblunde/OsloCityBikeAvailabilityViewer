from datetime import datetime


def findUTCOffest():
    utc_offset_min = int(round((datetime.now() - datetime.utcnow()).total_seconds())) / 60   # round for taking time twice
    utc_offset_h = utc_offset_min / 60
    return utc_offset_h
