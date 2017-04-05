from slackclient import SlackClient


BOT_NAME = 'starterbot'
STARTER_BOT_TOKEN = "xoxb-164308173152-Sd1XL4SAahvDsSwxrvPQtO4V"

slack_client = SlackClient(STARTER_BOT_TOKEN)

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    print api_call
    if api_call.get("ok"):
        # retrieve all users so we can find our bot
        users = api_call.get("members")
        for user in users:
            if "name" in user and user.get("name") == BOT_NAME:
                print "Bot ID for '" + user["name"] + "'is " + user.get("id")
    else:
        print "could not find the bot user with name " + BOT_NAME
