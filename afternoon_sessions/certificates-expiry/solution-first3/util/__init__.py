from datetime import datetime

def number_of_days_till_expire(ssl_date):

    try:
        expire_date = datetime.strptime(ssl_date,
                                        "%b %d %H:%M:%S %Y %Z")
    except Exception as e:
        raise Exception(e)

    expire_in = expire_date - datetime.now()
    if expire_in.days > 0:
        return expire_in.days
    else:
        return False
