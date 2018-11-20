//index.js
var WxSearch = require('../../wxSearchView/wxSearchView.js');

Page({
  data: {},

  // 搜索栏
  onLoad: function(e) {
    var that = this;
    var json_array = [];

    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/get_so/',
      data: {
        keyword: e.searchValue
      },
      method: 'get',
      success: function(res) {
        json_array = JSON.parse(res.data).reverse()
        console.log(json_array)
        if (json_array.length > 0) {
          that.setData({
            msg_list: json_array
          })
        } else if (json_array.length == 0) {
          wx.showToast({
            title: '没有相关数据',
          })

        }

      },
      fail: function() {
        json_array = [{
          "fields": {
            "text": "网络出小差了...请重新搜索"
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
    var that = this;
    // 2 搜索栏初始化
    WxSearch.init(
      that, // 本页面一个引用
      [], // 热点搜索推荐，[]表示不使用
      [], // 搜索匹配，[]表示不使用
      that.mySearchFunction, // 提供一个搜索回调函数
      that.myGobackFunction //提供一个返回回调函数
    );

  },


  // 转发函数,固定部分
  wxSearchInput: WxSearch.wxSearchInput, // 输入变化时的操作
  wxSearchKeyTap: WxSearch.wxSearchKeyTap, // 点击提示或者关键字、历史记录时的操作
  wxSearchDeleteAll: WxSearch.wxSearchDeleteAll, // 删除所有的历史记录
  wxSearchConfirm: WxSearch.wxSearchConfirm, // 搜索函数
  wxSearchClear: WxSearch.wxSearchClear, // 清空函数

  // 搜索回调函数  
  mySearchFunction: function(value) {
    // do your job here
    // 跳转
    wx.navigateTo({
      url: '../search/search?searchValue=' + value
    })
  },

  // 返回回调函数
  myGobackFunction: function() {
    // do your job here
    // 跳转
    wx.navigateBack({

    })
  },

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

  addToNode: function (e) {
    var openid = getApp().globalData.openid
    var msgid = e.currentTarget.dataset.text
    // console.log(msgid)
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/note_add',
      data: {
        openId: openid,
        msgId: msgid,
      },
      success: function (res) {
        wx.showToast({
          title: '笔记添加成功',
        })
      },
      fail: function () {
        wx.showToast({
          title: '添加失败已存在',
        })
      }
    })
  },
})