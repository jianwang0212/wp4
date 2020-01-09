import pandas as pd
pd.options.mode.chained_assignment = None
df = pd.read_excel('oxfordshire_lep_with_text.xlsx',
                   sheet_name='Construction 2019')


def element_to_list(element):
    return str(element).replace(";", "&").replace('"', "").split("&")


def frequency_count_skill_cluster(df):
    df = df[['JobID', 'JobText', 'SICCode',
             'CanonSkillClusters', 'SOCCode', 'CanonSkillClusters']]
    df['CanonSkillClusters'] = df['CanonSkillClusters'].apply(element_to_list)

    s = df.apply(lambda x: pd.Series(x['CanonSkillClusters']), axis=1).stack(
    ).reset_index(level=1, drop=True)
    s.name = 'CanonSkillClusters'
    s = df.drop('CanonSkillClusters', axis=1).join(s)

    df2 = pd.DataFrame(s['CanonSkillClusters'].value_counts())
    common = df2.loc[df2['CanonSkillClusters'].idxmax()].name
    df_common = s[s['CanonSkillClusters'] == "Plumbing"]
    return df2, df_common


df = df[['JobID', 'JobText', 'SICCode',
         'CanonSkillClusters', 'SOCCode']]
# df['CanonSkillClusters'] = df['CanonSkillClusters'].apply(element_to_list)


# df2, df_common = frequency_count_skill_cluster(df)
print(df['CanonSkillClusters'])
# print(df_common.head)
