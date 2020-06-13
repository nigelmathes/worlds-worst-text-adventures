try:
    import unzip_requirements
except ImportError:
    pass

import json
from pathlib import Path

from jericho import *


def do_action(event, context):
    """
    Function to take an array of input text commands, along with
    a game name found in games.json, and play that text adventure game.

    :param event: Input AWS Lambda event dict
                  Must contain in event["body"]:
                  {
                      "actions": [],
                      "game": "zork1",
                  }
    :param context: Input AWS Lambda context dict

    :return: Output AWS Lambda dict
    """
    # Decode the request
    request_body = event.get("body")
    if type(request_body) == str:
        request_body = json.loads(request_body)

    actions = request_body["actions"]
    game = request_body["game"].lower()

    # Create the environment
    game_suite_path = Path(__file__).resolve().parent / "jericho-game-suite"

    game_path = list(game_suite_path.glob(f"{game}*"))[0]

    env = FrotzEnv(game_path.as_posix())
    initial_observation, info = env.reset()
    done = False

    observation = ""
    action = ""
    for action in actions:
        action = action.lower()
        # Take an action in the environment using the step function.
        # The resulting text-observation, reward, and game-over indicator is returned.
        observation, reward, done, info = env.step(action)
        # Total score and move-count are returned in the info dictionary

    print('Last Action', action, 'Total Score', info['score'], 'Moves', info['moves'],
          done)

    message = observation.rstrip()

    if done:
        return f"GAME OVER YOU WIN.\n {message}"
    else:
        return message
