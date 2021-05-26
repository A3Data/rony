# Example os simple processing job done in sagemaker
import argparse
import pandas as pd

def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/A3Data/hermione/master/hermione/file_text/train.csv')

def make_transformation(df):
    """
    Calculate mean centered age
    """
    df['mcAge'] = df.Age - df.Age.mean()
    return df

def filter_sex(sex):
    return df.loc[df.Sex == sex]

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sex", help="choose a sex category to filter data", 
                        type=str, choices=['male', 'female', 'both'], default='both')
    args = parser.parse_args()
    
    df = get_data()

    if args.sex != 'both':
        df = filter_sex(args.sex)
    
    df = make_transformation(df)
    
    print(df)