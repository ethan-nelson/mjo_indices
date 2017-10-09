import datetime as dt
import numpy as np
import urllib2

URL = 'http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt'

def _retrieve():
    resp = urllib2.urlopen(URL)
    data = resp.read()

    return data


def _parse(data):
    d1 = data.split('\n')
    d2 = []
    for row in d1:
        d2.append(row.split())
    return d2[2:-1]


def _extract(data):
    # Columns are year, month, day, rmm1, rmm2, phase, amplitude, note. Missing values are 999 in phase.
    out = np.zeros([len(data), 4])
    for ir,row in enumerate(data):
        t = dt.datetime(int(row[0]), int(row[1]), int(row[2]))
        out[ir,:] = int(row[0]), t.timetuple().tm_yday, int(row[5]), float(row[6])
    return out


def load_indices():
    a = _retrieve()
    b = _parse(a)
    c = _extract(b)

    return c
