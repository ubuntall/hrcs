//index.js
const app = getApp()

Page({

  data: {
    url: 'https://22465rj114.iask.in/notification_api/',
  },

  onLoad: function(options) {
    var that = this;
    // options.url ? this.setData({
    //   url: options.url
    // }) : wx.navigateBack({
    //   delta: 2
    // });

    var id_temp = 0
    var msg_list = []
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/',
      method: 'get',
      success: function(res) {
        console.log(res.data)
        id_temp = res.data.id
        msg_list.push(res.data)
        that.setData({
          msg_list: msg_list
        })
      },
      fail: function() {

      },
      complete: function() {

      }
    })

    var id = 0
    var timer = setInterval(function() {
      wx.request({
        url: 'https://22465rj114.iask.in/notification_api/',
        method: 'get',
        success: function(res) {
          id = res.data.id
          if (id > id_temp) {
            console.log(res.data)
            id_temp = id
            msg_list.unshift(res.data)
            that.setData({
              msg_list: msg_list
            })

          }

        },
        fail: function() {

        },
        complete: function() {

        }
      })
    }, 1000 * 5)
  },
  
});