
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # добавить корень проекта
# from utils.loger import log_error, log_info, log_warning


def calc(a, b):
    if(b == 0):
    #    log_error("Devide by zero is phobitted")
       return 
    
    return a /b 
    

# 
# if __name__ == '__main__':
#     print("Mymodule.py >>> ",__name__)
    
print("Mymodule.py has>>> ",__name__)
    
# calc(2, 0)