import xmlrpclib
import zlib, gzip
from cStringIO import StringIO

class CookieTransportRequest(object):
    cookies = []

    def send_cookies(self, connection):
        if self.cookies:
            for cookie in self.cookies:
                connection.putheader("Cookie", cookie)

    def request(self, host, handler, request_body, verbose=0):
        self.verbose = verbose
        h = self.make_connection(host)
        if verbose:
            h.set_debuglevel(1)
        self.send_request(h, handler, request_body)
        self.send_host(h, host)
        self.send_cookies(h)
        self.send_user_agent(h)
        self.send_content(h, request_body)

        try:
            response = h.getresponse(buffering=True)
        except AttributeError:
            response = h._conn.getresponse()
        
        for header in response.msg.getallmatchingheaders("Set-Cookie"):
            val = header.split(":", 1)[1]
            cookie = val.split(";", 1)[0]
            self.cookies.append(cookie)

        if response.status != 200:
            raise xmlrpclib.ProtocolError(host + handler, response.status, response.reason, response.msg.headerS)
     
        if response.getheader("Content-Encoding") == "gzip":
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = response.read()

        parser, unmarshaller = self.getparser()
        parser.feed(data)
        parser.close()

        return unmarshaller.close()

class CookieTransport(CookieTransportRequest, xmlrpclib.Transport):
    def __init__(self, *args, **kwargs):
        xmlrpclib.Transport.__init__(self, *args, **kwargs)
        CookieTransportRequest.__init__(self)

class SafeCookieTransport(CookieTransportRequest, xmlrpclib.SafeTransport):
    def __init__(self, *args, **kwargs):
        xmlrpclib.SafeTransport.__init__(self, *args, **kwargs)
        CookieTransportRequest.__init__(self)

