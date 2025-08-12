#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def MosdDEF(d):
"""
This tool uses the MosDEF workflow to generate a LAMMPS data file from a molecule's
SMILE string. By default it uses the OPLS-AA force field for interaction parameters.
The box-size must be supplied in nanometers.
"""

    import mbuild
    import foyer

    name = d["name"]
    smiles = d["smiles"]
    box_size = d["length"]
    n_molecs = d["count"]

    system_smiles = smiles
    box_size = box_size
    n_molecules = n_molecs
    forcefield_name = "oplsaa"
    system_name = name
    system_unparad = mbuild.load(system_smiles, smiles=True)
    system_unparad.name = system_name
    box = mbuild.Box(3*[box_size])
    filled_box = mbuild.fill_box(compound=system_unparad,
                                 n_compounds=n_molecules,
                                 box=box,
                                 overlap=0.2)
    ff = foyer.Forcefield(name=forcefield_name)
    filled_box_param = filled_box.to_parmed(infer_residues=True)
    filled_box_parametrized = ff.apply(filled_box_param)

    mbuild.formats.lammpsdata.write_lammpsdata(filled_box_parametrized,
                                               system_name+".data",
                                               atom_style="full",
                                               unit_style="real",
                                               use_rb_torsions=True)

    with open(f"{system_name}.data", "r") as f:
        data = f.read()
    return data
