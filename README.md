# api-tools-dynamate
Dynamte Tools API

## Examples

In this section we present examples of the molecular dynamics tools that have been added
to DynaMate's toolset.

## MosdDEF

The MosdDef tool creates a LAMMPS data file from a smiles string, the following command
shows the data that we need to send along our request to the REST API:

```sh
curl --header "Content-Type: application/json" --data '{"name":"ethanol","smiles":"CCO","length":"1","count":"1"}' --request POST http://localhost:8000/api/tool/mosdef
```

In a future commit we shall display the contents of the LAMMPS data file here.
