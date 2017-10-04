import requests
import json


class CredentialException(Exception):
    pass


class HTTPException(Exception):
    pass


class NotConnected(Exception):
    pass


class Aruba:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def Connect(self):
        data = [
          ('credential_0', self.username),
          ('credential_1', self.password),]
        r = requests.post(
                        'https://activate.arubanetworks.com/LOGIN',
                        data=data)
        if r.status_code == 200:
            self.connection = r
            return True
        elif r.status_code == 403:
            raise CredentialException("Invalid credentials.")
        elif r.status_code == 404:
            raise HTTPException("Unable to contact Activate server.")
        else:
            return False

    def SearchInventory(self, mac=None, serial=None, name=None):
        func_parameters = locals()
        for key in func_parameters.keys():
            if func_parameters[key] is not None and key is not "self":
                search_terms = func_parameters[key]
        if serial is not None:
            query_variables = '{"serialNumbers":["'
        elif mac is not None:
            query_variables = '{"devices":["'
        elif name is not None:
            query_variables = '{"deviceNames":["'
        params = (
                ('action', 'query'),
                )
        if type(search_terms) is list:
            for s in search_terms[:-1]:
                query_variables = query_variables + str(s) + '",'
            query_variables = query_variables + '"' + search_terms[-1] + '"]}'
        else:
            query_variables = query_variables + search_terms + '"]}'
        data = [('json', query_variables)]
        try:
            p = requests.post(
                'https://activate.arubanetworks.com/api/ext/inventory.json',
                params=params,
                cookies=self.connection.cookies,
                data=data)
        except AttributeError:
            raise NotConnected("Use the .Connect() method.")
        self.Last_Query_Result = json.loads(p.text)
        return self.Last_Query_Result

    def ProvisionRAP(
            self,
            mac,
            rap_user_name=None,
            rap_name=None,
            folder_group=None):
        self.data = [('json',
                      '{"devices":[{"mac":"'
                      + mac
                      + '","deviceName":"'
                      + rap_name +
                      '","deviceFullName":"'
                      + rap_user_name
                      + '", "folderId":"'
                      + folder_group}]}'),]
        params = (('action', 'update'),)
        f = requests.post(
            'https://activate.arubanetworks.com/api/ext/inventory.json',
            params=params,
            cookies=self.connection.cookies,
            data=self.data)
        return True
