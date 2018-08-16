# File completed: Sept. 23rd, 2016 23:34
from platform import node, platform, version;
machine_info = {
                   "node":node(),
                   "platform":platform(),
                   "version":version()
               };

# The variables under this section should remain static. 
BUFFER = [""]; irc_data = {"raw":""}; command_info = {"name":"", "args":[]};
message_info = {"message":"", "length":0, "sender":{"name":"", "respond":""}};
server_info = {"address":"irc.university.edu", "channel":"#cis76", "port":6667};

# Change XX to your pod number and xxxxxx76 to your username.
bot_name = "PodXXbot"; command_symbol = "!";
auth_users =["xxxxxx76", "zombie_lord"];

# EOF
