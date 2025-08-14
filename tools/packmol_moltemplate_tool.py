#!/usr/bin/env python3
"""
packmol_moltemplate_tool

This tool generates a packmol input file that uses previously generated coordinate files
(pdb or xyz) and template files to generate a newly packed system. Then the templates are
used to create the LAMMPS data file with forcefield parameters.

WARNING: If the templates have parameter from distinc force fields issues can arise due to
the styles used to defined interaction parameters. This would require manual editing of
the hybrid functions used to describe each type of interaction.
"""

def packmol_template_tool(data):
    """
    Generate a LAMMPS data file using packmol and moltemplate for a system with multiple
    types of molecules.
    """

    import os
    names = data["names"]
    count = data["count"]
    box = data["box"]

    nmol = count

    # Writing packmol input
    with open("packmol.inp", "w") as f:
        print(f"""tolerance 2.0

# The file type of input and output files is PDB
filetype pdb

# The name of the output file
output system.pdb

# The system components
""", file=f)

        for i in range(len(names)):
            print(f"""
structure {names[i]}.pdb
  number {nmol[i]}
  inside box 0. 0. 0. {box} {box} {box}
end structure
""", file=f)

    # Run packmol
    os.system("packmol < packmol.inp")

    # Writing moltemplate system.lt file
    with open("system.lt", "w") as f:
        print(f"""
## Import the templates
""", file=f)

        # Loop to import each molecule's template file
        for name in names:
            print(f'import "{name}.lt"', file=f)

        print("\n# Define the number of molecules", file=f)

        # Loop to define each molecule with its respective count
        for i in range(len(names)):
            print(f"molec_{i+1} = new {names[i]}[{nmol[i]}] #.move(0,0,15.5171)", file=f)

        # Define the box size
        print(f"""
## Create the box. The box size is in Angstrom
write_once("Data Boundary") {{
   0.0  {box}  xlo xhi
   0.0  {box}  ylo yhi
   0.0  {box}  zlo zhi
}}
""", file=f)

    # Run moltemplate
    os.system(f"moltemplate.sh -pdb system.pdb system.lt")

    ## remove temporary files
    os.system("rm -rf output_ttree")

    with open("system.lt", "r") as f:
        data = f.read()
    return data
