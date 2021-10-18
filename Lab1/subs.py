import sys, os
import signal

class Channel:
    def __init__(self, name, subs_count, description):
        self.name = name
        self.subs_count = subs_count
        self.description = description

    def add_description(self, text):
        self.description += ''.join(text)
        return True

    def rm_description(self):
        self.description = ''
        return True

class Account:
    def __init__(self, name):
        self.subs_channels = []
        self.name = name

    def subscribe(self, channel):
        if channel not in self.subs_channels:
            self.subs_channels.append(channel)
            channel.subs_count += 1
            return True
        else:
            print("{} is already subscribed to {}".format(self.name, channel.name))
            return False
    
    def unsubscribe(self, channel):
        if channel in self.subs_channels:
            self.subs_channels.remove(channel)
            channel.subs_count -= 1
            return True
        else:
            print("{} is not subscribed to {}".format(self.name, channel.name))
            return False


def action(acc, option, channel):
    if option == 1:
        if acc.subscribe(channel):
            print("{} subscribed to {}".format(acc.name, channel.name))
            print("Current subscribers to {}: {}".format(channel.name, channel.subs_count))


    elif option == 2:
        if acc.unsubscribe(channel):
            print("{} unsubscribed to {}".format(acc.name, channel.name))
            print("Current subscribers to {}: {}".format(channel.name, channel.subs_count))

def handle_exit(sigint, frame):
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_exit)
    accounts = {
        1: Account("User 1"),
        2: Account("User 2")
    }

    channels = {
        1: Channel("One chan", 0, "Blank description in here."),
        2: Channel("Two chan", 0, "Lorem ipsum dos semit."),
        3: Channel("Simple chan", 0, ""),
        4: Channel("4 chan", 0, "Very short desc in here.")
    }

    accounts[1].subscribe(channels[1])
    accounts[1].subscribe(channels[2])
    accounts[1].subscribe(channels[3])
    accounts[2].subscribe(channels[1])


    # 0 - exit
    # 1 - subscirbe
    # 2 - unsubscribe
    # 3 - add description
    # 4 - remove description
    # 5 - info 
    # 6 - add user
    # 7 - add channel
    opt = 1
    print("Option: ")
    opt = int(input())
    while opt != 0:
        os.system('clear')
        try:
            if opt in [1, 2]:
                print("Account: ")
                acc = accounts[int(input())]
                print("Channel number 1-{}: ".format(len(channels)))
                chn = channels[int(input())]
                action(acc, opt, chn)
            elif opt == 3:
                print("Channel number 1-{} to change description: ".format(len(channels)))
                chn = channels[int(input())]
                desc = str(input("Insert description to add: "))
                chn.add_description(str(desc))
                print("Succesfully added a description for {}".format(chn.name))
            elif opt == 4:
                print("Channel number 1-{} to remove description: ".format(len(channels)))
                chn = channels[int(input())]
                chn.rm_description()
                print("Succesfully removed description for {}".format(chn.name))
            elif opt == 5:
                for num in accounts:
                    for chn in accounts[num].subs_channels:
                        print("{} is subscribed to {};\tSub Count: {};\tDescription: {}".format(accounts[num].name, chn.name, chn.subs_count,chn.description))
            elif opt == 6:
                num = len(accounts)
                new_name = str(input("New user name: "))
                accounts[num + 1] = Account(new_name)
            elif opt == 7:
                num = len(channels)
                new_name = str(input("New channel name: "))
                channels[num + 1] = Channel(new_name, 0, "")
            print("Option: ")
            opt = int(input())
        except KeyboardInterrupt:
            sys.exit(0)
