//index.js
var WxSearch = require('../../wxSearchView/wxSearchView.js');

Page({
  data: {},


  // 搜索栏
  onLoad: function(e) {
    var that = this;
    WxSearch.init(
      that, // 本页面一个引用
      [], [],
      //['杭州', '嘉兴', "海宁", "桐乡", '宁波', '金华'], // 热点搜索推荐，[]表示不使用
      //['湖北', '湖南', '北京', "南京"],// 搜索匹配，[]表示不使用
      that.mySearchFunction, // 提供一个搜索回调函数
      that.myGobackFunction //提供一个返回回调函数
    );

    var json_array = [{
      "fields": {
        "text": "正在搜索数据..."
      }
    }, ];

    that.setData({
      msg_list: json_array
    })

    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/get_so/',
      data: {
        keyword: e.searchValue
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
                "text": "没有搜索到相关数据"
              }
            }, ],
            that.setData({
              msg_list: json_array
            })

        }

      },
      fail: function() {

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
    wx.redirectTo({
      url: '../search/search?searchValue=' + value
    })
  },

  // 返回回调函数
  myGobackFunction: function() {
    // do your job here
    // 跳转
    wx.redirectTo({
      url: '../index/index'
    })
  }



})