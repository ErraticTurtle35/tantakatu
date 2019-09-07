import connexion
import six

from swagger_server.models.posting import Posting  # noqa: E501
from swagger_server.models.posting_photo_gallery import PostingPhotoGallery  # noqa: E501
from swagger_server import util


def create_posting(body):  # noqa: E501
    """Create posting

     # noqa: E501

    :param body: Created posting object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Posting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_posting_photo(body):  # noqa: E501
    """Create posting photo

     # noqa: E501

    :param body: Created posting object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostingPhotoGallery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_posting(posting_id):  # noqa: E501
    """Delete posting

    This can only be done by the logged in user. # noqa: E501

    :param posting_id: The posting_id that needs to be deleted
    :type posting_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_posting_photo(photo_id):  # noqa: E501
    """Delete posting photo

    This can only be done by the logged in user. # noqa: E501

    :param photo_id: The photo that needs to be deleted
    :type photo_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_posting_by_id(posting_id):  # noqa: E501
    """Get posting by id

     # noqa: E501

    :param posting_id: The posting_id thats needs to be fetched. Use 1 for testing
    :type posting_id: int

    :rtype: Posting
    """
    return 'do some magic!'


def get_posting_photo_by_id(photo_id):  # noqa: E501
    """Get posting photo by id

     # noqa: E501

    :param photo_id: The photo thats needs to be fetched. Use 1 for testing
    :type photo_id: int

    :rtype: PostingPhotoGallery
    """
    return 'do some magic!'


def publish_posting(body, posting_id):  # noqa: E501
    """Publish the posting

     # noqa: E501

    :param body: Publish posting object
    :type body: dict | bytes
    :param posting_id: The posting_id thats needs to be fetched. Use 1 for testing
    :type posting_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Posting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sell_posting(body, posting_id):  # noqa: E501
    """Sell posting

     # noqa: E501

    :param body: sell posting object
    :type body: dict | bytes
    :param posting_id: The posting_id thats needs to be fetched. Use 1 for testing
    :type posting_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Posting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_posting(body, posting_id):  # noqa: E501
    """Updates posting

    This is only can be done by the logged in user # noqa: E501

    :param body: Update posting object
    :type body: dict | bytes
    :param posting_id: posting_id that needs to be updated
    :type posting_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Posting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_posting_photo(body, photo_id):  # noqa: E501
    """Updates posting photo

    This is only can be done by the logged in user # noqa: E501

    :param body: Update photo rate object
    :type body: dict | bytes
    :param photo_id: photo_id that needs to be updated
    :type photo_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostingPhotoGallery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
