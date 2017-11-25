import connexion
from swagger_server.models.get_objects_response import GetObjectsResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from controller.objects import Objects

def get_objects_by_image_file(file):
    """
    Query to search objects and products

    :param file: Image file to upload (only support jpg format yet)
    :type file: werkzeug.datastructures.FileStorage

    :rtype: GetObjectsResponse
    """
    return Objects.get_objects_by_image_file(file)

def get_objects_by_product_id(productId):
    """
    Query to search multiple objects

    :param productId:
    :type productId: str

    :rtype: GetObjectsResponse
    """
    return Objects.get_objects_by_product_id(productId)
