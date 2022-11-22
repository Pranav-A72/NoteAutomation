# import requests
# import sys
# import meaningcloud
# import os

# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# file_path = filedialog.askopenfilename()


# with open(file_path, 'w') as f:
#     f.write("  As you have read, the total fertility rate (TFR) is the average number of children one woman in a given region or country will have during her childbearing years. Social factors that affect a country’s TFR include level of health care and level of education for women. The total fertility rate is high in most peripheral countries, and although it has been trending down in recent years, the TFR still remains higher than the rates in core and semi-peripheral countries. In the 1990s, Afghanistan’s TFR was about 7.5, one of the highest in the world at the time. The country’s fertility rate in 2017 was 4.5. Improvements in health care, sanitation, and diet—along with better access to hospitals and medicine—generally cause a decline in the number of births. But when access to health care and education is limited, fertility rates skyrocket. In 2017, the countries with the highest TFRs were Niger (7.0), Somalia (6.2), and the Democratic Republic of Congo (6.0). All three countries in the periphery had fewer than 0.2 doctors per 1,000 people. In contrast, there were 4.0 doctors per 1,000 people in Argentina—a semi-peripheral country—the same year, and its TFR was 2.3. ")
text = ' Look at the HDI map and chart on page 526. Compare the dimensions used for Norway v Niger). rankings are diffrent. '
# license_key = '05820c2b4emshe8ad672ce51e1a4p1732e7jsn196f3864394f'
# # text = file_path
# sentences = 5
# summary = ''
# import requests

# url = "https://api.meaningcloud.com/summarization-1.0"

# payload={
#     'key': '05820c2b4emshe8ad672ce51e1a4p1732e7jsn196f3864394f',
#     'txt': file_path,
#     'sentences': 5
# }

# response = requests.post(url, data=payload)

# print('Status code:', response.status_code)
# print(response.json())

import requests

url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"

querystring = {"sentences":"5","txt":text}

headers = {
	"Accept": "application/json",
	"X-RapidAPI-Key": "05820c2b4emshe8ad672ce51e1a4p1732e7jsn196f3864394f",
	"X-RapidAPI-Host": "meaningcloud-summarization-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)