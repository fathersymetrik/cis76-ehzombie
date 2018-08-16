# File completed: Sept. 23rd, 2016 22:29
import bot_parser; import bot_core; import bot_data; import bot_commands;
connection_core = bot_core.bot_core(bot_parser, bot_commands, bot_data);
connection_core.send_raw("JOIN {0}".format(connection_core.bot_data.server_info["channel"]));
print("Great, everything seems to be working. I'll keep you updated here with errors.");
print("As a reminder, maybe get rid of all these print functions if this is a real zombie?");
while True:
    connection_core.bot_data.BUFFER = connection_core.socket_connection.recv(1024).split("\r\n");
    # I yell buffer because it's easier to see.
    if connection_core.bot_data.BUFFER != [""]: connection_core.bot_parser.filter_errors(connection_core);

# EOF
