class Character_frequency:

    def __init__(self):
        self.freq = {}

    def char_frequency(self, str1):

        for n in str1:
            if n in self.freq:
                self.freq = self.freq[n] + 1
            else:
                self.freq[n] = 1
            print("Count of all characters in Geeks for Geeks is :\n "
                  + str(self.freq))


Character_frequency.char_frequency(str1="GOOGLE.CoM")
