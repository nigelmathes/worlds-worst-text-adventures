from typing import Dict

import pytest

from text_adventure import do_action


@pytest.fixture
def test_data() -> Dict:
    """
    Test input to the text adventure function

    :return: Dictionary of the form:
             {
                 "statusCode": 200,
                 "body": {
                    "actions": ["open mailbox"],
                    "game": "zork1"
                 }
             }
    """
    input_data = {
        "statusCode": 200,
        "body": {
            "actions": ["look", "search mailbox", "kick door", "go around house",
                        "go north", "search large tree"],
            "game": "zork1"
        }
    }

    return input_data


def test_basic_invoke(test_data: Dict) -> None:
    """
    Test a basic request works all the way to the end and the response
    is as expected.

    :param test_data: Pytest fixture containing an input request
    """
    # Arrange
    expected_response = "You find nothing unusual."

    # Act
    response = do_action(test_data, {})

    # Assert
    assert response == expected_response


def test_inventory(test_data: Dict) -> None:
    """
    Test that the inventory can be returned.

    :param test_data:Pytest fixture containing an input request
    """
    # Arrange
    test_data["body"]["actions"].append("inventory")
    expected_response = "You are empty-handed."

    # Act
    response = do_action(test_data, {})

    # Assert
    assert response == expected_response
