from util.network import check_ssl_expiry_date
from util.format import pretty_ssl_format


import csv

# Just a demo. Should be normalized further

def check_certs():

    res = []
    lst = ["ing.nl","twilio.com","rabobank.nl"]
    for item in lst:
       a = (version, name, date) = check_ssl_expiry_date(item)
       res.append(a)
    return res


def print_results_to_screen(res):
    for (v,n,d) in res:
        print(pretty_ssl_format(v,n,d))

def print_result_to_csv(res):
        with open("cert.csv", "w") as csvfile:
            certwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for (v, n, d) in res:
                certwriter.writerow([v,n,d])




