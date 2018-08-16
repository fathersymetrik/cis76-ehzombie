# File completed: Sept. 24th, 2016 01:45
# File modified: Oct. 1st, 2016 17:33 - added ping command.
# File modified: Oct. 15th, 2016 14:59 - added runscript command.
import commands
command_dictionary = {
    "join":{"code":"bot_core.bot_commands.join_channel(bot_core);"},
    "part":{"code":"bot_core.bot_commands.part_channel(bot_core);"},
    "quit":{"code":"bot_core.bot_commands.quit_server(bot_core);"},
    "debug":{"code":"bot_core.bot_commands.debug_variable(bot_core);"},
    "ping":{"code":"bot_core.bot_commands.ping_server(bot_core);"}
    }

def join_channel(bot_core):
    channel = bot_core.bot_data.command_info["args"][0];
    bot_core.send_raw("JOIN {0}".format(channel));

def part_channel(bot_core):
    channel = bot_core.bot_data.command_info["args"][0];
    bot_core.send_raw("PART {0}".format(channel));

def quit_server(bot_core):
    bot_core.send_raw("QUIT :Local kill")
    bot_core.socket_connection.close()
    quit()

def debug_variable(bot_core):
    exploit_list = ["exec", "eval", "hasattr", "getattr", "vars", "__import__"];
    debug_value = " ".join(bot_core.bot_data.command_info["args"]);
    try:
        debug_allow = True;
        for exploit_item in exploit_list:
            if exploit_item in debug_value: debug_allow = False;
        if debug_allow: bot_core.send_message("The value is: {0}".format(eval(debug_value)));
        else: bot_core.send_message("Sorry, that contains black-listed content.");
    except:
        bot_core.send_message("That produced an error.");

def ping_server(bot_core):
    target_server = bot_core.bot_data.command_info["args"][0];
    ping_allowed = True;
    if len(target_server) <= 15:
        try:
            for item in target_server.split("."): item = int(item);
        except: ping_allowed = False;
    else: ping_allowed = False;
    if ping_allowed:
        bot_core.send_message("Sending ten pings, give me around 20 seconds to process.");
        ping_output = commands.getoutput("ping -c 10 {0}".format(target_server)).split("\n");
        for item in ping_output:
            item_found = False;
            if "transmitted" in item and item_found != True:
                item_found = True;
                bot_core.send_message("Here you go: {0} | {1}".format(ping_output[0], item));
    else: bot_core.send_message("Sorry, this command is pretty strict. Make sure your IP address is simple IPv4.");

# EOF
