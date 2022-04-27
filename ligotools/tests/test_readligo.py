from ligotools import readligo as rl
import numpy as np
import json


fnjson = "/home/jovyan/HW/hw06-joezhou99/data/BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
eventname = 'GW150914' 
event = events[eventname]
fn_H1 = "/home/jovyan/HW/hw06-joezhou99/data/" + event['fn_H1'] 
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')

def test_dim_channel_to_seglist():
    assert (len(rl.dq_channel_to_seglist(np.array([1,1,1,1])))==1)
    
def test_type_channel_to_seglist():    
    assert (type(rl.dq_channel_to_seglist(np.array([1,1,1,1])))==list)
	
def test_type():   
    assert (type(rl.loaddata(fn_H1, 'H1'))==tuple)
    
def test_loaddata():
    assert (len(time_H1)==len(strain_H1))
	assert (len(chan_dict_H1)==13)
    assert (len(strain_H1)==131072)
	
def test_reading_hdf5():
    filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

    assert len(strain) != 0
    assert gpsStart is not None
    assert ts is not None
    assert len(shortnameList) != 0
    assert len(qmask) != 0
    assert len(injmask) != 0
    assert len(injnameList) != 0
    
    
