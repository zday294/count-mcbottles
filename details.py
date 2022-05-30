class Details:
    def __init__(self, pat="", monitored=None, replace="#", prefix="-"):
        self.pattern = pat
        self.monitoredChannel = monitored
        self.replaceChar = replace
        self.number = 0
        self.prefix = prefix