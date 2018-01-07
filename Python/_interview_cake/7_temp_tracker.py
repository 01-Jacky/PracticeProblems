class TempTracker:
    def __init__(self):
        # min max
        self.max = float('-inf')
        self.min = float('inf')

        # avg
        self.sum = 0
        self.total_records = 0
        self.mean = None

        # mode
        self.freq_arr = [0] * 111
        self.mode = None
        self.max_freq = 0

    def insert(self):
        # update max min

        # update avg

        # update temp

    def get_max(self):
       pass

    def get_min(self):
       pass

    def get_mean(self):
       pass

    def get_mode(self):
       pass