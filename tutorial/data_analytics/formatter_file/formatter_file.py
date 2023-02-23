
import numpy as np

OPTIONS = {}

def YNint(yn):
    return (0, 1)[yn.upper() in 'YES']

def nullint(x):
    try:
        return np.int64(x)
    except:
        return np.int64(-1)

#yellow_format = {'sep': ',','header': 0,'converters': {'adm0_id': nullint,'adm1_id': nullint,'mkt_id': nullint,'cm_id': nullint,
#'cur_id': nullint,'pt_id': nullint,'um_id': nullint,'mp_month': nullint,'mp_price': nullint,'conversion_rate': nullint}}

yellow_format = {'sep': ',','header': 0}

OPTIONS['yellow'] = yellow_format

#green_format = yellow_format.copy()
#green_format['parse_dates'] = ['lpep_dropoff_datetime', 'lpep_pickup_datetime']
#OPTIONS['green'] = green_format