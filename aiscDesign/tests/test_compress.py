from aiscDesign.compressElements import critical_Stress, effective_Slenderness, CompressDesign
from aiscpy import Shape

def test_table_Kl_r():
    Fa1 = critical_Stress(36, 1)
    assert Fa1 == 21.56
    
    Fa2 = critical_Stress(36, 165)
    assert Fa2 == 5.49

def test_compress_design():
    shape1 = Shape ('W', 'W4X13')
    s1 = CompressDesign(shape1, 14, 8, 36)
    
    assert s1.A == 3.83
    assert s1.rmin == 1
    assert s1.Fa == 13.48
    assert round(s1.fa, 1) == 3.7
    assert s1.status() == 'OK'