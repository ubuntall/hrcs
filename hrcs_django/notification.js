<script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
<script type="text/javascript">
    var i=0; //声明轮询次数变量
    temp=0
    $.get('http://127.0.0.1:8000/notification_api/', function(data){
        temp=data["id"]
        console.log(temp);
    });

    $(document).ready(function(){
        c = window.setInterval("getResult()",5000); //间隔多少秒去触发ajax
    });
 
    function getResult(){
        jQuery.ajax({
            type:'get',
            url:'http://127.0.0.1:8000/notification_api/',
            dataType:'json',
            async: true,
            success:function(data){
                i++; //记录轮询的次数
                if(data["id"] !== temp){ //处理自己的业务
                    temp=data["id"]
                    notification_pop()
                }
                //设置轮询了多少次停止轮询
                if(i>99999){
                    window.clearInterval(c); 
                }
            }
        });
    }



    function notification_pop(){
        if(Notification.permission === 'granted'){
            console.log('用户允许通知');
        }else if(Notification.permission === 'denied'){
            console.log('用户拒绝通知');
        }else{
            console.log('用户还没选择，去向用户申请权限吧');
            Notification.requestPermission().then(function(permission) {
                if(permission === 'granted'){
                    console.log('用户允许通知');
                    var n = new Notification('新房源提醒',{
                        body: '有新房源出现，点击查看',
                        data: {
                            url: 'http://127.0.0.1:8000/admin/msg2db/msg/'
                        }
                    })
                    n.onclick = function(){
                        window.location.href(n.data.url, 'http://127.0.0.1:8000/admin/msg2db/msg/');      // 打开网址
                        n.close();                              // 并且关闭通知
                    }
                }else if(permission === 'denied'){
                    console.log('用户拒绝通知');
                }
            });
        }
        i++;
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
        })
    }

</script>