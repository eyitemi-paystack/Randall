from slackclient import SlackClient
from slack import SlackClient
import slack


from .. import config
get_env2 = config.get_env()

class SlackHelper:

    def __init__(self):
        self.slack_token = get_env2('SLACK_TOKEN')
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env2('SLACK_CHANNEL')

    
    def post_message(self, msg, recipient):
        return self.slac.api_call(
            "chat.postMessage",
            channel=recipient,
            text=msg,
            as_user=True
        )

    