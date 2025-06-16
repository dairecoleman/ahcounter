from ahcounter.ahcounter import ToastmasterMeeting
import pytest

def test_ToastmasterMeeting_creation():
    test_instance = ToastmasterMeeting()
    assert test_instance.table == {}
    assert test_instance.filler_word_set == set()
    assert isinstance(test_instance, ToastmasterMeeting)

@pytest.fixture
def fresh_meeting():
    # Always return a fresh instance with cleared class-level data
    ToastmasterMeeting.table = {}
    ToastmasterMeeting.filler_word_set = set()
    return ToastmasterMeeting()

#def test_session():
#    test = ToastmasterMeeting()
#    test.log_input("Daire", "Um")
#    test.log_input("Daire", "Um")
#    test.log_input("Daire", "oh")
#    test.log_input("Judy", "Oh")
#    test.log_input("Karl", "Y'know")
#    tab = test.print_results()

def test_print_results_returns_pretty_table(fresh_meeting):
    fresh_meeting.log_input("Daire", "Um")
    fresh_meeting.log_input("Daire", "oh")
    fresh_meeting.log_input("Judy", "Oh")
    fresh_meeting.log_input("Karl", "Y'know")

    table = fresh_meeting.print_results()

    assert table.field_names == ["Speaker", *sorted(fresh_meeting.filler_word_set)] or table.field_names == ["Speaker", *fresh_meeting.filler_word_set]
    assert sorted([row[0] for row in table._rows]) == ["Daire", "Judy", "Karl"]
    # Optional: assert full string output
    output = table.get_string()
    print(output)
    assert "Daire" in output
    assert "Um" in output
    assert "Judy" in output

def test_log_input_adds_speaker_and_word(fresh_meeting):
    fresh_meeting.log_input("Daire", "Um")
    assert fresh_meeting.table == {"Daire": {"Um": 1}}
    assert "Um" in fresh_meeting.filler_word_set

def test_delete_table(fresh_meeting):
    fresh_meeting.log_input("Daire", "Um")
    fresh_meeting.delete_table()
    assert fresh_meeting.table == {}

def test_clear_filler_word_list(fresh_meeting):
    fresh_meeting.log_input("Daire", "Um")
    fresh_meeting.clear_filler_word_list()
    assert fresh_meeting.filler_word_set == set()

def test_clear_data(fresh_meeting):
    fresh_meeting.log_input("Daire", "Um")
    fresh_meeting.log_input("Judy", "Oh")
    fresh_meeting.clear_data()
    assert fresh_meeting.table == {}
    assert fresh_meeting.filler_word_set == set()
