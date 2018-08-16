# File completed: Sept. 24th, 2016 01:22
import socket; import time;
import bot_parser; import bot_commands; import bot_data;

def bot_core(bot_parser, bot_commands, bot_data):
    class bot():
        def __init__(self):
            self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM); print("Created AF_INET socket. Let me set a few things up, and I'll be alive shortly.");
            self.bot_data = bot_data; self.bot_commands = bot_commands; self.bot_parser = bot_parser;
            
            try:
                self.socket_connection.connect((self.bot_data.server_info["address"], self.bot_data.server_info["port"]));
            except socket.error, e:
                print("I failed to connect to the server you provided, I'll let you figure this out while I nap.");
                quit();
            
            time.sleep(1); self.send_raw("NICK {0}".format(self.bot_data.bot_name));
            time.sleep(1); self.send_raw("USER EH-Zombie 8 * :EHZombie");
            time.sleep(1); self.send_raw("MODE {0} +B".format(self.bot_data.bot_name));
            print("Sent my identity to the IRC server.");
        def module_rehash(self):
            module = self.bot_data.command_info["args"][0];
            sender = self.bot_data.message_info["sender"]["respond"]; 
            exec("reload({0});".format(module)) in globals();
            self.send_message("I reloaded {0}.".format(module), sender);
 
        def send_raw(self, message):
            self.socket_connection.send("{0}\r\n".format(message));

        def send_message(self, message, response=""):
            if response == "": response = self.bot_data.message_info["sender"]["respond"];
            self.socket_connection.send("PRIVMSG {0} :{1}\r\n".format(response, message));
            print("I just send the the message '{0}' to {1}.".format(message, self.bot_data.message_info["sender"]["name"]));
            
    botcore = bot();
    return botcore;

# EOF
