# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.box_array import BoxArray
from swagger_server.models.product import Product
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class BoxObject(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, box: BoxArray=None, class_code: str=None, class_name: str=None, score: float=None, products: List[Product]=None):
        """
        BoxObject - a model defined in Swagger

        :param box: The box of this BoxObject.
        :type box: BoxArray
        :param class_code: The class_code of this BoxObject.
        :type class_code: str
        :param class_name: The class_name of this BoxObject.
        :type class_name: str
        :param score: The score of this BoxObject.
        :type score: float
        :param products: The products of this BoxObject.
        :type products: List[Product]
        """
        self.swagger_types = {
            'box': BoxArray,
            'class_code': str,
            'class_name': str,
            'score': float,
            'products': List[Product]
        }

        self.attribute_map = {
            'box': 'box',
            'class_code': 'class_code',
            'class_name': 'class_name',
            'score': 'score',
            'products': 'products'
        }

        self._box = box
        self._class_code = class_code
        self._class_name = class_name
        self._score = score
        self._products = products

    @classmethod
    def from_dict(cls, dikt) -> 'BoxObject':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BoxObject of this BoxObject.
        :rtype: BoxObject
        """
        return deserialize_model(dikt, cls)

    @property
    def box(self) -> BoxArray:
        """
        Gets the box of this BoxObject.

        :return: The box of this BoxObject.
        :rtype: BoxArray
        """
        return self._box

    @box.setter
    def box(self, box: BoxArray):
        """
        Sets the box of this BoxObject.

        :param box: The box of this BoxObject.
        :type box: BoxArray
        """

        self._box = box

    @property
    def class_code(self) -> str:
        """
        Gets the class_code of this BoxObject.

        :return: The class_code of this BoxObject.
        :rtype: str
        """
        return self._class_code

    @class_code.setter
    def class_code(self, class_code: str):
        """
        Sets the class_code of this BoxObject.

        :param class_code: The class_code of this BoxObject.
        :type class_code: str
        """

        self._class_code = class_code

    @property
    def class_name(self) -> str:
        """
        Gets the class_name of this BoxObject.

        :return: The class_name of this BoxObject.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name: str):
        """
        Sets the class_name of this BoxObject.

        :param class_name: The class_name of this BoxObject.
        :type class_name: str
        """

        self._class_name = class_name

    @property
    def score(self) -> float:
        """
        Gets the score of this BoxObject.

        :return: The score of this BoxObject.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """
        Sets the score of this BoxObject.

        :param score: The score of this BoxObject.
        :type score: float
        """

        self._score = score

    @property
    def products(self) -> List[Product]:
        """
        Gets the products of this BoxObject.

        :return: The products of this BoxObject.
        :rtype: List[Product]
        """
        return self._products

    @products.setter
    def products(self, products: List[Product]):
        """
        Sets the products of this BoxObject.

        :param products: The products of this BoxObject.
        :type products: List[Product]
        """

        self._products = products

