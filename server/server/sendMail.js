const nodemailer = require("nodemailer");
sendMail = {
    count:0,
    countTimer:function(){
        //每分钟减少一个计数
        if(--sendMail.count){
            setTimeout(sendMail.countTimer,60000);
        }
        console.log(sendMail.count);
    },
    send: async function (req, res) {
        mymail="xxxx@xxx.com";//邮箱
        mymailkey='xxxxxxxxxxx';//IMAP/SMTP服务授权码

        
        //访问限流
        //本来是想做一个公共的后端给大家一起不用配置邮箱玩的，但是后面觉得如果公然暴露自己的服务器地址和使用自己的私人邮箱不安全，就取消了
        if(sendMail.count>4){
            return res.json({code:1,msg:"服务器接受的请求太多了！请稍后重试"});
        }
        if(sendMail.count==0){
            setTimeout(sendMail.countTimer,60000);
        }
        sendMail.count++;
        console.log(sendMail.count);
        console.log(req.query);
        if(!req.query.code||!req.query.mail){
            return res.json({code:1,msg:"参数错误"});
        }
        let transporter = nodemailer.createTransport({
            service: 'qq', //使用的邮箱服务，这里qq为例
            port: 465, //邮箱服务端口号
            secure: true, // true for 465, false for other ports
            auth: {
                user: mymail, //  邮箱地址
                pass: mymailkey, //授权码
            },
        });

        // send mail with defined transport object
        transporter.sendMail({
            from: '"检鼠"<'+mymail+'>', // 你的邮箱
            to: req.query.mail, //发送的邮箱列表
            subject: '验证码', // 主题
            html: `<div>你的验证码是${req.query.code}</div>`
        }).then(myres => {
            console.log(myres)
            return res.json({code:0});
        });
    }
}