Page({
 
    /**
     * 页面的初始数据
     */
    data: {
      imgUrls:null,
      indicatorDots: true, //是否显示面板指示点
      autoplay: true, //是否自动播放
      interval: 3000, //停留时间间隔
      duration: 1000, //播放时长
      previousMargin: '50px', //前边距，可用于露出前一项的一小部分，接受 px 和 rpx 值
      nextMargin: '50px', //后边距，可用于露出后一项的一小部分，接受 px 和 rpx 值
      circular: true, //是否采用衔接滑动
      currentSwiperIndex: 0, //swiper当前索引
    },
   
    swiperBindchange(e) {
      this.setData({
        currentSwiperIndex: e.detail.current
      })
    },
    return_main:function(event){
      wx.reLaunch({
        url: "../index/index",
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

    onLoad: function (options){
      var that=this
      wx.cloud.init()
      // 读取图片数据库，方便更新数据库
      wx.cloud.database().collection("picture_list").get({
      success(res){
      // console.log("读取图片数据库成功.....",res.data[0]['imgUrls'])
      that.setData({
            imgUrls:res.data[0]["imgUrls"]
      })
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