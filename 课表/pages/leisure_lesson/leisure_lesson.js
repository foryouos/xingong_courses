// pages/school_photo/school_photo.js
const DEFAULT_PAGE =3;
Page({
    /**
     * 页面的初始数据
     */
    startPageX: 2,
    currentView: DEFAULT_PAGE,

    data: {
    toView: `card_${DEFAULT_PAGE}`,
    vacant_class:null,
    today_week:null,
    members:['空闲教室查看,上下查看当天']
    },
    
    touchStart(e) {
    var that=this
    that.startPageX = e.changedTouches[0].pageX;
    },
    touchEnd(e) {
    var that=this
    const moveX = e.changedTouches[0].pageX - that.startPageX;
    const maxPage = 6;
    if (Math.abs(moveX) >= 150){
    if (moveX > 0) {
    that.currentView = that.currentView !== 0 ? that.currentView - 1 : 0;
    } else {
    that.currentView = that.currentView !== maxPage ? that.currentView + 1 : maxPage;
    }
    }
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that=this
        wx.cloud.init()
        wx.showNavigationBarLoading();
        wx.cloud.database().collection("vacant_class").get({
          success(res){
            var day_week={"1":"星期一","2":"星期二","3":"星期三","4":"星期四","5":"星期五","6":"星期六","7":"星期日",}
            // console.log("读取空闲教室名称成功.....",res.data[0]["vacant_class"])
            var week=day_week[new Date().getDay()]
            that.setData({
              vacant_class:res.data[0]["vacant_class"],
              today_week:week
            })
            wx.hideNavigationBarLoading();
          },
          fail(res){
            console.log("数据库API获取成功！",res)
          }
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
    },
    onShareTimeline() {}
})