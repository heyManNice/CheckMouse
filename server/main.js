//加载基础初始化服务
require('./server/init.js');
dirnameMain = __dirname;

//加载第三方模块
const WebSocket = require('ws')
const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');  
const app = express();
var myws

//服务器运行端口
const port = 8084;

//parser
app.use(bodyParser.json());
app.use(cookieParser());  

app.all('*', function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    res.header('Access-Control-Allow-Methods', '*');
    /* res.header('Content-Type', 'application/json;charset=utf-8'); */
    next();
  });

//加载服务组件
loadServer('pageRoute');
loadServer('sendMail');

//静态文件
app.use(express.static('public'));

//网页路由
app.get('/test',pageRoute.test);
app.get('/scan',async function(req, res){
    if(myws){
        myws.send("havescan");
    }
    print("有人扫码啦")
    return res.sendFile(dirnameMain+'/scan.html')
})

//API路由
app.get('/api/sendMail',sendMail.send);
app.get('/api/login',async function(req, res){
    print("有人按了登录")
    if(myws){
        myws.send("havelogin");
    }
    return res.send("ok");
});



const wss =new WebSocket.Server({
    port:3600
})

wss.on('connection',function(ws){
    ws.on('message',async function(message){
        message=message.toString();
        /* console.log(message);
        console.log(wss); */
        myws = ws;
        myws.send("hello");
    })
    ws.on('close',async function(){
        
    });
})


//启动成功提示
app.listen(port, () => {
    print(`系统已运行在 ${port}`)
})

//sendMail.send()