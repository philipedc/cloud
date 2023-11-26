# import pandas as pd
# import pickle
# from fpgrowth_py import fpgrowth

# # Change path when on VM
# FILEPATH_DS1 = './2023_spotify_ds1.csv'
# FILEPATH_DS1 = './2023_spotify_ds1.csv'

# RULES_PATH = './'

# def generate_rules(df):
#     df = df.loc[:, ['pid', 'track_name', 'artist_name']]
#     df.dropna()
#     grouped_df = df.groupby('pid').agg({'track_name': list, 'artist_name': list}).reset_index()

#     item_set_list = grouped_df['track_name'].values.tolist()
    
#     freqItemSet, rules = fpgrowth(item_set_list, minSupRatio=0.07, minConf=0.5)
    
#     # Format rules
#     formatted_rules = []

#     for rule in rules:
#         formatted_rules.append([str(list(rule[0])[0]), str(list(rule[1])[0]), rule[2]])
    
#     return formatted_rules
    
# first_df = pd.read_csv(FILEPATH_DS1)
# second_df = pd.read_csv(FILEPATH_DS1)

# improved_df = pd.concat([first_df, second_df], ignore_index=True)

# basic_rules = generate_rules(first_df)
# with open(RULES_PATH + "basic_rules.pkl", 'wb+') as f:
#     pickle.dump(basic_rules, f)

# #improved_rules = generate_rules(improved_df)
# #with open(RULES_PATH + "improved_rules.pkl", 'wb+') as f:
# #    pickle.dump(improved_rules, f)