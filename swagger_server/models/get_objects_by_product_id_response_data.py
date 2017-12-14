# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.box_object import BoxObject
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class GetObjectsByProductIdResponseData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, boxes: List[BoxObject]=None, product_id: str=None):
        """
        GetObjectsByProductIdResponseData - a model defined in Swagger

        :param boxes: The boxes of this GetObjectsByProductIdResponseData.
        :type boxes: List[BoxObject]
        :param product_id: The product_id of this GetObjectsByProductIdResponseData.
        :type product_id: str
        """
        self.swagger_types = {
            'boxes': List[BoxObject],
            'product_id': str
        }

        self.attribute_map = {
            'boxes': 'boxes',
            'product_id': 'product_id'
        }

        self._boxes = boxes
        self._product_id = product_id

    @classmethod
    def from_dict(cls, dikt) -> 'GetObjectsByProductIdResponseData':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetObjectsByProductIdResponse_data of this GetObjectsByProductIdResponseData.
        :rtype: GetObjectsByProductIdResponseData
        """
        return deserialize_model(dikt, cls)

    @property
    def boxes(self) -> List[BoxObject]:
        """
        Gets the boxes of this GetObjectsByProductIdResponseData.

        :return: The boxes of this GetObjectsByProductIdResponseData.
        :rtype: List[BoxObject]
        """
        return self._boxes

    @boxes.setter
    def boxes(self, boxes: List[BoxObject]):
        """
        Sets the boxes of this GetObjectsByProductIdResponseData.

        :param boxes: The boxes of this GetObjectsByProductIdResponseData.
        :type boxes: List[BoxObject]
        """

        self._boxes = boxes

    @property
    def product_id(self) -> str:
        """
        Gets the product_id of this GetObjectsByProductIdResponseData.

        :return: The product_id of this GetObjectsByProductIdResponseData.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str):
        """
        Sets the product_id of this GetObjectsByProductIdResponseData.

        :param product_id: The product_id of this GetObjectsByProductIdResponseData.
        :type product_id: str
        """

        self._product_id = product_id

