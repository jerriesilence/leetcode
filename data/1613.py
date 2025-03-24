import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    customer_num = customers['customer_id'].max()
    full_list = pd.Series(data = list(range(1,customer_num+1)), name = 'customer_id' )
    new_df = pd.merge(left = full_list, right = customers, how = 'left', on = 'customer_id')

    df = new_df[new_df['customer_name'].isnull()]
    df = df['customer_id'].to_frame()
    # for df only,df = df.rename(columns={"customer_id": "ids"})
    # for series： df.rename('ids', axis = 0)
    return df.rename(columns={"customer_id": "ids"})