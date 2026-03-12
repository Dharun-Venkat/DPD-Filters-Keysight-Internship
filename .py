import keysight.qcs as qcs
import numpy as np
import matplotlib.pyplot as plt
import json
import re
import time
import copy
from keysight.qcs.utils import load 
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import savgol_filter, lfilter
from scipy.constants import h
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from keysight.qcs.experiments import GATES, Experiment 
from keysight.qcs.analysis import Exponential, IQuadrature, DecayingSinusoid
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from pathlib import Path

print(qcs.__version__)
