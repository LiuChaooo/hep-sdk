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

from hep_rest_api.models.order_item import OrderItem  # noqa: F401,E501


class Order(object):
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
        'description': 'str',
        'price_currency': 'str',
        'total_price': 'str',
        'order_number': 'str',
        'seller': 'str',
        'customer': 'str',
        'broker': 'str',
        'order_items': 'list[OrderItem]',
        'chain_txid': 'str'
    }

    attribute_map = {
        'description': 'description',
        'price_currency': 'price_currency',
        'total_price': 'total_price',
        'order_number': 'order_number',
        'seller': 'seller',
        'customer': 'customer',
        'broker': 'broker',
        'order_items': 'order_items',
        'chain_txid': 'chain_txid'
    }

    def __init__(self, description=None, price_currency=None, total_price=None, order_number=None, seller=None, customer=None, broker=None, order_items=None, chain_txid=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._price_currency = None
        self._total_price = None
        self._order_number = None
        self._seller = None
        self._customer = None
        self._broker = None
        self._order_items = None
        self._chain_txid = None
        self.discriminator = None

        self.description = description
        self.price_currency = price_currency
        self.total_price = total_price
        self.order_number = order_number
        self.seller = seller
        self.customer = customer
        if broker is not None:
            self.broker = broker
        self.order_items = order_items
        if chain_txid is not None:
            self.chain_txid = chain_txid

    @property
    def description(self):
        """Gets the description of this Order.  # noqa: E501

        The order description  # noqa: E501

        :return: The description of this Order.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Order.

        The order description  # noqa: E501

        :param description: The description of this Order.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 64:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `64`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def price_currency(self):
        """Gets the price_currency of this Order.  # noqa: E501

        The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.  # noqa: E501

        :return: The price_currency of this Order.  # noqa: E501
        :rtype: str
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, price_currency):
        """Sets the price_currency of this Order.

        The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.  # noqa: E501

        :param price_currency: The price_currency of this Order.  # noqa: E501
        :type: str
        """
        if price_currency is None:
            raise ValueError("Invalid value for `price_currency`, must not be `None`")  # noqa: E501
        if price_currency is not None and len(price_currency) > 64:
            raise ValueError("Invalid value for `price_currency`, length must be less than or equal to `64`")  # noqa: E501
        if price_currency is not None and len(price_currency) < 1:
            raise ValueError("Invalid value for `price_currency`, length must be greater than or equal to `1`")  # noqa: E501

        self._price_currency = price_currency

    @property
    def total_price(self):
        """Gets the total_price of this Order.  # noqa: E501

        The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.  # noqa: E501

        :return: The total_price of this Order.  # noqa: E501
        :rtype: str
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this Order.

        The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.  # noqa: E501

        :param total_price: The total_price of this Order.  # noqa: E501
        :type: str
        """
        if total_price is None:
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501
        if total_price is not None and len(total_price) > 64:
            raise ValueError("Invalid value for `total_price`, length must be less than or equal to `64`")  # noqa: E501
        if total_price is not None and len(total_price) < 1:
            raise ValueError("Invalid value for `total_price`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_price = total_price

    @property
    def order_number(self):
        """Gets the order_number of this Order.  # noqa: E501

        The order number  # noqa: E501

        :return: The order_number of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Order.

        The order number  # noqa: E501

        :param order_number: The order_number of this Order.  # noqa: E501
        :type: str
        """
        if order_number is None:
            raise ValueError("Invalid value for `order_number`, must not be `None`")  # noqa: E501
        if order_number is not None and len(order_number) > 64:
            raise ValueError("Invalid value for `order_number`, length must be less than or equal to `64`")  # noqa: E501
        if order_number is not None and len(order_number) < 1:
            raise ValueError("Invalid value for `order_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._order_number = order_number

    @property
    def seller(self):
        """Gets the seller of this Order.  # noqa: E501

        The seller's NewID  # noqa: E501

        :return: The seller of this Order.  # noqa: E501
        :rtype: str
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this Order.

        The seller's NewID  # noqa: E501

        :param seller: The seller of this Order.  # noqa: E501
        :type: str
        """
        if seller is None:
            raise ValueError("Invalid value for `seller`, must not be `None`")  # noqa: E501
        if seller is not None and len(seller) > 64:
            raise ValueError("Invalid value for `seller`, length must be less than or equal to `64`")  # noqa: E501
        if seller is not None and len(seller) < 1:
            raise ValueError("Invalid value for `seller`, length must be greater than or equal to `1`")  # noqa: E501

        self._seller = seller

    @property
    def customer(self):
        """Gets the customer of this Order.  # noqa: E501

        The customer's NewID  # noqa: E501

        :return: The customer of this Order.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Order.

        The customer's NewID  # noqa: E501

        :param customer: The customer of this Order.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501
        if customer is not None and len(customer) > 64:
            raise ValueError("Invalid value for `customer`, length must be less than or equal to `64`")  # noqa: E501
        if customer is not None and len(customer) < 1:
            raise ValueError("Invalid value for `customer`, length must be greater than or equal to `1`")  # noqa: E501

        self._customer = customer

    @property
    def broker(self):
        """Gets the broker of this Order.  # noqa: E501

        The broker's NewID. optional.  # noqa: E501

        :return: The broker of this Order.  # noqa: E501
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this Order.

        The broker's NewID. optional.  # noqa: E501

        :param broker: The broker of this Order.  # noqa: E501
        :type: str
        """
        if broker is not None and len(broker) > 64:
            raise ValueError("Invalid value for `broker`, length must be less than or equal to `64`")  # noqa: E501

        self._broker = broker

    @property
    def order_items(self):
        """Gets the order_items of this Order.  # noqa: E501


        :return: The order_items of this Order.  # noqa: E501
        :rtype: list[OrderItem]
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this Order.


        :param order_items: The order_items of this Order.  # noqa: E501
        :type: list[OrderItem]
        """
        if order_items is None:
            raise ValueError("Invalid value for `order_items`, must not be `None`")  # noqa: E501

        self._order_items = order_items

    @property
    def chain_txid(self):
        """Gets the chain_txid of this Order.  # noqa: E501

        The chain txid  # noqa: E501

        :return: The chain_txid of this Order.  # noqa: E501
        :rtype: str
        """
        return self._chain_txid

    @chain_txid.setter
    def chain_txid(self, chain_txid):
        """Sets the chain_txid of this Order.

        The chain txid  # noqa: E501

        :param chain_txid: The chain_txid of this Order.  # noqa: E501
        :type: str
        """
        if chain_txid is not None and len(chain_txid) > 256:
            raise ValueError("Invalid value for `chain_txid`, length must be less than or equal to `256`")  # noqa: E501

        self._chain_txid = chain_txid

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
