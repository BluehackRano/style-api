# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.image_dataset import ImageDataset
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class GetImagesByCategoryResponseData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_count: str=None, images: List[ImageDataset]=None):
        """
        GetImagesByCategoryResponseData - a model defined in Swagger

        :param total_count: The total_count of this GetImagesByCategoryResponseData.
        :type total_count: str
        :param images: The images of this GetImagesByCategoryResponseData.
        :type images: List[ImageDataset]
        """
        self.swagger_types = {
            'total_count': str,
            'images': List[ImageDataset]
        }

        self.attribute_map = {
            'total_count': 'total_count',
            'images': 'images'
        }

        self._total_count = total_count
        self._images = images

    @classmethod
    def from_dict(cls, dikt) -> 'GetImagesByCategoryResponseData':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetImagesByCategoryResponse_data of this GetImagesByCategoryResponseData.
        :rtype: GetImagesByCategoryResponseData
        """
        return deserialize_model(dikt, cls)

    @property
    def total_count(self) -> str:
        """
        Gets the total_count of this GetImagesByCategoryResponseData.

        :return: The total_count of this GetImagesByCategoryResponseData.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count: str):
        """
        Sets the total_count of this GetImagesByCategoryResponseData.

        :param total_count: The total_count of this GetImagesByCategoryResponseData.
        :type total_count: str
        """

        self._total_count = total_count

    @property
    def images(self) -> List[ImageDataset]:
        """
        Gets the images of this GetImagesByCategoryResponseData.

        :return: The images of this GetImagesByCategoryResponseData.
        :rtype: List[ImageDataset]
        """
        return self._images

    @images.setter
    def images(self, images: List[ImageDataset]):
        """
        Sets the images of this GetImagesByCategoryResponseData.

        :param images: The images of this GetImagesByCategoryResponseData.
        :type images: List[ImageDataset]
        """

        self._images = images

