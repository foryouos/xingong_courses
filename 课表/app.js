// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    var start_index=wx.getStorageSync('index')
    if(!start_index){undefined  //判断内部缓存是否为空值，若为空值，则上传，若不是空值，则不上传
      wx.setStorage({//初始化缓存，将信管193班作为第一缓存
        key:"index",
        data:"263"
    })
    console.log("为空值")
    }
    else console.log("本地内容有缓存")
    

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
  },
  globalData: {
    userInfo: null
  }
})
