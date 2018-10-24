Page({
  data: {
    url: 'https://22465rj114.iask.in/notification_api/'
  },
  onLoad: function(options) {
    var that=this;
    // options.url ? this.setData({
    //   url: options.url
    // }) : wx.navigateBack({
    //   delta: 2
    // });
    
    wx.request({
      url: 'https://22465rj114.iask.in/notification_api/',
      method: 'get',
      success: function(res) {
        console.log(res)
        that.setData({ 
          data:res.data,
        })
      },
      fail: function() {

      },
      complete: function() {

      }
    })

    var timer=setInterval(function(){
      wx.request({
        url: 'https://22465rj114.iask.in/notification_api/',
        method: 'get',
        success: function (res) {
          console.log(res)
          that.setData({
            data: res.data,
          })
        },
        fail: function () {

        },
        complete: function () {

        }
      })
    }
      ,3000)
  },
});