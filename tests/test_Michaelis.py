from Neg_Sel_Pred.negative_sel_project import Michaelis_Menten

def test_0_Subtrate():
	K_m = 1
	S = 0
	Vmax = 10
	V = Michaelis_Menten(Vmax,S,K_m)
	assert V == 0, "The expected Value should be 0"	
