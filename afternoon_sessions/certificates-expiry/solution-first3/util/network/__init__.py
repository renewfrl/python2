import ssl
from urllib.request import Request, urlopen, ssl, socket


def check_ssl_expiry_date(url):
    context = ssl.create_default_context() #create a SSL context
    with socket.create_connection((url,"443")) as sock: #open connection to the server
        with context.wrap_socket(sock, server_hostname=url) as ssock: #provide access to the SSL layer
            data = ssock.getpeercert() # get certificate
            return(ssock.version(), data['subjectAltName'][0][1], data['notAfter'])
