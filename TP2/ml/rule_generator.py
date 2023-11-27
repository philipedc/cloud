import os
import ssl
import pandas as pd
import pickle
from fpgrowth_py import fpgrowth

ssl._create_default_https_context = ssl._create_unverified_context
DATASET_URL = os.environ.get('DATASET_URL')

RULES_PATH = './rules/'

def generate_rules(df):
    df = df.loc[:, ['pid', 'track_name', 'artist_name']]
    df.dropna()
    grouped_df = df.groupby('pid').agg({'track_name': list, 'artist_name': list}).reset_index()
    item_set_list = grouped_df['track_name'].values.tolist()
  
    freqItemSet, rules = fpgrowth(item_set_list, minSupRatio=0.07, minConf=0.5)
  
    # Format rules
    formatted_rules = []
    for rule in rules:
        formatted_rules.append([str(list(rule[0])[0]), str(list(rule[1])[0]), rule[2]])
  
    return formatted_rules
  
df = pd.read_csv(DATASET_URL)

basic_rules = generate_rules(df)

with open(RULES_PATH + "basic_rules.pkl", 'wb+') as f:
    pickle.dump(basic_rules, f)
    
# Debug
## model = pickle.load(open(RULES_PATH + "basic_rules.pkl", "rb"))
## print(f"After pickle: {model[:10]}")
