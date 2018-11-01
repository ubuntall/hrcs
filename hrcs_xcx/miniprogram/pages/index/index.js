//index.js
const app = getApp()

// 1 导入js文件
var WxSearch = require('../../wxSearchView/wxSearchView.js');

Page({

  data: {
    url: 'https://22465rj114.iask.in/notification_api/get_five/',
    searchValue:'',
  },

  onLoad: function(options) {

    var that = this;

    var id_temp = 0
    var msg_list = []
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/get_five/',
      method: 'get',
      success: function(res) {
        var json_array = JSON.parse(res.data)
        console.log(json_array)
        id_temp = json_array[0].pk
        console.log(id_temp)
        that.setData({
          msg_list: json_array
        })
      },
      fail: function() {

      },
      complete: function() {

      }
    })

    // 2 搜索栏初始化
    WxSearch.init(
      that,  // 本页面一个引用
      [],
      [],
      //['松涛龙高', '发展大厦', "桃源小区", "龙城春天", '实验二小', '松涛分校', '龙盛花园', '尚品至尊'], // 热点搜索推荐，[]表示不使用
      //['实小龙初', '水韵华都', '附小七中', "一中分校"],// 搜索匹配，[]表示不使用
      that.mySearchFunction, // 提供一个搜索回调函数
      that.myGobackFunction //提供一个返回回调函数
    );

    var id = 0
    var timer = setInterval(function() {
      wx.request({
        url: 'https://22465rj114.iask.in/notification_api/get_five/',
        method: 'get',
        success: function(res) {
          var json_array = JSON.parse(res.data)
          id = json_array[0].pk
          if (id > id_temp) {
            console.log(json_array)
            id_temp = id
            that.setData({
              msg_list: json_array
            })
            // wx.playBackgroundAudio({
            //   dataUrl: 'http://m3.13400.com:9888/v2013/smso.mp3',
            // })

          }

        },
        fail: function() {

        },
        complete: function() {

        }
      })
    }, 1000 * 60)
  },

  // 3 转发函数，固定部分，直接拷贝即可
  wxSearchInput: WxSearch.wxSearchInput,  // 输入变化时的操作
  wxSearchKeyTap: WxSearch.wxSearchKeyTap,  // 点击提示或者关键字、历史记录时的操作
  wxSearchDeleteAll: WxSearch.wxSearchDeleteAll, // 删除所有的历史记录
  wxSearchConfirm: WxSearch.wxSearchConfirm,  // 搜索函数
  wxSearchClear: WxSearch.wxSearchClear,  // 清空函数

  // 4 搜索回调函数  
  mySearchFunction: function (value) {
    // do your job here
    // 示例：跳转
    wx.redirectTo({
      url: '../search/search?searchValue=' + value
    })
  },

  // 5 返回回调函数
  myGobackFunction: function () {
    // do your job here
    // 示例：返回
    wx.redirectTo({
      url: '../index/index'
    })
  }

});