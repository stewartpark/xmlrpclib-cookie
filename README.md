xmlrpclib-cookie
=============

xmlrpclib-cookie provides a transport that enables xmlrpclib to retain cookie/session.

Example:

    import xmlrpclib_cookie
    import xmlrpclib

    RPC = xmlrpclib.ServerProxy('http://foo.bar:8080/', transport=xmlrpclib_cookie.CookieTransport())
    # or, for HTTPS connections, transport=xmlrpclib_cookie.SafeCookieTransport()


