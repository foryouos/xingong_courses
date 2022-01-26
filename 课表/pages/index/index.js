// pages/course/course.js
Page({
  data:{
    members:['这里是新乡工程学院课程表']
  },
  onTapJump:function(event){
    wx.redirectTo({
      url: "../classroom/classroom",
      success:function(){
        console.log("jump success")
      },
      fail:function(){
        console.log("jump failed")
      },
      complete:function(){
        console.log("jump complete")
      }
    });
  },
  onTapJump_tab:function(event){
    wx.reLaunch({
      url: "../course_schedule/course_schedule",
      success:function(){
        console.log("jump success")
      },
      fail:function(){
        console.log("jump failed")
      },
      complete:function(){
        console.log("jump complete")
      }
    });
  },
  onTapJump_vacant:function(event){
    wx.reLaunch({
      url: "../leisure_lesson/leisure_lesson",
      success:function(){
        console.log("jump success")
      },
      fail:function(){
        console.log("jump failed")
      },
      complete:function(){
        console.log("jump complete")
      }
    });
  },
  onTapJump_photo:function(event){
    wx.reLaunch({
      url: "../school_photo/school_photo",
      success:function(){
        console.log("jump success")
      },
      fail:function(){
        console.log("jump failed")
      },
      complete:function(){
        console.log("jump complete")
      }
    });
  
},

onLoad: function (options) {
  var that=this
  var day_week={"1":"星期一","2":"星期二","3":"星期三","4":"星期四","5":"星期五","6":"星期六","7":"星期日",}
  var week="今天是"+day_week[new Date().getDay()]
  // console.log("读取星期....",that.data["members"])
  that.setData({
    members:that.data["members"].concat(week),
  })
  var url = "https://devapi.qweather.com/v7/weather/now?"
  var city="113.90,35.20"
  var params = {
      location: city,
      key: "592d4160e98742dab6cf5a326b7d546e"
    }
    wx.request({
      url: url,
      data: params,
      success: function (res) {
        // console.log("新工实时天气:",res.data.now.text,res.data.now.temp+"度",res.data.now.windDir)
        var weather="新工此时天气为:"+res.data.now.text+res.data.now.temp+"度"+res.data.now.windDir
        that.setData({
          members:that.data["members"].concat(weather),
        })
      },
      fail: function (res) {
       },
      complete: function (res) { 
      },
    })
    wx.request({
      url: "https://devapi.qweather.com/v7/air/now?",
      data: params,
      success: function (res) {
        var air="新工空气质量指数为:"+res.data.now.aqi+"pm2.5为"+res.data.now.pm2p5
        var air_condition="空气质量:"+res.data.now.category
        that.setData({
          members:that.data["members"].concat(air).concat(air_condition),
          
        })
      },
      fail: function (res) {
       },
      complete: function (res) { 
      },
    })
},
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
    ,
    onShareTimeline() {}
})