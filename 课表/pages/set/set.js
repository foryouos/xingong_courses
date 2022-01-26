// js
Page({
    data:{
        name:'',
        canIUseGetUserProfile: true,//显示登录按钮(wx:if 是遇 true 显示，hidden 是遇 false 显示。)
    },
    clean_data:function(event){
        wx.showModal({
          title:"提示",
          content:"确认清理？再次进入生效",
          success:function(res){
              if(res.confirm){
                //   console.log("确认")
                  wx.clearStorage()
                  wx.startPullDownRefresh()
                //   onPullDownRefresh
              } else{
                  console.log("取消")
              }
              wx.stopPullDownRefresh()
          }
        })
        // 
      },
onLoad(){
    wx.getStorage({//异步获取缓存
        key:"name",//本地缓存中指定的 key
        success:(res)=>{ 
          console.log('获取缓存成功',res.data)      
            this.setData({
                name:res.data, //将得到的缓存给key 
                 canIUseGetUserProfile: false,             
            }) 
            fail:(err)=>{
                console.log("获取失败",err);
            }                 
        }
    })//因为异步操作耗时，后显示这个。与下面的console.log("======")比较   
    try {//同步操作（按顺序显示），先显示这个。与下面的console.log("======")比较 
                var count= wx.getStorageSync('count', '')
                var mudiis = wx.getStorageSync('index')
                console.log('count',count);
                //注意 ：： wx.getStorageSync 和 wx.setStorageSync 是固定写法
            //这里将内存中的数据读取出来并且保存到一个新变量中
            
            //that是在外面重定义了this指向 代码： var that = this 
            //原因 ; 一些开发场景中 在success函数里面中this无法访问到外部的
            //data，除非使用箭头函数就不用重新定义this指向问题
            //原因 ：： ES6中新增的箭头函数并没有自身的this
            that.setData({
                index : mudiis 
                // 将数据热更新到data数据中
              })
              console.log(this.data.mudi_is)
              //输出是否有数据
               } catch (e) { }
            console.log('======');
   
},

 
    getUserProfile(e){//获取用户信息绑定的单击事件
        wx.getUserProfile({//获取用户信息
          desc: '用于完善会员资料',// 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
           success:(res)=>{
            console.log("---",res);    
            this.setData({
              name:res.userInfo
            })
            wx.setStorage({
                key:'name',//本地缓存中指定的 key(类型：string)
                data:res.userInfo,//需要存储的内容。只支持原生类型、Date、及能够通过JSON.stringify序列化的对象(类型:any)
                success:(s)=>{
                    console.log('存储缓存成功====',s);
                    this.setData({
                         canIUseGetUserProfile: false  //隐藏登录按钮  
                    })
                },
                fail:(f)=>{
                    console.log('存储缓存失败====',f);                    
                }
            })
        }
        })
}
})