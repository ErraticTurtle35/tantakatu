import connexion
import six

from swagger_server.models.posting_category import PostingCategory  # noqa: E501
from swagger_server import util


def create_posting_category(body):  # noqa: E501
    """Create a posting category

     # noqa: E501

    :param body: Created category object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostingCategory.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_posting_category(category_id):  # noqa: E501
    """Delete category

    This can only be done by the logged in user. # noqa: E501

    :param category_id: The category_id that needs to be deleted
    :type category_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_posting_category_by_id(category_id):  # noqa: E501
    """Get category by id

     # noqa: E501

    :param category_id: The category_id thats needs to be fetched. Use 1 for testing
    :type category_id: int

    :rtype: PostingCategory
    """
    return 'do some magic!'


def update_posting_category(body, category_id):  # noqa: E501
    """Updates posting

    This is only can be done by the logged in user # noqa: E501

    :param body: Update category object
    :type body: dict | bytes
    :param category_id: category_id that needs to be updated
    :type category_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostingCategory.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
