"""
Generate a unified cats.csv and columns.csv file from the cats.ini file and the catrefs.csv file.
"""
import configparser
import pandas as pd


def ini_to_df(ini_file):
    """
    Parse the cats.ini file and return a dataframe with the following columns:
    [id, url, columns]
    """
    config = configparser.ConfigParser(interpolation=None)
    config.read(ini_file)
    # The Dataframe will have the following columns:
    # [id, url, columns]
    optional_columns = ["url", "columns"]
    df_columns = ["id"] + optional_columns
    data_frame = pd.DataFrame(columns=df_columns)  # disable=redefined-outer-name,invalid-name
    # Parse the sections in the ini file and create a new dataframe entry for each one
    data = []
    for section in config.sections():
        row_data = [section]
        for col in optional_columns:
            if col in config[section]:
                row_data.append(config[section][col])
        data.append(row_data)
    data_frame = pd.DataFrame(data, columns=df_columns)  # disable=invalid-name
    return data_frame



if __name__ == "__main__":
    # df = ini_to_df("cats.ini")
    # # write the dataframe file in different formats
    cats_df = pd.read_csv("cats/cats.csv")
    ref_df = pd.read_csv("cats/catrefs.csv", sep=';', skipinitialspace=True)
    # remove duplicates from both dataframes
    cats_df.drop_duplicates(subset='id', inplace=True)
    ref_df.drop_duplicates(subset='id', inplace=True)
    # The column "columns" in the cats.csv file contains a list of
    # columns that should be used for the
    # corresponding id. This list is a string, so we need to convert it
    # to a list of strings.
    # convert the column "columns" to a list of strings (split by comma)
    cats_df['columns'] = cats_df['columns'].apply(
        lambda x: x.split(',') if isinstance(x, str) else x
    )
    # create a new dataframe with the columns "id" and "columns"
    columns_df = cats_df[['id', 'columns']]
    # explode the column "columns" to multiple rows
    columns_df = columns_df.explode('columns')
    # rename the column "columns" to "name"
    columns_df.rename(columns={'columns': 'name'}, inplace=True)
    columns_df.rename(columns={'id': 'cat_id'}, inplace=True)
    # remove duplicates from the columns dataframe
    columns_df.drop_duplicates(inplace=True)

    # remove the column "columns" from the cats dataframe
    cats_df.drop(columns=['columns'], inplace=True)


    # join the two dataframes with a full outer Join on the id column
    df = pd.merge(cats_df, ref_df, on='id', how='outer')
    # sort the dataframe by the id column
    df.sort_values(by=['id'], inplace=True)
    df.to_csv("cats/unified_cats.csv", index=False)

    # write the columns dataframe to a csv file
    columns_df.to_csv("cats/unified_columns.csv", index=False)

    move_to_defaults = input("Move the unified cats and columns to the defaults folder? (y/n): ")
    if move_to_defaults.lower() == 'y':
        import shutil
        shutil.copy("cats/unified_cats.csv", "packages/blazar_proxy/defaults/cats.csv")
        shutil.copy("cats/unified_columns.csv", "packages/blazar_proxy/defaults/vertices.csv")
        print("Moved the unified cats and columns to the defaults folder.")
    print("Done.")
