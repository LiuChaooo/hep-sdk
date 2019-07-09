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


class ProofReward(object):
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
        'proof_hash': 'str',
        'proof_item_id': 'str',
        'proof_subitem_id': 'str',
        'earn_tokens': 'str',
        'newid': 'str',
        'newforce': 'str'
    }

    attribute_map = {
        'proof_hash': 'proof_hash',
        'proof_item_id': 'proof_item_id',
        'proof_subitem_id': 'proof_subitem_id',
        'earn_tokens': 'earn_tokens',
        'newid': 'newid',
        'newforce': 'newforce'
    }

    def __init__(self, proof_hash=None, proof_item_id=None, proof_subitem_id=None, earn_tokens=None, newid=None, newforce=None):  # noqa: E501
        """ProofReward - a model defined in Swagger"""  # noqa: E501
        self._proof_hash = None
        self._proof_item_id = None
        self._proof_subitem_id = None
        self._earn_tokens = None
        self._newid = None
        self._newforce = None
        self.discriminator = None
        self.proof_hash = proof_hash
        self.proof_item_id = proof_item_id
        self.proof_subitem_id = proof_subitem_id
        self.earn_tokens = earn_tokens
        self.newid = newid
        self.newforce = newforce

    @property
    def proof_hash(self):
        """Gets the proof_hash of this ProofReward.  # noqa: E501


        :return: The proof_hash of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._proof_hash

    @proof_hash.setter
    def proof_hash(self, proof_hash):
        """Sets the proof_hash of this ProofReward.


        :param proof_hash: The proof_hash of this ProofReward.  # noqa: E501
        :type: str
        """
        if proof_hash is None:
            raise ValueError("Invalid value for `proof_hash`, must not be `None`")  # noqa: E501

        self._proof_hash = proof_hash

    @property
    def proof_item_id(self):
        """Gets the proof_item_id of this ProofReward.  # noqa: E501


        :return: The proof_item_id of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._proof_item_id

    @proof_item_id.setter
    def proof_item_id(self, proof_item_id):
        """Sets the proof_item_id of this ProofReward.


        :param proof_item_id: The proof_item_id of this ProofReward.  # noqa: E501
        :type: str
        """
        if proof_item_id is None:
            raise ValueError("Invalid value for `proof_item_id`, must not be `None`")  # noqa: E501

        self._proof_item_id = proof_item_id

    @property
    def proof_subitem_id(self):
        """Gets the proof_subitem_id of this ProofReward.  # noqa: E501


        :return: The proof_subitem_id of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._proof_subitem_id

    @proof_subitem_id.setter
    def proof_subitem_id(self, proof_subitem_id):
        """Sets the proof_subitem_id of this ProofReward.


        :param proof_subitem_id: The proof_subitem_id of this ProofReward.  # noqa: E501
        :type: str
        """
        if proof_subitem_id is None:
            raise ValueError("Invalid value for `proof_subitem_id`, must not be `None`")  # noqa: E501

        self._proof_subitem_id = proof_subitem_id

    @property
    def earn_tokens(self):
        """Gets the earn_tokens of this ProofReward.  # noqa: E501


        :return: The earn_tokens of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._earn_tokens

    @earn_tokens.setter
    def earn_tokens(self, earn_tokens):
        """Sets the earn_tokens of this ProofReward.


        :param earn_tokens: The earn_tokens of this ProofReward.  # noqa: E501
        :type: str
        """
        if earn_tokens is None:
            raise ValueError("Invalid value for `earn_tokens`, must not be `None`")  # noqa: E501

        self._earn_tokens = earn_tokens

    @property
    def newid(self):
        """Gets the newid of this ProofReward.  # noqa: E501


        :return: The newid of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._newid

    @newid.setter
    def newid(self, newid):
        """Sets the newid of this ProofReward.


        :param newid: The newid of this ProofReward.  # noqa: E501
        :type: str
        """
        if newid is None:
            raise ValueError("Invalid value for `newid`, must not be `None`")  # noqa: E501

        self._newid = newid

    @property
    def newforce(self):
        """Gets the newforce of this ProofReward.  # noqa: E501


        :return: The newforce of this ProofReward.  # noqa: E501
        :rtype: str
        """
        return self._newforce

    @newforce.setter
    def newforce(self, newforce):
        """Sets the newforce of this ProofReward.


        :param newforce: The newforce of this ProofReward.  # noqa: E501
        :type: str
        """
        if newforce is None:
            raise ValueError("Invalid value for `newforce`, must not be `None`")  # noqa: E501

        self._newforce = newforce

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
        if issubclass(ProofReward, dict):
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
        if not isinstance(other, ProofReward):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other