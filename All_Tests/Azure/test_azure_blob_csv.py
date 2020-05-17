import pandas as pd 
import pytest

"""
Notes for Pytest
Modules must be name test_*.py or *_test.py
optionally inside classes names Test*
"""

@pytest.fixture
def setup_df():
    source="https://storexyz.blob.core.windows.net/storexyz/FinancialDataNZ.csv?sp=r&st=2020-05-17T07:26:43Z&se=2020-05-17T15:26:43Z&sip=94.10.246.176&spr=https&sv=2019-10-10&sr=b&sig=uZQ41k28eJPK%2FwWBGTA%2FHe8P6rJtmmerdchJYJkVfDs%3D"
    df = pd.read_csv(source)
    return df
    #yield
    #df.close()

def test_Industry_aggregation_NZSIOC_must_be_999(setup_df):
    err_found = 0
    for index, row in setup_df.iterrows():
        if not str(row['Variable_code']).startswith("H1"):
            err_found += 1
            print("Should start with 'H1' but is: "+str(row['Variable_code']))
    assert err_found == 0


""" BACKUP code:
#validate column data
for index, row in df.iterrows():
    print(row['PersonIdentifier'])
    if not str(row['PersonIdentifier']).startswith("SKY"):
        print("err PersonIdentifier should start with 'SKY'")
    if str(row['SkyCampaignChannelTypeCode']) not in {'POS', 'EMA', 'SMS'}:
        print("Invalid entry for SkyCampaignChannelTypeCode."+str(row['SkyCampaignChannelTypeCode']))
    if str(row['SkyMultiroomFlag']) not in {'N', 'Y'}:
        print("Invalid entry for SkyMultiroomFlag."+str(row['SkyCampaignChannelTypeCode']))

#filter column data
df = main_data.loc[main_data['SkyCampaignChannelTypeCode'] == 'POS']
print(df)
"""
