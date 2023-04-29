import pycba as cba
import numpy as np
import matplotlib.pyplot as plt
from IPython import display

def influence_lines(L: list[float], EI : list[float], R : list[float], etype: list[float], x_location: float):
    '''
    Generates influence for bending, shear and reaction given an x position
    '''
    ils = cba.InfluenceLines(L, EI, R, etype) 
    ils.create_ils(step=0.5)
    fig, axs = plt.subplots(3, 1)
    M_plot = ils.plot_il(x_location, "M", axs[0]) 
    V_plot = ils.plot_il(x_location, "V", axs[1])
    R_plot = ils.plot_il(x_location, "R", axs[2])
    return fig

def static_bridge_analysis(L: list[float], EI : list[float], R : list[float], etype: list[float], axle_loads: list[float],axle_spacings: list[float], x_position: float):
    '''
    Generates shear and moment diagrams for vehicle based on user input of vehicle position
    '''
    ba = cba.BridgeAnalysis()
    bridge = ba.add_bridge(L, EI, R, etype)
    vehicle = ba.add_vehicle(axle_spacings, axle_loads)
    ba.static_vehicle(x_position, plotflag=True) 
  
    #fig, axs = plt.subplots(3, 1)
    fig_static = ba.plot_static(x_position,)

    return fig_static

def envelope_bridge_analysis(L: list[float], EI : list[float], R : list[float], etype: list[float], axle_loads: list[float],axle_spacings: list[float]):
    '''
    Generates envelope of shear and moment diagrams 
    '''
    ba = cba.BridgeAnalysis()
    bridge = ba.add_bridge(L, EI, R, etype)
    vehicle = ba.add_vehicle(axle_spacings, axle_loads)
    env = ba.run_vehicle(0.5, plot_env=True, plot_all=False)

    fig_envelope = ba.plot_envelopes(env)

    return fig_envelope

def envelope_bridge_analysis2(L: list[float], EI : list[float], R : list[float], etype: list[float], axle_loads: list[float],axle_spacings: list[float]):
    '''
    Generates max and min values of bending and shear with their positions 
    '''

    ba = cba.BridgeAnalysis()
    bridge = ba.add_bridge(L, EI, R, etype)
    vehicle = ba.add_vehicle(axle_spacings, axle_loads)
    env = ba.run_vehicle(0.5, plot_env=True, plot_all=False)
    cvals = ba.critical_values(env)
  
    Mmax = cvals["Mmax"]["val"]
    Mmin = cvals["Mmin"]["val"]
    Vmax = cvals["Vmax"]["val"]
    Vmin = cvals["Vmin"]["val"]

    Mmax_at = cvals["Mmax"]["at"]
    Mmin_at = cvals["Mmin"]["at"]
    Vmax_at = cvals["Vmax"]["at"]
    Vmin_at = cvals["Vmin"]["at"]
  
    return Mmax, Mmin, Vmax, Vmin, Mmax_at, Mmin_at, Vmax_at, Vmin_at

def patch_loads(L: list[float], EI : list[float], R : list[float], LM: list[list[float]], etype: list[float]):
    '''
    Generates bending, shear and deflection diagrams/values of applied UDL patch loads 
    '''
    beam_analysis = cba.BeamAnalysis(L, EI, R, LM, etype)
    beam_analysis.analyze()
    results = beam_analysis.plot_results()
    Mmax=max(beam_analysis.beam_results.results.M)
    Mmin=min(beam_analysis.beam_results.results.M)
    Vmax=max(beam_analysis.beam_results.results.V)
    Vmin=min(beam_analysis.beam_results.results.V)
    return results, Mmax, Mmin, Vmax, Vmin 