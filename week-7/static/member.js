function handleClick() {
    const username = document.getElementById("username").value;
    fetch("http://127.0.0.1:3000/api/member?username=" + username)
        .then(function (response) {
            response.json()
                .then(function (data) {
                    if (data.data !== null) {
                        document.getElementById("apiMember").innerHTML = data.data.name + "(" + data.data.username + ")";
                    }
                    if (data.data === null) {
                        document.getElementById("apiMember").innerHTML = "無此會員";
                    }
                })
        })
}


function handleClick2() {
    let name = document.getElementById("name");
    let entry2 = {
        name: name.value
    };

    fetch("/api/member", {
        method: "PATCH",
        credentials: "include",
        body: JSON.stringify(entry2),
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        }
    })
        .then(function (response) {
            response.json()
                .then(function (data) {
                    if (data.ok == true) {    //null大小寫有差
                        document.getElementById("apiMember2").innerHTML = "更新成功";
                    }
                    if (data.ok !== true) {
                        document.getElementById("apiMember2").innerHTML = "更新失敗";
                    }
                })
        })
}