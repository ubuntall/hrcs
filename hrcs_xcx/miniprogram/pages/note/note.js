//index.js
var WxSearch = require('../../wxSearchView/wxSearchView.js');

Page({
  data: {},


  // 搜索栏
  onLoad: function(e) {
    var that = this;
    var json_array = [{
      "fields": {
        "text": "正在查找笔记..."
      }
    }, ];

    that.setData({
      msg_list: json_array
    })

    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/notes_getall/',
      data: {
        openId: getApp().globalData.openid,
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
          json_array = [{
              "fields": {
                "text": "还没有笔记..."
              }
            }, ],
            that.setData({
              msg_list: json_array
            })

        }

      },
      fail: function() {
        json_array = [{
          "fields": {
            "text": "网络出小差了..."
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

    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/notes_getall/',
      data: {
        openId: getApp().globalData.openid,
      },
      method: 'get',
      success: function(res) {
        var json_array = JSON.parse(res.data).reverse()
        console.log(json_array)
        if (json_array.length > 0) {
          that.setData({
            msg_list: json_array
          })
        } else if (json_array.length == 0) {
          json_array = [{
              "fields": {
                "text": "还没有笔记..."
              }
            }, ],
            that.setData({
              msg_list: json_array
            })

        }

      },
      fail: function() {
        json_array = [{
          "fields": {
            "text": "网络出小差了..."
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
    wx.switchTab({
      url: '../index/index',
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

  deleteFromNote: function(e) {
    console.log(e.currentTarget.dataset.text)
    var nodeid = e.currentTarget.dataset.text
    var that = this;
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/note_delete',
      data: {
        noteId: nodeid,
        openId: getApp().globalData.openid,
      },
      success: function(e) {

        wx.request({
          url: 'https://22465rj114.iask.in/notification_api/notes_getall/',
          data: {
            openId: getApp().globalData.openid,
          },
          method: 'get',
          success: function(res) {
            var json_array = JSON.parse(res.data).reverse()
            console.log(json_array)
            if (json_array.length > 0) {
              that.setData({
                msg_list: json_array
              })
            } else if (json_array.length == 0) {
              json_array = [{
                "fields": {
                  "text": "还没有笔记..."
                }
              }, ];
              that.setData({
                msg_list: json_array
              })
            }
          },
          fail: function() {
            json_array = [{
              "fields": {
                "text": "网络出小差了..."
              }
            }, ];

            that.setData({
              msg_list: json_array
            })

          },
          complete: function() {
            wx.showToast({
              title: '笔记删除成功',
            })

          }
        })
      }
    })
  }
})