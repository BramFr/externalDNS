#!/usr/bin/env python3
import os
import dns.resolver

class externalList:
    def __init__(self):
        self.workingdir = os.path.dirname(os.path.realpath(__file__)) + '/';
        self.savedir = os.path.dirname(os.path.realpath(__file__)) + '/';
        self.file = "externalDNS.conf";
        self.fullPathConfigFile = self.workingdir + self.file;
        self.fethUrls = [];
        self.lookupDns = [];
        self.configFileContainInfo = self.createChecklist(self.read_file(self.fullPathConfigFile))


    def read_file(self, fullPathFile):
        if not os.path.isfile(fullPathFile):
            os.mknod(fullPathFile)

        Lines = [];
        with open(fullPathFile) as f:
            Lines = f.read().splitlines()
        return Lines

    def dnsLookup(self, dnsItem):
        resolver = dns.resolver.Resolver()
        resolver.timeout = 6
        resolver.lifetime = 6
        try:
            resultDNS = resolver.query(dnsItem, 'A')
        except:
            print("Timeout DNS no result.")
            print("item: " + dnsItem)
            resultDNS = "";
        return resultDNS


    def write_file(self):
        if (len(self.lookupDns) > 0):
            for dnsItem in self.lookupDns:
                foo = self.dnsLookup(dnsItem);
                with open(self.savedir + dnsItem + '.txt', 'w') as f:
                    for item in foo:
                        a = item.to_text()
                        f.write("%s\n" % item.to_text())


    def createChecklist(self, Lines):
        for line in Lines:
            split = line.split("=")
            if split[0].lower() == 'dns':
                self.lookupDns.append(split[1])
            if split[0].lower() == 'url':
                self.fethUrls.append(split[1])
            if split[0].lower() == 'savedir':
                self.savedir = split[1] + "/"

        if (len(self.lookupDns) > 0) or (len(self.fethUrls) > 0):
            return True
        return False



def main():
    externallist = externalList();
    if externallist.configFileContainInfo:
        externallist.write_file()
    else:
        print("Config File Empty")

if __name__ == '__main__':
    main()
