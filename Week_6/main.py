import string
import random
import pandas as pd

# # work 1 Start
#
# characters = string.ascii_letters
#
# firstDataSet = {
#     'first': [''.join(random.choice(characters) for _ in range(10)) for _ in range(100)],
#     'second': [random.randint(0, 10) for _ in range(100)],
#     'third': [random.randint(0, 7) for _ in range(100)],
#     'four': [random.randint(1, 100) for _ in range(100)]
# }
#
# myvar = pd.DataFrame(firstDataSet)
# # myvar.to_excel("data.xlsx", index=False)
# # myvar.to_excel("data.xlsx", index=False, sheet_name='sheetOne')
#
# # work 1 End
#
# # work 2 Start
#
# massive_names = [
#     "John", "Alice", "Bob", "Eleanor", "David", "Olivia", "Liam", "Sophia", "Mason", "Ava", "William", "Charlotte",
#     "James", "Isabella", "Henry", "Amelia", "Michael", "Harper", "Emma", "Alexander", "Daniel", "Oliver", "Evelyn",
#     "Benjamin", "Sophie", "Matthew", "Mia", "Ethan", "Scarlett",
# ]
#
# massive_last_names = [
#     "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
#     "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
#     "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Young", "King", "Scott", "Green",
# ]
#
# secondDataSet = {
#     'first': [random.randint(1, 100) for _ in range(50)],
#     'second': [random.choice(massive_names) for _ in range(50)],
#     'third': [random.choice(massive_last_names) for _ in range(50)],
#     'four': [random.randint(2000, 5000) for _ in range(50)]
# }
#
# myvar2 = pd.DataFrame(secondDataSet)
# # with pd.ExcelWriter('data.xlsx', mode='a') as writer:
# #    myvar2.to_excel(writer, sheet_name='sheetTwo', index=False)
#
# # work 2 End
#
# # work 3 Start

input_file = 'data.xlsx'
output_file = 'datanew.xlsx'

# xls = pd.read_excel(input_file, sheet_name=None)
#
# with pd.ExcelWriter(output_file) as writer:
#     for sheet_name, df in xls.items():
#         df.to_excel(writer, sheet_name=sheet_name, index=False)

# # work 3 end

# work 4 start

# data_df = pd.read_excel('data.xlsx')
# filtered_df = data_df[data_df['first'].str.contains('a')]

# df = pd.read_excel('datanew.xlsx')

# df = df._append(filtered_df, ignore_index=True)

# with pd.ExcelWriter('datanew.xlsx', mode='a') as writer:
#     df.to_excel(writer, sheet_name='sheet3')

# end work 4

# start work 5

# df = pd.read_excel('data.xlsx', sheet_name='sheetTwo')
# column_4 = df.iloc[:, 3]
# new_df = column_4.nlargest(10)
#
# df = pd.read_excel('datanew.xlsx')
# df = df._append(new_df, ignore_index=True)
#
# with pd.ExcelWriter('datanew.xlsx', mode='a') as writer:
#     df.to_excel(writer, sheet_name='sheet4')

# end work 5

# start work 6

# df = pd.read_excel('file_example_XLSX_1000.xlsx')
# df.sort_values(by='Id', ascending=True)
# average_age = df['Age'].mean()
# max_age = max(df['Age'])
# min_age = min(df['Age'])

# end work 6

# start work 7

df = pd.read_excel('staff_1000.xlsx')
new_df = df[(df['Age'] >= 30) & (df['Age'] <= 40)]
new_df.to_excel('staff_age.xlsx', index=False)

# end work 7
