from MainCode.negative_sel_project import AA_import_todict

def test_AA_import_todict():
    file = "data/AA_reference_table.txt"
    AA_info = AA_import_todict(file)

    assert AA_info["A"]["type"] == "non-polar"
    assert AA_info["H"]["pka3"] == "6.00"
    assert AA_info["E"]["charged_atom"] == "O"