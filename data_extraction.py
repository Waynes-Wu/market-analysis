import re  
import pandas as pd

PATTERN = r"(\d+\.\d+)\s*percent"  


def extractAndReturnRates(text):
    rates = re.findall(PATTERN, text)
    # 
    rates = pd.Series(map(float, rates), index=["TRRR", "ODIR", "LFIR"])
    return rates

# dummyText = """The Monetary Board decided to keep the BSP's Target Reverse Repurchase Rate at 5.75 percent. The interest rates on the overnight deposit and lending facilities thus remain at 5.25 percent and 6.25 percent, respectively."""  
# print(extractAndReturnRates(dummyText))

interest_df = pd.read_excel('./data/MonetaryPolicyDecisions.xlsx')
interest_df.columns = interest_df.columns.str.strip()
# TRRR Target Reverse Repurchase Rate 
# ODIR overnight deposit interest rate
# LFIR lending facility interest rate
interest_df[["TRRR", "ODIR", "LFIR"]] = interest_df["Description"].apply(extractAndReturnRates)
interest_df.drop(columns=["Description"], inplace=True)
interest_df.to_csv("./data/monetaryDeicisionProcessed.csv", index=False)
