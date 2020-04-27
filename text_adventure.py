try:
    import unzip_requirements
except ImportError:
    pass

import json
from jericho import *


def do_action(event, context):
    """
    Function to take input text command and play a text adventure

    :param event: Input AWS Lambda event dict
    :param context: Input AWS Lambda context dict

    :return: Output AWS Lambda dict
    """
    # Decode the request
    request_body = event.get("body")
    if type(request_body) == str:
        request_body = json.loads(request_body)

    action = request_body["action"].lower()
    # game = request_body["game"].lower()

    # Create the environment
    env = FrotzEnv("jericho-game-suite/zork1.z5")
    initial_observation, info = env.reset()
    done = False

    # Take an action in the environment using the step fuction.
    # The resulting text-observation, reward, and game-over indicator is returned.
    observation, reward, done, info = env.step(action)
    # Total score and move-count are returned in the info dictionary
    print('Total Score', info['score'], 'Moves', info['moves'])
    print(observation)

    return None


if __name__ == "__main__":
    do_action({
        "statusCode": 200,
        "body": {
            "action": "take leaflet",
            "game": "zork1"
        }
    }, {})
