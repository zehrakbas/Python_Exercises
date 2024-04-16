# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

# Beklenen Çıktı

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
import pandas as pd

# veri setinin içindeki max. sütunlar gözükmeli
pd.set_option('display.max_columns', None)

# veri setinin içindeki görüntüyü genişletme
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.head()
df.columns
df.info()


df["total"].dtype
df["speeding"].dtype
df["alcohol"].dtype
df["not_distracted"].dtype
df["no_previous"].dtype
df["ins_premium"].dtype
df["ins_losses"].dtype
df["abbrev"].dtype

for col in df.columns:
    print(df[col].dtype)



# List Comprehension
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# Alternative(Düz Mantık)
for col in df.columns:
    if df[col].dtype != "O":
        print("NUM_" + col.upper())
    else:
        print(col.upper())


# Function

def column(data):
    for col in data.columns:
        if data[col].dtype != "0":
            print("NUMERIC " + col.upper())
        else:
            print(col.upper())

column(df)

# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

# Notlar:

# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.

# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Alternative
for col in df.columns:
    if "no" not in col:
        print(col.upper() + "_FLAG")
    else:
        print(col.upper())
# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan eğişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

# Notlar:
# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# Beklenen çıktı:

#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630


og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


[col for col in df.columns if col not in og_list]
# Alternative


og_list = [col for col in df.columns if "rev" in col ]

# Function
def compre(data):
    new_cols = [col for col in data.columns if col not in og_list]
    new_df = data[new_cols]
    print(new_df.head())

# if çıktısı -- for döngüsü --- if eğer kısmı
[col for col in data.columns if col not in og_list]


compre(df)
