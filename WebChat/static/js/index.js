window.onload = function (ev) {

    document.getElementById("send").onclick = function (ev2) {
        xmlHttp = new XMLHttpRequest();
        var content = document.getElementById("input_info").value;
        if (content.length < 1) {
            alert("请输入字符后发送");
            return;
        } else if (content.length > 200) {
            alert("每次发送不可以超出200个字符哈~");
            return;
        }
        xmlHttp.open("GET", "/send_and_save?my_text=" + content, true)
        xmlHttp.onreadystatechange = function () {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            }
        }
        xmlHttp.send();
        document.getElementById("input_info").value = "";
    }

}


old_info = 0;

function updata_info() {
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "/get?old_info=" + old_info, true)
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            a = JSON.parse(xmlHttp.responseText).dataa
            if (parseInt(old_info) == parseInt(JSON.parse(a).old_info)) {
                return;
            }
            old_info = parseInt(JSON.parse(a).old_info)
            content = JSON.parse(a).info;
            for (var i = 0; i < content.length; i++) {
                if (content[i].user_name == document.getElementById("user_id")) {


                    var div1 = document.createElement("div");
                    var div2 = document.createElement("div");
                    var div3 = document.createElement("div");
                    var span1 = document.createElement("span");
                    var span2 = document.createElement("span");
                    span1.innerHTML = content[i].user_name
                    span2.innerHTML = content[i].chat_content
                    div2.appendChild(span1)
                    div3.appendChild(span2)
                    div1.appendChild(div2)
                    div1.appendChild(div3)
                    document.getElementById("content").appendChild(div1)


                } else {
                    {
                        var div1 = document.createElement("div");
                        var div2 = document.createElement("div");
                        var div3 = document.createElement("div");
                        var span1 = document.createElement("span");
                        var span2 = document.createElement("span");
                        span1.innerHTML = content[i].user_name
                        span2.innerHTML = content[i].chat_content
                        div2.appendChild(span1)
                        div3.appendChild(span2)
                        div1.appendChild(div2)
                        div1.appendChild(div3)
                        document.getElementById("content").appendChild(div1)
                    }
                }
            }
        }
    }
    xmlHttp.send();
}

updata_info();
setInterval(updata_info, 1000);

