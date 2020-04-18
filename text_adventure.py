try:
    import unzip_requirements
except ImportError:
    pass

import json
import textworld
import wget


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
    game = 'zork1'
    initialized = False

    # Download the game
    if not initialized:
        wget.download("https://archive.org/download/Zork1Release88Z-machineFile/zork1.z5",
                      game + ".z5")
        env = textworld.start('./zork1.z5')
        game_state = env.reset()
        initialized = True

    if action == 'Done':
        env.close()

    game_state, reward, done = env.step(action)

    return env.render()
