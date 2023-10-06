# import pandas as pd
# import pandas_dedupe

# # #load dataframe
# # df = pd.read_csv('data/3d_curr.csv')

# # print(df.head())

# # #initiate deduplication
# # df_final = pandas_dedupe.dedupe_dataframe(df,'class')

# # #send output to csv
# # df_final.to_csv('deduplication_output.csv')


# df = pd.DataFrame({'class': ['Iris-setosa', 'Iris-setossa', 'Iris-versicolor', 'Iris-virginica', 'versicolor', 'iris-setosa', 'versicolor']})


# if __name__ == '__main__':
#     dd = pandas_dedupe.dedupe_dataframe(
#         df, 
#         field_properties = ['class'], 
#         sample_size=1,
#         canonicalize=True
#         )
    
#     print(dd)


import pandas as pd
import pandas_dedupe

# path to 3d-printing data CSV file
csv_file = 'data/3d_curr.csv'

# Use pandas to read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# convert timestamp column from str to pd.Timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# #load dataframe
# df = pd.read_csv('test_names.csv')

# actual list of classes:
class_list = ["Pass. Pursuit", "PIE", "DFM", "Scope", "IS", "DesNat",
              "Ren. Energy", "EEC", "Mech Proto", "QEA", "Research",
              "P&M", "SustDes", "RoboSys", "DBF", "Personal Proj.",
              "Test Piece", "Proj. Team/Club", "Class/Research Unspec"]

# #send output to csv
# df_final.to_csv('class_deduplication_output.csv')

if __name__ == '__main__':
    #initiate deduplication
    # class_dd = pandas_dedupe.dedupe_dataframe(df,['class'], canonicalize=True, )
    class_dd = pandas_dedupe.dedupe_dataframe(
        df, 
        field_properties = ['class'], 
        sample_size=1,
        canonicalize=class_list
        )

    pre_dd_classes = df["class"].unique()
    dd_classes = class_dd["class"].unique()