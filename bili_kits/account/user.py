import requests,time

from ..api import user,account
from ..utils import response_check

class UserNotLoginError(response_check.ResponseError):
    def __init__(self,code,msg):
        super().__init__(code,msg)

def get_user_card_info(mid,photo = False):
    """获取指定用户的卡片信息\n
    mid:用户的唯一数字标识\n
    photo:[可选]是否返回包含空间头图的数据
    """
    r = requests.get(user.CARD,params = {"mid":mid,"photo":photo})
    r.raise_for_status()
    result = r.json()
    response_check.raise_check(result)
    return result['data']['card']

class BaseUser(object):
    def __init__(self):
        # 初始化当前对象的session
        self.__session__ = requests.session()

    def __del__(self):
        # 安全关闭session
        self.__session__.close()
    
    def _convert_response(self,response):
        response.raise_for_status()
        result=response.json()
        response_check.raise_check(result,error_dict={-101:UserNotLoginError})
        return result

    @property
    def expires(self):
        """获取当前用户的有效生存截止时间"""
        result = self._convert_response(self.session.get(account.OAUTH))
        return time.localtime(int(result['access_info']['expires']))

    @property
    def islogined(self):
        """获取当前用户的是否已登录"""
        try:
            return bool(self.expires)
        except UserNotLoginError:
            return False
    @property
    def session(self):
        """获取当前用户使用的session"""
        return self.__session__

    @property
    def nav_info(self):
        """获取当前用户的导航栏信息"""
        result = self._convert_response(self.session.get(user.NAV))
        return result['data']

class WebUser(BaseUser):
    pass
class ClientUser(BaseUser):
    pass



