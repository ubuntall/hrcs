//index.js
const app = getApp()

Page({

  data: {
    url: 'https://22465rj114.iask.in/notification_api/get_five/',
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
      url: 'https://22465rj114.iask.in/notification_api/get_five/',
      method: 'get',
      success: function(res) {
        console.log(res.data)
        id_temp = res.data[0]["pk"]
        msg_list = res.data
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
        url: 'https://22465rj114.iask.in/notification_api/get_five/',
        method: 'get',
        success: function(res) {
          id = res.data[0]["pk"]
          if (id > id_temp) {
            console.log(res.data)
            id_temp = id
            msg_list = res.data
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