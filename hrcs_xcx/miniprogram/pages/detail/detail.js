//index.js
const app = getApp()

// 1 导入js文件
var WxSearch = require('../../wxSearchView/wxSearchView.js');

Page({

  data: {
    url: 'https://22465rj114.iask.in/notification_api/get_item_by_id',
    searchValue: '',
  },

  onLoad: function(options) {

    var that = this;
    var json_array = [{
      "fields": {
        "text": "正在载入数据..."
      }
    }, ];

    that.setData({
      msg_list: json_array
    })

    var id_temp = 0
    var msg_list = []
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/get_item_by_id',
      data: {
        id: options.id
      },
      method: 'get',
      success: function(res) {
        json_array = JSON.parse(res.data)
        console.log(json_array)
        id_temp = json_array[0].pk
        //console.log(id_temp)
        var date = new Date(json_array[0].fields.createTime)
        date = date.toLocaleString()
        json_array[0].fields.createTime = date
        console.log(json_array[0].fields.createTime)
        console.log(json_array[0].fields.text)
        that.setData({
          msg_list: json_array
        })

      },
      fail: function() {
        json_array = [{
          "fields": {
            "text": "网络出小差了...点击右上角返回按键刷新"
          }
        }, ];

        that.setData({
          msg_list: json_array
        })

      },
      complete: function() {

      }
    })
  },

  onShow: function(options) {
    // 2 搜索栏初始化
    var that = this;
    WxSearch.init(
      that, // 本页面一个引用
      [], // 热点搜索推荐，[]表示不使用
      [], // 搜索匹配，[]表示不使用
      that.mySearchFunction, // 提供一个搜索回调函数
      that.myGobackFunction //提供一个返回回调函数
    );
  },


  // 3 转发函数，固定部分，直接拷贝即可
  wxSearchInput: WxSearch.wxSearchInput, // 输入变化时的操作
  wxSearchKeyTap: WxSearch.wxSearchKeyTap, // 点击提示或者关键字、历史记录时的操作
  wxSearchDeleteAll: WxSearch.wxSearchDeleteAll, // 删除所有的历史记录
  wxSearchConfirm: WxSearch.wxSearchConfirm, // 搜索函数
  wxSearchClear: WxSearch.wxSearchClear, // 清空函数

  // 4 搜索回调函数  
  mySearchFunction: function(value) {
    // do your job here
    // 示例：跳转
    wx.navigateTo({
      url: '../search/search?searchValue=' + value
    })
  },

  // 5 返回回调函数
  myGobackFunction: function() {
    // do your job here
    // 示例：返回
    wx.navigateBack({

    })
  },

  // click: function(e) {
  //   console.log(e.currentTarget.dataset)

  // },

  dailing: function(e) {
    console.log(e.currentTarget.dataset.text)
    var tel_array = e.currentTarget.dataset.text.replace(/\s*/g, "").match(/(1[3456789]\d{9})/g);
    // tel_array = Array.from(new Set(tel_array));
    // if (tel_array.length > 1) {
    //   tel_array = tel_array.slice(0, 1);
    // }
    // console.log(tel_array)
    if (tel_array != null) {
      var tel = tel_array[0]
      wx.makePhoneCall({
        phoneNumber: tel,
      })
    } else {
      wx.showToast({
        title: '未找到手机号码',
      })
    }

  },

  longPress: function(e) {
    console.log(e.currentTarget.dataset.text)
    wx.setClipboardData({
      data: e.currentTarget.dataset.text,
    })
  },

  addToNode: function(e) {
    var openid = getApp().globalData.openid
    var msgid = e.currentTarget.dataset.text
    // console.log(msgid)
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/note_add',
      data: {
        openId: openid,
        msgId: msgid,
      },
      success: function(res) {
        wx.showToast({
          title: '笔记添加成功',
        })
      },
      fail: function() {
        wx.showToast({
          title: '添加失败已存在',
        })
      }
    })
  },

  deleteFromNote: function(e) {
    wx.showToast({
      title: '笔记删除成功',
    })

  }


});