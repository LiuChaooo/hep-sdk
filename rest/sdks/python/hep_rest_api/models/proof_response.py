# coding: utf-8

"""
    HEP REST API

    The REST API for HEP protocol  # noqa: E501

    OpenAPI spec version: v1
    Contact: xiawu@zeuux.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from hep_rest_api.models.order import Order  # noqa: F401,E501


class ProofResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dapp_key': 'str',
        'protocol': 'str',
        'version': 'str',
        'ts': 'int',
        'nonce': 'str',
        'os': 'str',
        'language': 'str',
        'dapp_signature_method': 'str',
        'dapp_signature': 'str',
        'sign_type': 'str',
        'signature': 'str',
        'action': 'str',
        'uuid': 'str',
        'dapp_id': 'str',
        'content': 'Order'
    }

    attribute_map = {
        'dapp_key': 'dapp_key',
        'protocol': 'protocol',
        'version': 'version',
        'ts': 'ts',
        'nonce': 'nonce',
        'os': 'os',
        'language': 'language',
        'dapp_signature_method': 'dapp_signature_method',
        'dapp_signature': 'dapp_signature',
        'sign_type': 'sign_type',
        'signature': 'signature',
        'action': 'action',
        'uuid': 'uuid',
        'dapp_id': 'dapp_id',
        'content': 'content'
    }

    def __init__(self, dapp_key=None, protocol=None, version=None, ts=None, nonce=None, os=None, language=None, dapp_signature_method=None, dapp_signature=None, sign_type=None, signature=None, action=None, uuid=None, dapp_id=None, content=None):  # noqa: E501
        """ProofResponse - a model defined in Swagger"""  # noqa: E501
        self._dapp_key = None
        self._protocol = None
        self._version = None
        self._ts = None
        self._nonce = None
        self._os = None
        self._language = None
        self._dapp_signature_method = None
        self._dapp_signature = None
        self._sign_type = None
        self._signature = None
        self._action = None
        self._uuid = None
        self._dapp_id = None
        self._content = None
        self.discriminator = None
        self.dapp_key = dapp_key
        self.protocol = protocol
        self.version = version
        self.ts = ts
        self.nonce = nonce
        self.os = os
        self.language = language
        self.dapp_signature_method = dapp_signature_method
        self.dapp_signature = dapp_signature
        self.sign_type = sign_type
        self.signature = signature
        self.action = action
        self.uuid = uuid
        self.dapp_id = dapp_id
        self.content = content

    @property
    def dapp_key(self):
        """Gets the dapp_key of this ProofResponse.  # noqa: E501

        The decentralized application access key  # noqa: E501

        :return: The dapp_key of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_key

    @dapp_key.setter
    def dapp_key(self, dapp_key):
        """Sets the dapp_key of this ProofResponse.

        The decentralized application access key  # noqa: E501

        :param dapp_key: The dapp_key of this ProofResponse.  # noqa: E501
        :type: str
        """
        if dapp_key is None:
            raise ValueError("Invalid value for `dapp_key`, must not be `None`")  # noqa: E501

        self._dapp_key = dapp_key

    @property
    def protocol(self):
        """Gets the protocol of this ProofResponse.  # noqa: E501

        The protocol name. default is 'HEP'.  # noqa: E501

        :return: The protocol of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ProofResponse.

        The protocol name. default is 'HEP'.  # noqa: E501

        :param protocol: The protocol of this ProofResponse.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self):
        """Gets the version of this ProofResponse.  # noqa: E501

        The protocol version such as '1.0'  # noqa: E501

        :return: The version of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProofResponse.

        The protocol version such as '1.0'  # noqa: E501

        :param version: The version of this ProofResponse.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def ts(self):
        """Gets the ts of this ProofResponse.  # noqa: E501

        The current timestamp  # noqa: E501

        :return: The ts of this ProofResponse.  # noqa: E501
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this ProofResponse.

        The current timestamp  # noqa: E501

        :param ts: The ts of this ProofResponse.  # noqa: E501
        :type: int
        """
        if ts is None:
            raise ValueError("Invalid value for `ts`, must not be `None`")  # noqa: E501

        self._ts = ts

    @property
    def nonce(self):
        """Gets the nonce of this ProofResponse.  # noqa: E501

        The random string or auto-increment sequence  # noqa: E501

        :return: The nonce of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this ProofResponse.

        The random string or auto-increment sequence  # noqa: E501

        :param nonce: The nonce of this ProofResponse.  # noqa: E501
        :type: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def os(self):
        """Gets the os of this ProofResponse.  # noqa: E501

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :return: The os of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ProofResponse.

        The operating system of client such as ios, android, dweb,etc.  # noqa: E501

        :param os: The os of this ProofResponse.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def language(self):
        """Gets the language of this ProofResponse.  # noqa: E501

        The i18n language code such as zh, en, etc.  # noqa: E501

        :return: The language of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ProofResponse.

        The i18n language code such as zh, en, etc.  # noqa: E501

        :param language: The language of this ProofResponse.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def dapp_signature_method(self):
        """Gets the dapp_signature_method of this ProofResponse.  # noqa: E501

        The signature method used by dapp.  # noqa: E501

        :return: The dapp_signature_method of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature_method

    @dapp_signature_method.setter
    def dapp_signature_method(self, dapp_signature_method):
        """Sets the dapp_signature_method of this ProofResponse.

        The signature method used by dapp.  # noqa: E501

        :param dapp_signature_method: The dapp_signature_method of this ProofResponse.  # noqa: E501
        :type: str
        """
        if dapp_signature_method is None:
            raise ValueError("Invalid value for `dapp_signature_method`, must not be `None`")  # noqa: E501

        self._dapp_signature_method = dapp_signature_method

    @property
    def dapp_signature(self):
        """Gets the dapp_signature of this ProofResponse.  # noqa: E501

        The signature generated by dapp.  # noqa: E501

        :return: The dapp_signature of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_signature

    @dapp_signature.setter
    def dapp_signature(self, dapp_signature):
        """Sets the dapp_signature of this ProofResponse.

        The signature generated by dapp.  # noqa: E501

        :param dapp_signature: The dapp_signature of this ProofResponse.  # noqa: E501
        :type: str
        """
        if dapp_signature is None:
            raise ValueError("Invalid value for `dapp_signature`, must not be `None`")  # noqa: E501

        self._dapp_signature = dapp_signature

    @property
    def sign_type(self):
        """Gets the sign_type of this ProofResponse.  # noqa: E501

        The signature Type,aka cryptographic algorithm.  # noqa: E501

        :return: The sign_type of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this ProofResponse.

        The signature Type,aka cryptographic algorithm.  # noqa: E501

        :param sign_type: The sign_type of this ProofResponse.  # noqa: E501
        :type: str
        """
        if sign_type is None:
            raise ValueError("Invalid value for `sign_type`, must not be `None`")  # noqa: E501

        self._sign_type = sign_type

    @property
    def signature(self):
        """Gets the signature of this ProofResponse.  # noqa: E501

        The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].  # noqa: E501

        :return: The signature of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ProofResponse.

        The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].  # noqa: E501

        :param signature: The signature of this ProofResponse.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def action(self):
        """Gets the action of this ProofResponse.  # noqa: E501

        The action name which value is 'hep.proof.submit'.  # noqa: E501

        :return: The action of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ProofResponse.

        The action name which value is 'hep.proof.submit'.  # noqa: E501

        :param action: The action of this ProofResponse.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def uuid(self):
        """Gets the uuid of this ProofResponse.  # noqa: E501

        The request uuid  # noqa: E501

        :return: The uuid of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProofResponse.

        The request uuid  # noqa: E501

        :param uuid: The uuid of this ProofResponse.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def dapp_id(self):
        """Gets the dapp_id of this ProofResponse.  # noqa: E501

        The decentralized application ID  # noqa: E501

        :return: The dapp_id of this ProofResponse.  # noqa: E501
        :rtype: str
        """
        return self._dapp_id

    @dapp_id.setter
    def dapp_id(self, dapp_id):
        """Sets the dapp_id of this ProofResponse.

        The decentralized application ID  # noqa: E501

        :param dapp_id: The dapp_id of this ProofResponse.  # noqa: E501
        :type: str
        """
        if dapp_id is None:
            raise ValueError("Invalid value for `dapp_id`, must not be `None`")  # noqa: E501

        self._dapp_id = dapp_id

    @property
    def content(self):
        """Gets the content of this ProofResponse.  # noqa: E501


        :return: The content of this ProofResponse.  # noqa: E501
        :rtype: Order
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ProofResponse.


        :param content: The content of this ProofResponse.  # noqa: E501
        :type: Order
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProofResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProofResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
