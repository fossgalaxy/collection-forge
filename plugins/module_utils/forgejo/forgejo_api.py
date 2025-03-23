##
# Forgejo API client
#
# Used by some of the forgejo modules.
# based on: https://github.com/ansible-middleware/keycloak/blob/main/plugins/module_utils/identity/keycloak/keycloak.py
##

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import traceback

from ansible.module_utils.urls import open_url
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.common.text.converters import to_native, to_text

URL_USER = "{url}/users/{username}"

def get_token(module_params):

    token = module_params.get('token')
    base_url = module_params.get('auth_forgejo_url')
    
    if token is None:
        pass

    return {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
            }


class ForgejoError(Exception):
    pass

class FrogejoAPI(object):

    def __init__(self, module, connection_headers):
        self.module = module
        self.baseurl = self.module.params.get('auth_forgejo_url')
        self.restheaders = connection_headers

    def get_user_by_username(self, username):
        user_url = URL_USER.format(url=self.baseurl, username=username)

        try:
            return json.loads(to_native(open_url(user_url, method='GET', headers=self.restheaders).read()))
        except HTTPError as e:
            if e.code == 404:
                return None
            else:
                self.fail_open_url(e, msg="Could not get user '%s': %s" % (username, str(e)),
                                   exception.traceback.format_exc())
        except Exception as e:
            self.module.fail_json(msg="Could not get user '%s': %s" % (username, str(e)),
                                   exception.traceback.format_exc())
                                  )

    def fail_open_url(self, e, msg, **kwargs):
        try:
            if isinstance(e, HTTPError):
                msg = "%s: %s" % (msg, to_native(e.read()))
        except Exception as ignore:
            pass
        self.module.fail_json(msg, **kwargs)
