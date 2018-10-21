from django.contrib import admin

# Register your models here.
from .models import Msg


@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('createTime', 'actualNickName', 'nickName', 'text')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
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
    #list_filter = ('actualNickName', 'nickName')
    # 搜索功能及能实现搜索的字段
    search_fields = ('actualNickName', 'nickName', 'text')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.register(Msg)
