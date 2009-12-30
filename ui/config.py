# coding: utf-8
import os, sys

class Configure:
    def __init__(self):
        self.rundir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.conffile = os.path.join(self.rundir, "mycash.conf") 
        self.data = {}
        self.load()

    def load(self):
        f = open(self.conffile, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = [ x.strip() for x in line.split('=') ]
            self.data[parts[0]] = parts[2]

    def dump(self):
        f = open(self.conffile, 'w')
        for k in self.data:
            f.write('%s = %s\n' % (k, self.data[k]))

        f.close()

    def __getitem__(self, k):
        return self.data[k]

    def __setitem__(self, k, v):
        self.data[k] = v


