import pandas as pd

def users():
    fea_dir = "features\\features.txt"
    features = []

    with open(fea_dir, 'r') as f:
        features += f.readlines()

    a = [] 

    for i in range(len(features)):
        # split each user features by space
        a.append(features[i].split()) 

    final = []

    # make a dict that key is feature and value is corresponeding value
    for j in range(len(a)):
        b_col = []
        b_row = []
        for i in range(len(a[j][1:])):
            b_col.append(a[j][1:][i][::-1].split(';', 1)[1][::-1])
            b_row.append(a[j][1:][i].split(';')[-1])

        final.append(dict(zip(b_col, b_row)))

    df = pd.DataFrame(final).fillna(-1)
    #print(f"number of user:  {len(df)}")

    return df