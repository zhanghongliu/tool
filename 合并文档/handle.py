# with open("orgin.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     #print(lines)
# with open("new.txt","w",encoding="utf-8") as f_w:
#     for line in lines:
#         if "山水中" in line:
#             continue
#         if '艾米安' in line:
#             continue
#         if '刘云斌' in line:
#             continue
#         if '灵汐' in line:
#             continue
#         if '呗一明' in line:
#             continue
#         if(line.startswith('\n')):
#             continue
#         f_w.write(line.replace('\n',' '))

import os

# 遍历文件夹
def walkFile(file):
    tables = ['auth_role.sql', 'project.sql', 'admin.sql', 'agent.sql', 'cloud.sql', 'cloud_server.sql',  'server_config.sql', 'orders.sql', 'product.sql',  'seller.sql', 'service_info.sql'];
    # tables = ['auth_role.sql', 'project.sql', 'admin.sql', 'agent.sql', 'cloud.sql', 'cloud_server.sql', 'server_config.sql', 'orders.sql', 'product.sql', 'service_info.sql'];
    with open(file + "mysql.sql", "w", encoding="utf-8") as f_w:
        for table in tables :
            with open(file+table,"r",encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    f_w.write(line)

def main():
    walkFile("D:/sql/")


if __name__ == '__main__':
    main()