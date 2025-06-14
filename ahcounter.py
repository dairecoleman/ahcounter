from prettytable import PrettyTable

# class/object that contains the information from a toastmaster meeting about the speakers, their filler words and the frequency of filler words
class ToastmasterMeeting:
    table={}
    table_pretty= [['Speaker', 'Ah', 'Um', 'Eh'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
    filler_word_list =[]

    # init function that starts the object that will hold meeting data
    def __init__(self):
        pass
    
    # adding a new speaker (key)
    def new_speaker(self, speaker):
        self.table[speaker]
   
   # Print a table of the current recordings TODO: in a pretty format
    def print_results(self):
        print("Raw table dict data")
        print(self.table)
        print("pretty print attempt")
        tab = PrettyTable(self.table_pretty[0]) # line that creates prettytable object with headers, using "Speaker" and list of filler_word_list recorded as heard
        tab.add_rows(self.table_pretty[1:]) # define function: insert_player_record() that uses the table dict to insert a row with speaker's name and occurences of each filler_word_list. Put 0 if no count exists.
        print(tab)

    # function that logs a speaker and a filler word they used into the table
    def log_input(self, speaker=str, filler_word=str):
        print(f"{self}, {speaker}, {filler_word}")
        # add speaker if they don't already exist
        if speaker in self.table:
            # add word or increment
            if filler_word in self.table[speaker]:
                self.table[speaker][filler_word]+=1
            else:
                # adding filler_word key
                self.table[speaker][filler_word]=1
                # modify filler_word_list if needed
        else:
            # adding speaker
            self.table[speaker]={}
            self.table[speaker][filler_word]=1
            # modify filler_word_list if needed

    def delete_table(self):
        print("deleting table")
        self.table={}

# testing
# create test objects
#testsession = ToastmasterMeeting()
#logger = AhCounterLogger()
#testsession.print_results()
#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "Um")
#testsession.log_input("Daire", "oh")
#testsession.log_input("Daire", "oh")
#testsession.log_input("Daire", "Um")
#testsession.log_input("Judy", "Oh")
#testsession.print_results()

# NOTE to use prettytable need to activate .venv and install it

