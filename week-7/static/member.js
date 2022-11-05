function handleClick() {
    let username = document.getElementById("username");
    let entry = {
        username: username.value
    };

    fetch("/api/member", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        }
    })
        .then(function (response) {
            response.json().then(function (data) {
                document.getElementById("apiMember").innerHTML = data.data.name + "(" + data.data.username + ")";
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
            response.json().then(function (data) {
                document.getElementById("apiMember2").innerHTML = data.ok;
            })
        })


}