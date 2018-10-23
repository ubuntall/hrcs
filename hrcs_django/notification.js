<script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
<script type="text/javascript">
    var i=0; //声明轮询次数变量
    temp=0;
    $.get('http://22465rj114.iask.in/notification_api/', function(data){
        temp=data["id"];
        console.log("in get temp=",temp);
        //console.log(temp);
    });

    $(document).ready(function(){
        c = window.setInterval("getResult()",3000); //间隔多少秒去触发ajax
    });
 
    function getResult(){
        jQuery.ajax({
            type:'get',
            url:'http://22465rj114.iask.in/notification_api/',
            dataType:'json',
            async: true,
            success:function(data){
                i++; //记录轮询的次数
                console.log("in ajax id=",data["id"]);
                //console.log(data["id"]);
                if(data["id"] != temp){ //处理自己的业务
                    temp=data["id"];
                    notification_pop();
                }
                //设置轮询了多少次停止轮询
                if(i>99999){
                    window.clearInterval(c); 
                }
            }
        });
    }

    function notification_pop(){
        var n = new Notification('新房源提醒',{
            body: '有新房源出现，点击查看',
            data: {
                url: 'http://22465rj114.iask.in/admin/msg2db/msg/',
            },
            icon: 'http://pics.sc.chinaz.com/Files/pic/icons128/5001/1.png',
            tag:"tag",
            renotify:true,
            silent:true,
            sticky:true,
        });

        n.onclick = function(){
            var url = window.location.href;
            console.log("url=",url);
            if (url=='http://22465rj114.iask.in/admin/msg2db/msg/'){
                window.location.reload();//重新载入当前窗户，以呈现新房源
            }else{
                console.log("n.data.url=",n.data.url);
                window.open(n.data.url);// 新窗口打开网址
            }
            n.close();// 关闭通知
        };
    }

    if(Notification.permission === 'granted'){
        console.log('用户允许通知');
    }else if(Notification.permission === 'denied'){
        console.log('用户拒绝通知');
    }else{
        console.log('用户还没选择，去向用户申请权限吧');
        Notification.requestPermission().then(function(permission) {
            if(permission === 'granted'){
                console.log('用户允许通知');
            }
            else if(permission === 'denied'){
                console.log('用户拒绝通知');
            }
        });
    };
</script>