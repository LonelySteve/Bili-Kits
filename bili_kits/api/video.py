from . import _BASE_API_BILIBILI_COM,_BASE_API_BILIBILI_COM_X,_BASE_WEB_INTERFACE

_BASE_ARTICLE="%s/article" % _BASE_API_BILIBILI_COM_X
_BASE_PLAYER="%s/player" % _BASE_API_BILIBILI_COM_X
_BASE_TAG="%s/tag" % _BASE_API_BILIBILI_COM_X
# 获取视频快照
PVIDEO="%s/pvideo" % _BASE_API_BILIBILI_COM
# 获取视频总览数据，较为简洁，可用于统计数据
STAT="%s/archive/stat" % _BASE_WEB_INTERFACE
# 获取视频信息，返回的结果比较丰富
ARCHIVES="%s/archives" % _BASE_ARTICLE
ARCHIVE_TAGS="%s/archive/tags" % _BASE_TAG
PAGELIST="%s/pagelist" % _BASE_PLAYER