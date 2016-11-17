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
    
    for r in od:
        lookup.add([r["name"],r["local-authority"].split(":")[1]])
    
    lookup.save(dest)
    
    
if __name__ == "__main__":
    build_messy_lookup("uk_local_authorities.csv",
                       "uk_local_authority_messy_lookup.csv",
                       "local-authority-code") 
