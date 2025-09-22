# Dev Diary - 2025-09-17
## What we did
-[] modify the API URL for Positive and Negative Datasets
-[] 
## what we learned 
- python JSON un-wrapper deals deals with fields as nested lists
- sometimes it's better to limit the number of entries from the API call; just because it will be computationally less expensive.
## Next steps
- erification of numerosity of the datasets all together (Amir and Bianca checked quickly)
- Collection of the datasets as json files running the script
- Figuring out how to extract the FASTA format (maybe through the TSV)
## Notes 
BG - I edited the notebook:
> The last function was splitted in 2 functions, one for pos and one for negs 
> The I commented out the filter_neg_entry function because idk if we actually need it
> I commented the fact that instead of one output_file variable we need 2, one for pos and one for neg
> I started the editing of the last cell of the notebook calling the 2 functions
