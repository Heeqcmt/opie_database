import ontario_ndp
import ontario_pc
import ontario_lib

def combined():
    event_list_final = ontario_ndp.get_ndp_on_event() + ontario_pc.get_on_pc_event() + ontario_lib.get_on_lib_event()

    #reshuffle the id 
    counter = 0
    for event in event_list_final:
        event.id = counter
        counter += 1
    print("combined")
    return event_list_final


