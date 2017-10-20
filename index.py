import xlrd     # excel module
import os
from sendemail import send

excel_path = "info.xlsx"
# excel_path = os.path.join('send_message', "info.xlsx")  # 0列：学号 1列：姓名 2列：邮箱地址 3列：需要发送的信息
data = xlrd.open_workbook(excel_path)
table = data.sheets()[0]    # sheet 0
nrows = table.nrows
for i in range(1, nrows): 
    data = table.row_values(i)
    id = data[0]
    name = data[1]
    emailaddr = data[2]
    message = data[3]
    subject = "测试邮件"
    content = """
        <p>%s你好，%s, 这是一封测试邮件~</p>
        <p>记得做心理测评,需要在23日八点前完成</p>
        <p>测试网址：http://xinli.gzedu.com/</p>
        <p>学校代码为:10141</p>
        <p>from：TaylorMei</p>
    """ % (message, id) 
    back = send(name, emailaddr, content, subject)
    print(back)
