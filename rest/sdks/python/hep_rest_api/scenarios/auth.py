"""The implementation of HEP Authentication protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
import datetime
from hep_rest_api.scenarios import BaseHelper
from hep_rest_api import models

logger = logging.getLogger(__name__)


class AuthHelper(BaseHelper):

    def generate_auth_request(self, scope=1, expired=300, memo='', uuid=None):
        """Generate the authentication request

        :param int scope: The request scope. 1: base profile including name,head,newid; 2: advance profile including cellphone.
        :param int expired: The expired time of request
        :param str memo: The memo of request to end user
        :param str uuid: The request uuid for desktop-browser. optional.
        :rtype: dict
        :return: The request information including signature
        """
        if not uuid:
            raise AttributeError(
                "uuid can not be None"
            )
        if not memo:
            memo = "default"
        data = {
            'action': self.action_auth_login,
            'scope': scope,
            'expired': int(datetime.datetime.now().timestamp()) + expired,
            'memo': memo,
            'uuid': uuid
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        final_data = self.sign_secp256r1(hmac_data)
        # start request
        auth_cache = models.AuthCacheRequest(**final_data)
        auth_response = self.api_client.rest_newnet_caches_auth_create(auth_cache, self.api_version)
        return auth_response


    def generate_qrcode_string(self, auth_request):
        """Generate the hep-based scheme string string for QRCode 
        
        :param dict auth_request: The auth request
        :rtype: str
        :return: The QRcode string
        """
        auth_hash = auth_request.auth_hash
        protocol = self.base_parameters.get('protocol')
        dapp_id = self.base_parameters.get('dapp_id')
        action = self.action_auth_login
        qrcode_str = "%s://%s/?action=%s&auth_hash=%s" % (protocol, dapp_id, action, auth_hash)
        return qrcode_str

    def validate_auth_callback(self, data):
        """Validate the response of auth callback sent by end users such as NewPay users 
        
        :param dict data: The callback data
        :rtype: bool
        :return: True if valid data, otherwise False
        """
        pass