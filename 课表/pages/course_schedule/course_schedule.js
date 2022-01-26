// pages/leisure_lesson/leisure_lesson.js
//云数据库初始化
Page({

    /**
     * 页面的初始数据
     */
    data: {
        name_num:34,
        lesson_name_list:null,
        fruitTypeList: 
        [
          {
            "fruitTypeId": 1,
            "typeName": "上午一"
          },
          {
            "fruitTypeId": 2,
            "typeName": "上午二"
          },
          {
            "fruitTypeId": 3,
            "typeName": "下午一"
          },
          {
            "fruitTypeId": 4,
            "typeName": "下午二"
          },
          {
            "fruitTypeId": 5,
            "typeName": "晚自习"
          },
          
        ],
        fruitList: null,
        // 课程选取列表，数组
        lesson_all: null,
      },
      bindPickerChange: function (e) {
        var that=this
        wx.cloud.init()
        console.log('picker发送选择改变，携带值为', e.detail.value)
        var name_key=Object.keys(that.data["lesson_all"][e.detail.value])[0]
        // console.log("返回的lesson值",that.data["lesson_all"])
        // console.log("返回的key值",name_key)
        this.setData({
          name_num: e.detail.value,
          fruitList: that.data["lesson_all"][e.detail.value][name_key],
        })
        wx.setNavigationBarTitle({
          title: name_key
      })
      },
    
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options){
      var that=this
        wx.cloud.init()
        wx.showNavigationBarLoading();
        wx.cloud.database().collection("course_name_list").get({
          success(res){
            // console.log("读取课程名称成功.....",res.data[0]["lesson"])
            that.setData({
              lesson_name_list:res.data[0]["lesson"]
            })
          },
          fail(res){
            console.log("数据库API获取成功！",res)
          }
        })
        // 将总文件保存到内容里面
        wx.cloud.database().collection("course_schedule01").get({
          success(res){
            // console.log("读取具体01内容成功......",res.data)
            that.setData({
              lesson_all: res.data[0]["json_lesson_list"],
            })
            console.log("读取本地内容01成功......")
          },
          fail(res){
            console.log("数据库API01获取成功！",res)
          }
        })
        wx.cloud.database().collection("course_schedule02").get({
          success(res){
            
            that.setData({
              lesson_all: that.data["lesson_all"].concat( res.data[0]["json_lesson_list"]),
              fruitList: that.data["lesson_all"][4]["会计学原理"]
            })
            console.log("读取02文件内容成功,并传递成功")
            wx.hideNavigationBarLoading();
          },
          fail(res){
            console.log("数据库API01获取成功！",res)
            
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

    }
    ,
    onShareTimeline() {}
})