import connexion
import six

from swagger_server.models.country import Country  # noqa: E501
from swagger_server import util


def create_country(body):  # noqa: E501
    """Create a country

     # noqa: E501

    :param body: Created country object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Country.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_country(country_id):  # noqa: E501
    """Delete country

    This can only be done by the logged in user. # noqa: E501

    :param country_id: The country id that needs to be deleted
    :type country_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_county_by_id(country_id):  # noqa: E501
    """Get user by name

     # noqa: E501

    :param country_id: The id thats needs to be fetched. Use 1 for testing
    :type country_id: int

    :rtype: Country
    """
    return 'do some magic!'


def update_country(body, country_id):  # noqa: E501
    """Updates country

    This is only can be done by the logged in user # noqa: E501

    :param body: Update Country object
    :type body: dict | bytes
    :param country_id: id that needs to be updated
    :type country_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Country.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
