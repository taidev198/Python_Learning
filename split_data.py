import pandas as pd

data = """01/09/2024
5213.45946
01/09/2024
5090.85797
01/09/2024
5241.83107
01/09/2024
5218.87149
01/09/2024
5388.96713
01/09/2024
5212.91607
01/09/2024
5220.28596
01/09/2024
5388.33462
01/09/2024
5216.68569
01/09/2024
5387.37142
01/09/2024
5161.94345
01/09/2024
5219.94264",,"50.000
20.000
29.000
3.000
3.000
3.000
3.000
3.000
3.000
3.000
10.000
6.000",,"292976.010924.013647.xin cam on
VCB.CTDK.31/03/2024.ADIDA PHAT. CT tu
0481000755821 toi 0011001932418 MAT
TRAN TO QUOC VN - BAN CUU TRO TW
MBVCB.6916176124.CAO VIET TUAN
chuyen tien.CT tu 0101001222009 CAO VIET
TUAN toi 0011001932418 MAT TRAN TO
QUOC VN - BAN CUU TRO TW
272986.010924.101858.DO DUC LOI chuyen
tien
020097040509011046122024JDC5013867.96713
.104607.Vietcombank:0011001932418:DANG
THI THANH MHS533583
529474.010924.112032.BUI VAN DAI chuyen
tien
577301.010924.113215.DO DUC LOI MHS
4242
020097040509011137472024Y7ZE058213.33462
.113747.Vietcombank:0011001932418:NGUYE
N THI VAN chuyen tien
761664.010924.121847.NGUYEN VAN TUAN
chuyen tien
0200970405090112202020246WVI059470.3714
2.122015.Vietcombank:0011001932418:NGUYE
N QUANG THO 010166
PARTNER.DIRECT_DEBITS_VCB.ZLP.ZP6R
34H953F5.20240901.Nguyet chuyen tien qua
Zalopay
266303.010924.122804.NGUYEN THI MAO
Chuyen tien"""

# Split the data by ",," which separates the different types of data
sections = data.split('",,"')

# First section contains date and values
dates_and_values = sections[0].strip().split('\n')
dates = dates_and_values[0::2]  # Dates are at even indices
values = dates_and_values[1::2]  # Values are at odd indices

# Second section contains numbers
numbers = sections[1].strip().split('\n')

# Third section contains descriptions
descriptions = sections[2].strip().split('\n')

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Value': values,
    'Number': numbers,
    'Description': descriptions
})

# Display the DataFrame
print(df)

# Save to CSV
df.to_csv('output1.csv', index=False)