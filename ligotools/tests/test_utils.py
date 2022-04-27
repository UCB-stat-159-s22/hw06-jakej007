from ligotools import readligo as rl
from ligotools import utils as utils
from scipy.interpolate import interp1d
import json
import numpy as np
import matplotlib.mlab as mlab


fnjson = "data/BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
eventname = 'GW150914' 
event = events[eventname]
fn_H1 = 'data/' + event['fn_H1']       
fs = event['fs']
NFFT = 4*fs
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
time = time_H1
dt = time[1] - time[0]
psd_H1 = interp1d(freqs, Pxx_H1)
strain_H1_whiten = utils.whiten(strain_H1,psd_H1,dt)

def test_whiten():
    """ test whiten func """
    assert isinstance(strain_H1_whiten, np.ndarray)
    assert strain_H1_whiten.shape==(131072,)
    assert np.isclose(strain_H1_whiten[0], 648.16749914)
	
def test_wavfile():
    filename = "/home/jovyan/HW/hw06-jakej007/audio/pytest.wav"
    utils.write_wavfile(filename,int(fs), strain_H1_whitenbp[indxd])
    assert os.path.isfile(filename) 
	
	
def test_reqshift():
    strain_H1_shifted = utils.reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
    shifted_l = len(strain_H1_shifted)
    unshifted_l = len(strain_H1)
    assert(shifted_l == unshifted_l)
	
def test_plot_H1_around_event_graphs():
    img = plt.imread('figures/GW150914_L1_matchfreq.png')
    assert img is not None