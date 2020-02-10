# -*- coding: utf-8 -*-
"""
OpenVox sim information adapter
"""
__author__ = "Dmitrii Dubrov"
__copyright__ = "Copyright 2020"
__version__ = "1.0"

# //TODO login and password to settings.

import requests
from requests.auth import HTTPDigestAuth
import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self, ip, board, port, obj):
        if board is None or port is None or ip is None or obj is None:
            return cherrypy._cperror.HTTPError
        if int(board) == 0 or int(board) > 6:
            return "Parameters board = 0 or > 6. Edit parameters and try again late."
        if board == '1':
            req = requests.get('http://{0}/service?action=get_gsminfo'.format(ip),
                               auth=HTTPDigestAuth('admin', 'admin')).json()
            reg_sim = req[str(port)][0]['register']
            data_obj = req[str(port)][0][obj]
            if obj == 'signal' and 'Registered' not in reg_sim:
                data_obj = '0'
            return data_obj
        if int(board) > 1:
            req = requests.get('http://{0}/{1}/service?action=get_gsminfo'.format(ip, board),
                               auth=HTTPDigestAuth('admin', 'admin')).json()
            reg_sim = req[str(port)][0]['register']
            data_obj = req[str(port)][0][obj]
            if obj == 'signal' and 'Registered' not in reg_sim:
                data_obj = '0'
            return data_obj
        else:
            return "Error. Check all parameters and try again late."


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 9090, 'server.socket_host': '0.0.0.0'})
    tracebacks = cherrypy.request.show_tracebacks
    cherrypy.config.update({'request.show_tracebacks': not tracebacks})
    cherrypy.quickstart(Root(), '/')
