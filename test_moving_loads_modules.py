import moving_loads_modules as ilm
from pytest import approx, raises

def test_envelope_bridge_analysis2():
    L = [20,20]
    EI = [39000000.00,39000000.00]
    R = [-1,0,-1,0,-1,0]
    etype = [1,1]
    axle_loads = [120,120,120,120,120,120,120,120,120,120,120,120]  
    axle_spacings = [1.25,1.25,3.75,1.25,1.25,6.25,1.25,1.25,5,1.25,1.25]  
    x_location = 20 
    x_position = 25
    LM = [[1,3,6,0,20]]
    
    Mmax, Mmin, Vmax, Vmin, Mmax_at, Mmin_at, Vmax_at, Vmin_at = ilm.envelope_bridge_analysis2(L, EI , R , etype, axle_loads ,axle_spacings )
    
    assert Mmax == approx(1981.94668359375)
    assert Mmin == approx(-2331.861328125)
    assert Vmax == approx(676.25244140625)
    assert Vmin == approx(-664.3641796875)

    assert Mmax_at == approx(8.200000000000001)
    assert Mmin_at == approx(20.0)
    assert Vmax_at == approx(20.0)
    assert Vmin_at == approx(19.6)

def test_patch_loads():
    L = [20,20]
    EI = [39000000.00,39000000.00]
    R = [-1,0,-1,0,-1,0]
    etype = [1,1]
    LM = [[1,3,6,0,20]]
    
    fig, Mmax, Mmin, Vmax, Vmin = ilm.patch_loads(L, EI , R , LM , etype)
    
    assert Mmax == approx(229.67999999999995)
    assert Mmin == approx(-150.00000000000003)
    assert Vmax == approx(52.5)
    assert Vmin == approx(-67.5)