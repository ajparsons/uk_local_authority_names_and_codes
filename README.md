# UK Local Authority Names and Codes Lookup
Lookup between the many, many different ways of naming and coding UK local authorities.

If you ever try to match UK local authority statistics against each other you'll quickly find your efforts frustrated by inconsistent uses of official codes and different versions of LA names. These lookups are an ongoing tool to help translate between these. 

* The uk_local_authorities.csv file contain the table to match between different codes. 
* The uk_local_authority_messy_lookup.csv file combine all alternate names into one column to let you quickly match any data and get back a canonical code (which can be checked against the other table to convert to your preferred format). Also combined with this [name lookup](https://github.com/openregister/local-authority-data/edit/master/maps/name.tsv) from openregister for fuller coverage.

This is using the official [local authority registers](https://github.com/openregister/local-authority-data) in development to provide a canonical three character code and a canonical name for the local authority. This is then expanded with current and older ONS codes and varying forms of the LA name (the real point of the exercise being to quickly get from horrible code-less data to other formats quickly).

Useful fields:

* local-authority-code - canonical three character code
* official-name - canonical local authority name
* parent-council - for london and non-metropolitan councils, id of GLA or overlapping county council. 
* alt-name-1 - canonical shorter name
* alt-name-2 - variations on name
* alt-name-3 - variations on name
* gss-code - current standard 9-character ONS code. *
* archaic-gss-code - old codes (changed because of boundary changes) to help with mismatches on some datasets (even recent datasets may use the wrong codes).
* snac - old ONS Standard Names and Codes code
* os - Ordnance Survey code
* old-ons-la-code - old ONS code for local authorities. 
* ofcom - variant on snac authority code used in coding survey responses (for instance in OFCOM's [Connected Nations report](https://www.ofcom.org.uk/research-and-data/infrastructure-research/connected-nations-2015))
* ecode - used in [revenue and accounting documents](https://www.gov.uk/government/collections/local-authority-revenue-expenditure-and-financing)


Additional maps can be found [here](https://github.com/openregister/local-authority-data/tree/master/maps).

*The code used for the Greater London Authority is the gss code is for London region - when working from code point open use E18000007 and the NHS_HA_code column.
