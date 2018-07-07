
class ResponseError(Exception):
    """响应错误"""
    def __init__(self,code,msg,**kwargs):
        self.__code__=code
        self.__msg__=msg
    def __str__(self):
        return "[code:%d]%s" %(self.__code__,self.__msg__)

def check(response_body):
    """返回一个元组，分别为响应的代码和消息"""
    obj=None
    if isinstance(response_body,dict):
        obj=response_body
    elif isinstance(response_body,str): # 支持转换json文本
        import json
        obj=json.loads(response_body)
    else: 
        raise TypeError('response_body 应该是 str 或者 dict 类型')
    if 'code' not in obj:
        raise ValueError('响应体中未找到code！')
    return obj['code'],obj['message'] if 'message' in obj else None

def raise_check(response_body,ignore_codes=[],error_dict={}):
    """如果未通过响应代码检查，则抛出响应异常
    response_body:欲检查的响应体
    ignore_codes:忽视的代码列表
    error_dict:存放错误的字典
    """
    code,msg=check(response_body)
    if code and code not in ignore_codes:
        if code in error_dict:
            raise error_dict[code](code,msg)
        raise ResponseError(code,msg)
    