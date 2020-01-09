import pandas as pd
pd.options.mode.chained_assignment = None
df = pd.read_excel('oxfordshire_lep_with_text.xlsx',
                   sheet_name='Construction 2019')


def unicode_to_list(element):
    return eval(element.replace("' '", "','"))


def element_to_list(element):
    return str(element).replace(";", "&").replace('"', "").split("&")


def frequency_count_skill(df):
    df = df[['JobID', 'JobText', 'SICCode',
             'CanonSkillClusters', 'SOCCode', 'CanonSkills']]
    df['CanonSkills'] = df['CanonSkills'].apply(unicode_to_list)

    s = df.apply(lambda x: pd.Series(x['CanonSkills']), axis=1).stack(
    ).reset_index(level=1, drop=True)
    s.name = 'CanonSkills'
    s = df.drop('CanonSkills', axis=1).join(s)

    df2 = pd.DataFrame(s['CanonSkills'].value_counts())
    common = df2.loc[df2['CanonSkills'].idxmax()].name
    df_common = s[s['CanonSkills'] == "Plumbing"]
    return df2, df_common


def frequency_count_skill_cluster(df):
    df = df[['JobID', 'JobText', 'SICCode',
             'CanonSkillClusters', 'SOCCode']]
    df['CanonSkillClusters'] = df['CanonSkillClusters'].apply(element_to_list)

    s = df.apply(lambda x: pd.Series(x['CanonSkillClusters']), axis=1).stack(
    ).reset_index(level=1, drop=True)
    s.name = 'CanonSkillClusters'
    s = df.drop('CanonSkillClusters', axis=1).join(s)

    df2 = pd.DataFrame(s['CanonSkillClusters'].value_counts())
    common = df2.loc[df2['CanonSkillClusters'].idxmax()].name
    df_common = s[s['CanonSkillClusters'] == "Plumbing"]
    return df2, df_common


df2, df_common = frequency_count_skill_cluster(df)
print(df2.head)
print(df_common.head)
