# api-tools-dynamate
DynaMate Tools API

This is a work in progress and so this documentation is missing a lot of context.

The machine running this API is tasked with executing the molecular dynamics tools.
Some of the agent tools that we made public in the original
[DynaMate](https://github.com/omendibleba/dynaMate) are going to be added.

## Examples

In this section we present examples of the molecular dynamics tools that have been added
to DynaMate's toolset.

## MosdDEF

The MosdDef tool creates a LAMMPS data file from a smiles string, the following command
shows the data that we need to send along our request to the REST API:

```sh
curl --header "Content-Type: application/json" --data '{"name":"ethanol","smiles":"CCO","length":"2","count":"1"}' --request POST http://localhost:8000/api/tool/mosdef
```

via the command we are requesting a lammps data file for a single ethanol molecule, whose
SMILES string is CCO, placed in a box of 2 nanometers in length.

The output from the MosdDEF tool is the following:

```lammps
# ethanol data file
mol: ethanol
box-length: 2 nm
molecule: 1

# atom types
atom_types: 5
bond_types: 7
angle_types: 4
dihedral_types: 7

# masses
masses:
1	12.010780	# opls_135
2	1.007947	# opls_140
3	15.999430	# opls_154
4	1.007947	# opls_155
5	12.010780	# opls_157

# pair coefficients (lj)
pair_coeff:
1	epsilon (kcal/mol)		sigma (Angstrom)
1	0.06600		3.50000		# opls_135
2	0.03000		2.50000		# opls_140
3	0.17000		3.12000		# opls_154
4	0.00000		10.00000		# opls_155
5	0.06600		3.50000		# opls_157

# bond coefficients (harmonic)
bond_coeff:
1	340.0		1.09		# opls_135	opls_140
2	268.0		1.529		# opls_135	opls_157
3	340.0		1.09		# opls_140	opls_157
4	553.0		0.945		# opls_154	opls_155
5	320.0		1.41		# opls_154	opls_157

# angle coefficients (harmonic)
angle_coeff:
1	33.0		107.80000	# opls_140	opls_135	opls_140
2	37.5		110.70000	# opls_140	opls_135	opls_157
3	55.0		108.50000	# opls_155	opls_154	opls_157
4	37.5		110.70000	# opls_135	opls_157	opls_140
5	50.0		109.50000	# opls_135	opls_157	opls_154
6	33.0		107.80000	# opls_140	opls_157	opls_140
7	35.0		109.50000	# opls_140	opls_157	opls_154

# dihedral coefficients (oplts)
dihedral_coeff:
1	-0.00000	-0.00000		0.30000		-0.00000	# opls_140opls_135	opls_157	opls_140
2	0.00000	-0.00000		0.46800		-0.00000	# opls_140	opls_135	opls_157	opls_154
3	-0.35600	-0.17400		0.49200		-0.00000	# opls_155opls_154	opls_157	opls_135
4	0.00000	-0.00000		0.45000		-0.00000	# opls_155	opls_154	opls_157	opls_140

# atoms
atom_data:
1	1	1	-0.180000	3.371081	17.594997	2.920308
2	1	5	0.145000	3.262702	16.075993	2.972701
3	1	3	-0.683000	4.495436	15.488022	2.658299
4	1	2	0.060000	3.697034	17.918132	1.908934
5	1	2	0.060000	4.106493	17.951309	3.672416
6	1	2	0.060000	2.382158	18.048578	3.142250
7	1	2	0.060000	2.507353	15.740265	2.231202
8	1	2	0.060000	2.921840	15.753654	3.982733
9	1	4	0.418000	5.068328	15.581746	3.463833

# bonds
bond_data:
1	2	1	2
2	1	1	4
3	1	1	5
4	1	1	6
5	5	2	3
6	3	2	7
7	3	2	8
8	4	3	9

# angles
angle_data:
1	5	1	2	3
2	4	1	2	7
3	4	1	2	8
4	2	2	1	4
5	2	2	1	5
6	2	2	1	6
7	2	2	1	7

# dihedral angles
dihedral_data:
1	-0.00000	-0.00000		0.30000		-0.00000	# opls_140opls_135	opls_157	opls_140
2	0.00000	-0.00000		0.46800		-0.00000	# opls_140	opls_135	opls_157	opls_154
3	-0.35600	-0.17400		0.49200		-0.00000	# opls_155opls_154	opls_157	opls_135
4	0.00000	-0.00000		0.45000		-0.00000	# opls_155	opls_154	opls_157	opls_140
```
