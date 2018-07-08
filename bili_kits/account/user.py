import requests,time

from ..api import user,account
from ..utils.response_check import ResponseError,resp_check

class UserNotLoginError(ResponseError):
    def __init__(self,code,msg):
        super().__init__(code,msg)

@resp_check(result_func=lambda r:r['data']['card'])
def get_user_card_info(mid,photo = False):
    """获取指定用户的卡片信息\n
    mid:用户的唯一数字标识\n
    photo:[可选]是否返回包含空间头图的数据
    """
    r = requests.get(user.CARD,params = {"mid":mid,"photo":photo})
    r.raise_for_status()
    return r.json()

class BaseUser(object):
    def __init__(self):
        # 初始化当前对象的session
        self.__session__ = requests.session()

    def __del__(self):
        # 安全关闭session
        self.__session__.close()

    @property
    @resp_check(error_dict={-101:UserNotLoginError},result_func=lambda r:int(r['access_info']['expires']))
    def expires(self):
        """获取当前用户的有效生存截止时间"""
        r = self.session.get(account.OAUTH)
        r.raise_for_status()
        return r.json()

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
    @resp_check(error_dict={-101:UserNotLoginError},result_func=lambda r:r['data'])
    def nav_info(self):
        """获取当前用户的导航栏信息"""
        r = self.session.get(user.NAV)
        r.raise_for_status()
        return r.json()

class WebUser(BaseUser):
    pass
class ClientUser(BaseUser):
    pass



