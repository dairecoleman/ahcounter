from prettytable import PrettyTable

# class/object that contains the information from a toastmaster meeting about the speakers, their filler words and the frequency of filler words
class ToastmasterMeeting:
    table={}
    filler_word_set = set()
    
    # init function that starts the object that will hold meeting data
    def __init__(self):
        pass
    
   # Print a table of the current recordings TODO: in a pretty format
    def print_results(self):
        print("Raw table dict data")
        print(self.table)
        print("pretty print attempt")
        tab = PrettyTable(['Speaker', *self.filler_word_set]) # line that creates prettytable header, unordered
        for speaker in self.table:
            print(speaker)
            self.insert_player_results(tab, speaker)
        print(tab)
        return tab

    def insert_player_results(self, table, speaker):
        # construct speaker's count for each filler word and add that speakers results for the session
        speakers_counts=[]
        for word in self.filler_word_set:
            if word in self.table[speaker]:
                speakers_counts.append(self.table[speaker][word])
            else:
                speakers_counts.append("0")
        table.add_row([speaker, *speakers_counts])
        print(f"inserting {speaker} records")

    # function that logs a speaker and a filler word they used into the table
    def log_input(self, speaker=str, filler_word=str):
        # check if filler word has been seen before, if new, add to set
        self.update_filler_word_set(filler_word)

        print(f"{self}, {speaker}, {filler_word}")
        # add speaker if they don't already exist
        if speaker in self.table:
            # add word to speakers list or increment
            if filler_word in self.table[speaker]:
                self.table[speaker][filler_word]+=1
            else:
                # adding filler_word key
                self.table[speaker][filler_word]=1
        else:
            # adding speaker
            self.table[speaker]={}
            self.table[speaker][filler_word]=1
    
    def update_filler_word_set(self, word=str):
        self.filler_word_set.add(word)
        print(f"added {word} to filler word set : {self.filler_word_set}")

    def delete_table(self):
        print(f"deleting table, Table: {self.table}")
        self.table={}

    def clear_filler_word_list(self):
        print(f"clearing filler_word set, Set: {self.filler_word_set}")
        self.filler_word_set.clear()

    def clear_data(self):
        print("clearing session data")
        self.delete_table()
        self.clear_filler_word_list()

    def add_speaker(self, speaker):
        if speaker not in self.table:
            self.table[speaker]={}

    def return_speakers(self):
        list_of_speakers=self.table.keys()
        return list_of_speakers


# testing
# create test objects
#testsession = ToastmasterMeeting()
#testsession.print_results()
#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "Um")
#3testsession.log_input("Daire", "oh")
#testsession.log_input("Judy", "Oh")
#testsession.log_input("Karl", "Y'know")
#testsession.print_results()
#testsession.clear_data()

#print(testsession.filler_word_set)
#print(testsession.table)

#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "oh")
#t#estsession.print_results()

# instructions to use interactivly
# NOTE to use prettytable need to activate .venv and install it
# source .venv/bin/activate
# python3
# import ahcounter
# testsession = ahcounter.ToastmasterMeeting()
# testsession.print_results() prints results
# testsession.log_input("Bob", "ah") logs results

