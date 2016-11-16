# UK Local Authority Names and Codes Lookup
Lookup between the many, many different ways of naming and coding UK local authorities.

If you ever try to match UK local authority statistics against each other you'll quickly find your efforts frustrated by inconsistent uses of official codes and different versions of LA names. These lookups are an ongoing  tool to help translate between these. 

* The _local_authorities.csv files contain the table to match between different codes. 
* The _messy_lookup.csv files combine all alternate names into one column to let you quickly match any data and get back a canonical code (which can be checked against the other table to convert to your preferred format). 

##English Local Authorities

For  English Local Authorities I use the [Local Authorities in England](https://local-authority-eng.register.gov.uk/) register as the base. This register provides a canonical three character code and a canonical name for the local authority. This is then expanded with current and older ONS codes and varying forms of the LA name. 

Useful fields:

* local-authority-eng - canonical three character code
* official-name - canonical local authority name
* alt-name-1 - canonical shorter name
* alt-name-2 - variations on name
* alt-name-3 - variations on name
* gss-code - current standard 9-character ONS code.
* old-ons-la-code - old ONS code for local authorities. 
* ualad99 - older local authority code used in coding survey responses (for instance in OFCOM's [Connected Nations report](https://www.ofcom.org.uk/research-and-data/infrastructure-research/connected-nations-2015))


##Scottish, Welsh and N. Irish Local Authorities

As there is currently no offical register for these, I've simply made a quick lookup using the gss code as the ID with a few name variants.

* gss-code - current standard 9-character ONS code.
* offical-name - ONS name for local authoirty
* alt-name-1 - variations on name
* alt-name-2 - variations on name
* ualad99 - older local authority code used in coding survey responses (for instance in OFCOM's [Connected Nations report](https://www.ofcom.org.uk/research-and-data/infrastructure-research/connected-nations-2015))
