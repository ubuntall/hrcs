from django.contrib import admin

# Register your models here.
from .models import Msg, User, Note, Comment, Image


@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    # list_display = ('text', 'actualNickName', 'createTime', 'nickName')
    list_display = ('text',)
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-createTime',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段
    list_editable = []
    # fk_fields 设置显示外键字段
    # fk_fields = ()
    # 过滤器功能及能过滤的字段
    # list_filter = ('actualNickName',)
    # 搜索功能及能实现搜索的字段
    # search_fields = ('actualNickName', 'nickName', 'text')
    search_fields = ('text', 'actualNickName')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    # list_display = ('text', 'actualNickName', 'createTime', 'nickName')
    list_display = ('id', 'openId', 'actualNickName', 'chineseName', 'employmentNumber', 'cellPhoneNumber', 'joinTime')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-joinTime',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段
    list_editable = []
    # fk_fields 设置显示外键字段
    # fk_fields = ()
    # 过滤器功能及能过滤的字段
    # list_filter = ('actualNickName',)
    # 搜索功能及能实现搜索的字段
    # search_fields = ('actualNickName', 'nickName', 'text')
    search_fields = ('id', 'openId', 'actualNickName', 'chineseName', 'employmentNumber', 'cellPhoneNumber', 'joinTime')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    # list_display = ('text', 'actualNickName', 'createTime', 'nickName')
    list_display = ('id', 'text', 'addTime', 'msgId', 'userId')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-addTime',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段
    list_editable = []
    # fk_fields 设置显示外键字段
    # fk_fields = ()
    # 过滤器功能及能过滤的字段
    # list_filter = ('actualNickName',)
    # 搜索功能及能实现搜索的字段
    # search_fields = ('actualNickName', 'nickName', 'text')
    search_fields = ('id', 'text', 'addTime', 'msgId', 'userId')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    # list_display = ('text', 'actualNickName', 'createTime', 'nickName')
    list_display = ('id', 'text', 'addTime', 'msgId', 'userId')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-addTime',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段
    list_editable = []
    # fk_fields 设置显示外键字段
    # fk_fields = ()
    # 过滤器功能及能过滤的字段
    # list_filter = ('actualNickName',)
    # 搜索功能及能实现搜索的字段
    # search_fields = ('actualNickName', 'nickName', 'text')
    search_fields = ('id', 'text', 'addTime', 'msgId', 'userId')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    # list_display = ('text', 'actualNickName', 'createTime', 'nickName')
    list_display = ('id', 'imgUrl', 'addTime', 'msgId', 'userId')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-addTime',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段
    list_editable = []
    # fk_fields 设置显示外键字段
    # fk_fields = ()
    # 过滤器功能及能过滤的字段
    # list_filter = ('actualNickName',)
    # 搜索功能及能实现搜索的字段
    # search_fields = ('actualNickName', 'nickName', 'text')
    search_fields = ('id', 'imgUrl', 'addTime', 'msgId', 'userId')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.register(Msg)
admin.register(User)
admin.register(Note)
admin.register(Comment)
admin.register(Image)
