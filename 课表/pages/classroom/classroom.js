// pages/leisure_lesson/leisure_lesson.js
//云数据库初始化
Page({

    /**
     * 页面的初始数据
     */
    data: {
        name_num:60,
        class_name_list:null,
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
        classroom_all:null
        // 课程选取列表，数组
      },
      bindPickerChange: function (e) {
        var that=this
        console.log('picker发送选择改变，携带值为', e.detail.value)
        var name_key=Object.keys(that.data["classroom_all"][e.detail.value])[0]
        // console.log("返回的lesson值",that.data["lesson_all"])
        // console.log("返回的key值",name_key)
        that.setData({
          name_num: e.detail.value,
          fruitList: that.data["classroom_all"][e.detail.value][name_key],
        })
        wx.setNavigationBarTitle({
          title: name_key
      })
      // console.log("返回的num值",that.data["name_num"])
      },
    
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options){
      var that=this
        wx.cloud.init()
        wx.showNavigationBarLoading();
        wx.cloud.database().collection("classroom_list").get({
          success(res){
            // console.log("读取教室名称成功.....",res.data[0]["lesson"])
            that.setData({
              class_name_list:res.data[0]["lesson"]
            })
          },
          fail(res){
            console.log("数据库API获取成功！",res)
          }
        })
        // 将总文件保存到内容里面
        wx.cloud.database().collection("classroom_lesson").get({
          success(res){
            var name_start=Object.keys(res.data[0]["json_class_list"][that.data["name_num"]])[0]
            that.setData({
              classroom_all:res.data[0]["json_class_list"],
              fruitList: res.data[0]["json_class_list"][that.data["name_num"]][name_start]
            })
            wx.setNavigationBarTitle({
              title: name_start
          })
            // console.log("读取教室内容成功,",res.data[0]["json_class_list"])
            // console.log("设置的初始值"+that.data["name_num"])
            // console.log("设置的关键字"+name_start)
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

    
    },
    onShareTimeline() {}
})