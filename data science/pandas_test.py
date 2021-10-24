import pandas as pd


def load_data():

    vul = pd.read_csv(".\\data\\vulner.csv")
    ast = pd.read_csv(".\\data\\assets.csv")
    return vul, ast
    
# print (df.head())

# y = df.groupby(['risk']).count()
# print ("df.groupby(['risk']).count()", '\n', y)


# v_nrisk = df[['name','risk']]
# x = v_nrisk[v_nrisk['risk'] == 'High'].count()

# print ("v_nrisk[v_nrisk['risk'] == 'High'].count()", '\n', x)


# select rows based on field criteria
# x = df['risk'] == 'High'
# print ("df['risk'] == 'High'", '\n', x)

# v_nrisk = df[['name','risk']]
# x = v_nrisk[v_nrisk['risk'].isin(['High', 'Medium'])]

# print ('High & Medium:',x)

# print ("Unique risks: ", df['risk'].unique())


# grp = df[['name', 'risk', 'vulnid']].loc[df["risk"] == 'High']
# print (grp)

# print (df.columns)
def test_groupby():
    vul,ast = load_data()
    x = vul[['name', 'risk', 'vulnid']].groupby(['name', "risk"]).count().reset_index()
    print (x.iloc[0:200,:])
    print (x.loc[50:,['name','risk', 'vulnid']])

    print ('-------- Pivot ------------')
    y = vul[['name', 'risk', 'vulnid']].groupby(['name', "risk"],as_index = False).count().pivot('name', "risk").fillna(0)
    print (y)

def test_join():
    vul,ast = load_data()
    va = vul.join(ast.set_index('ipaddress'), on = 'ipaddress', lsuffix=", rsuffix=")
    print(va.head())
    x = va[['profile_group', 'risk', 'vulnid']].groupby(['profile_group', 'risk'],as_index = False).count().pivot('profile_group', "risk").fillna(0)
    print ('Pivot: ',x, '\n------------------------------------')
    print ( va.iloc[:10]['name'])
    
# test_join()
if __name__ == '__main__':
    test_join()