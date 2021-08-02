"""
Builds easy two column lookups from all the alternative names

"""
import pandas as pd
from pathlib import Path


def build_messy_lookup(source, dest, ref_col):
    """
    given source and destination, will pull together all alt names to give a nice easy lookup
    """
    la = pd.read_excel(source)
    od = pd.read_csv(Path("source_files", "local_authority_data_names.csv"))

    lookup_data = []

    possible = ["official-name", "alt-name-1", "alt-name-2", "alt-name-3"]
    possible = [p for p in possible if p in la.columns]
    for _, r in la.iterrows():
        for p in possible:
            if pd.isna(r[p]) is False:
                lookup_data.append([r[p], r[ref_col]])

    current_names = [x[0] for x in lookup_data]

    for _, r in od.iterrows():
        if r["name"] not in current_names:
            code = r["local-authority"].split(":")[1]
            lookup_data.append([r["name"], code])

    lookup = pd.DataFrame(lookup_data, columns=["la name", ref_col])
    lookup.to_csv(dest, index=False)


def build_messy_lookup_lad(source, dest):
    """
    given source and destination, will pull together all alt names to give a nice easy lookup
    """
    la = pd.read_excel(source)

    lookup_data = []
    possible = ["gss-code", "archaic-gss-code"]
    possible = [p for p in possible if p in la.columns]
    for _, r in la.iterrows():
        for p in possible:
            if r[p]:
                values = [x for x in str(r[p]).split(",") if x != "nan"]
                for v in values:
                    lookup_data.append([v, r["local-authority-code"]])

    lookup = pd.DataFrame(lookup_data, columns=[
                          "gss-code", "local-authority-code"])
    lookup.to_csv(dest, index=False)


def add_sources_to_csv(source, dest):

    extra_info = [Path("source_files", "la_area_pop.csv"),
                  Path("source_files", "la_xy.csv")]

    df = pd.read_excel(source).set_index("local-authority-code")
    for extra in extra_info:
        ndf = pd.read_csv(extra).set_index("local-authority-code")
        df = df.join(ndf)

    df.reset_index().to_csv(dest, index=False)


if __name__ == "__main__":
    build_messy_lookup("uk_local_authorities.xlsx",
                       "lookup_name_to_registry.csv",
                       "local-authority-code")
    build_messy_lookup_lad("uk_local_authorities.xlsx",
                           "lookup_gss_to_registry.csv",)
    add_sources_to_csv("uk_local_authorities.xlsx",
                       "uk_local_authorities.csv")
