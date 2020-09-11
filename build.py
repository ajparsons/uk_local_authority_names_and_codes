"""
Builds easy two column lookups from all the alternative names

"""
from useful_inkleby.files import QuickGrid




def build_messy_lookup(source,dest,ref_col):
    """
    given source and destination, will pull together all alt names to give a nice easy lookup
    """
    la = QuickGrid().open(source)
    od = QuickGrid().open("source_files\\local_authority_data_names.csv")
    
    lookup = QuickGrid()
    lookup.header = ["la name",ref_col]

    possible = ["official-name","alt-name-1","alt-name-2","alt-name-3"]
    possible = [p for p in possible if p in la.header]
    for r in la:
        for p in possible:
            if r[p]:
                lookup.add([r[p],r[ref_col]])
    
    current_names = [x[0] for x in lookup]

    for r in od:
        if r["name"] not in current_names:
            code = r["local-authority"].split(":")[1]
            lookup.add([r["name"],code])
    
    lookup.save(dest,force_unicode=True)
    
    
def build_messy_lookup_lad(source,dest):
    """
    given source and destination, will pull together all alt names to give a nice easy lookup
    """
    la = QuickGrid().open(source)

    lookup = QuickGrid()
    lookup.header = ["gss-code","local-authority-code"]

    possible = ["gss-code","archaic-gss-code"]
    possible = [p for p in possible if p in la.header]
    for r in la:
        for p in possible:
            if r[p]:
                values = r[p].split(",")
                for v in values:
                    lookup.add([v,r["local-authority-code"]])
    
    lookup.save(dest,force_unicode=True)
    
def create_csv(source,dest):
    qg = QuickGrid().open(source)
    qg.save(dest,force_unicode=True)
    
if __name__ == "__main__":
    build_messy_lookup("uk_local_authorities.xlsx",
                       "lookup_name_to_registry.csv",
                       "local-authority-code") 
    build_messy_lookup_lad("uk_local_authorities.xlsx",
                           "lookup_gss_to_registry.csv",)
    create_csv("uk_local_authorities.xlsx",
               "uk_local_authorities.csv")
