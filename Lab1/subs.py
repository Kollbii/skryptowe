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

    def get_description(self):
        return self.description

class Account:
    def __init__(self, name):
        self.subs_channels = []
        self.name = name

    def subscribe(self, channel):
        if channel not in self.subs_channels:
            self.subs_channels.append(channel)
            return True
        else:
            print("{} is already subscribed to {}".format(self.name, channel.name))
            return False
    
    def unsubscribe(self, channel):
        if channel in self.subs_channels:
            self.subs_channels.remove(channel)
            return True
        else:
            print("{} is not subscribed to {}".format(self.name, channel.name))
            return False


def action(acc, option, channel):
    if option == 1:
        if acc.subscribe(channel):
            print("{} subscribed to {}".format(acc.name, channel.name))
    elif option == 2:
        if acc.unsubscribe(channel):
            print("{} unsubscribed to {}".format(acc.name, channel.name))  


if __name__ == '__main__':
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
    # 6 - add channel
    opt = 1
    print("Option: ")
    opt = int(input())
    while opt != 0:
        try:
            if opt not in [3, 4, 5, 6]:
                print("Account: ")
                acc = accounts[int(input())]
                print("Channel number 1-4: ")
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
                        print("{} is subscribed to {} -> Description: {}".format(accounts[num].name, chn.name, chn.description))
            elif opt == 6:
                num = len(accounts)
                new_name = str(input("New user name: "))
                accounts[num + 1] = Account(new_name)
            
            print("Option: ")
            opt = int(input())
        except KeyboardInterrupt:
            quit()
    else:
        quit()
