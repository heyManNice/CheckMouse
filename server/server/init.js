//日志打印功能
print = function(msg,type){
    let temp = new Date();
    let H = temp.getHours();
    let M = temp.getMinutes();
    let S = temp.getSeconds();
    let fmsg = `[${temp.getFullYear()}-${temp.getMonth()+1}-${temp.getDate()} ${H<10?"0"+H:H}:${M<10?"0"+M:M}:${S<10?"0"+S:S}] ${msg}`;
    switch(type){
        case 'err':
            console.error(fmsg);
            break;
        default:
            console.log(fmsg);
    }
}
//加载组件功能
loadServer=function(name) {
    try {
        if ( typeof eval(name) != undefined) {
            print(name + "服务冲突",'err');
            return 1
        }
    } catch {
        require('./' + name + '.js')
        print(name + "服务已加载");
    }
}