//app.js

App({
  globalData: {
    openid: null,

  },
  onLaunch: function() {
    var that = this;
    wx.login({
      //获取code
      success: function(res) {
        var code = res.code; //返回code
        // console.log(code);
        var appId = 'wx749b2d174283a7c8';
        var secret = '8434f860137420779984cce8b7e7efbb';
        wx.request({
          url: 'https://api.weixin.qq.com/sns/jscode2session?appid=' + appId + '&secret=' + secret + '&js_code=' + code + '&grant_type=authorization_code',
          data: {},
          header: {
            'content-type': 'json'
          },
          success: function(res) {
            getApp().globalData.openid = res.data.openid //返回openid
            console.log(getApp().globalData.openid);
            wx.request({
              url: 'https://22465rj114.iask.in/notification_api/user_add',
              data: {
                openId: getApp().globalData.openid,
              },
            })
          }
        })
      }
    })
  }
})