
//封装前端Ajax请求
request={
    post: function (route, json) {
        let xhr = new XMLHttpRequest();
        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                let newJson;
                console.log(this.responseText);
                try{
                    //newJson = JSON.parse(this.responseText);
                }catch{
                    warn.show({msg:"未知错误，请联系管理员",ms:3000})
                    return
                }
                /* if (newJson['callback']) {
                    for(let i=0;i<newJson['callback'].length;i++){
                        eval(newJson['callback'][i])(newJson);
                    }
                } */
                
            }
        });
        xhr.open("POST", "./api/" + route);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify(json));
    },
    get: function (route,callback) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText)
                if(callback){
                    callback(JSON.parse(this.responseText))
                }
                /* var newJson = JSON.parse(this.responseText);
                if (newJson['callback']) {
                    for(let i=0;i<newJson['callback'];i++){
                        newJson['callback'][i]();
                    }
                } */
            }
        });
        //xhr.open("GET", "./api/" + route);
        xhr.open("GET", route);
        xhr.send();
    },
}