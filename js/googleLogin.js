function handleCredentialResponse(googleUser) {
    console.log(googleUser)
    console.log(googleUser.credential)

    var token = googleUser.credential;  //在请求头中获取token
    let strings = token.split("."); //截取token，获取载体
    var userinfo = JSON.parse(decodeURIComponent(escape(window.atob(strings[1].replace(/-/g, "+").replace(/_/g, "/"))))); //解析，需要吧‘_’,'-'进行转换否则会无法解析
    console.log(userinfo);
    document.getElementById("dmoejson").innerHTML = userinfo.name + ", " + userinfo.email;
    // if (userinfo.email_verified == true) {
    //     location = "complete.html"
    // }

    // var data = decodeJWT.googleUser.credential;
    // JSON.parse(data);
    // console.log(data);
}




// function handleCredentialResponse(googleUser) {
//     console.log(googleUser)
//     console.log(googleUser.credential)

//     var token = googleUser.credential;  //在请求头中获取token
//     let strings = token.split("."); //截取token，获取载体
//     var userinfo = JSON.parse(decodeURIComponent(escape(window.atob(strings[1].replace(/-/g, "+").replace(/_/g, "/"))))); //解析，需要吧‘_’,'-'进行转换否则会无法解析
//     console.log(userinfo);
//     document.getElementById("dmoejson").innerHTML = userinfo.name + ", " + userinfo.email;

//     var data = decodeJWT.googleUser.credential;
//     JSON.parse(data);
//     console.log(data);
// }