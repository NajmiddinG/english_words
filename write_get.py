# # txtga o'tgazish
# import pandas as pd
# xl = pd.ExcelFile('2.xlsx')
# for sheet in xl.sheet_names:
#     file = pd.read_excel(xl, sheet_name=sheet)
#     file.to_csv(sheet + 'txt', header=False, index=False)

# # 2 ta txt ma'lumotini 3-ga o'tgazish
# f1 = open('words.txt', 'r')
# f2 = open('uzbek.txt', 'r')
# f3 = open('dictionary.txt', 'a')
# a = ""
# for i in range(1, 4341):
#     a = (f1.readline()).strip()+','+f2.readline()
#     f3.write(a)

# txtga o'tgazish
# import pandas as pd
# xl = pd.ExcelFile('2.xlsx')
# for sheet in xl.sheet_names:
#     file = pd.write(xl, sheet_name=sheet)
#     file.to_csv(sheet + 'txt', header=False, index=False)

# # exselga txt dan o'tgazish
# import pandas as pd

# excel = 'dictionary.txt'

# df = pd.read_csv(excel, sep=',')
# df.to_excel('englishwords.xlsx', index=False)