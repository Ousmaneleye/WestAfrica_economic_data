import requests
import pandas as pd

######## Get source_data(html) ###############
url = "https://fr.countryeconomy.com/pays/groupes/communaute-economique-etats-afrique-ouest/"
response = requests.get(url)
response_html = response.text
#########################################

######### Renaming columns ##############
westafrica_df = pd.read_html(response_html)[0]
columns = {
    "Pays": "pays",
    "Population": "population",
    "PIB annuel": "PIB/an (M. €)",
    "PIB annuel.1": "PIB/an (M. $)",
    "Dette totale (M. €)": "Dette_totale (M. €)",
    "Dette totale (M. $)": "Dette_totale (M. $)",
    "PIB par habitant": "PIB/hbt (€)",
    "PIB par habitant.1": "PIB/hbt ($)",
}
westafrica_df.rename(columns=columns, inplace=True)
########################################

############ Cleaning data #############
westafrica_df['pays'] = westafrica_df['pays'].apply(lambda x: x.replace("[+]", '').strip())
westafrica_df['population'] = westafrica_df['population'].apply(lambda x: int(x.replace(".","")))
westafrica_df['PIB/an (M. €)'] = westafrica_df['PIB/an (M. €)'].apply(lambda x: int(x.split()[0].replace(".","")))
westafrica_df['PIB/an (M. $)'] = westafrica_df['PIB/an (M. $)'].apply(lambda x: int(x.split()[0].replace(".","")))
westafrica_df['PIB/hbt (€)'] = westafrica_df['PIB/hbt (€)'].apply(lambda x: int(x.split()[0].replace(".","")))
westafrica_df['PIB/hbt ($)'] = westafrica_df['PIB/hbt ($)'].apply(lambda x: int(x.split()[0].replace(".","")))
westafrica_df['Dette (%PIB)'] = westafrica_df['Dette (%PIB)'].apply(lambda x: float(x.replace("%","").replace(",",".")))
westafrica_df['Déficit (%PIB)'] = westafrica_df['Déficit (%PIB)'].apply(lambda x: float(str(x).replace("%", "").replace(",",".")))
westafrica_df.dropna(axis=0, inplace=True)

westafrica_df.loc[0, "pays"] = "Benin"
westafrica_df.loc[1, "pays"] = "Burkina Faso"
westafrica_df.loc[2, "pays"] = "Cap Vert"
westafrica_df.loc[3, "pays"] = "Ivory Coast"
westafrica_df.loc[4, "pays"] = "Gambia"
westafrica_df.loc[6, "pays"] = "Guinea"
westafrica_df.loc[7, "pays"] = "Guinea Bissau"
westafrica_df.loc[12, "pays"] = "Senegal"
westafrica_df.sort_values('pays', inplace=True)
########################################
