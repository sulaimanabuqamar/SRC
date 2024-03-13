var navbartoggle = document.getElementById("navbartoggle");
function toggleNavbar(visible) {
    console.log(visible)
    if(visible) {
        document.getElementsByClassName("subnavbar")[0].style.animation = "showNavbar 1s ease-in-out forwards";
    }
    else {
        document.getElementsByClassName("subnavbar")[0].style.animation = "hideNavbar 1s ease-in-out forwards";
    }
}
html2canvas(document.querySelector("#bg")).then(canvas => {
    // document.body.appendChild(canvas)
    var bounds = document.getElementsByClassName("mask")[0].getBoundingClientRect();
    var tempCanvas = document.createElement("canvas"),
        tCtx = tempCanvas.getContext("2d");
    tempCanvas.width = 100;
    // tempCanvas.width = document.getElementsByClassName("mask")[0].clientWidth;
    // tempCanvas.height = document.getElementsByClassName("mask")[0].clientHeight;
    tempCanvas.height = 100;
    console.log(document.getElementsByClassName("mask")[0].offsetLeft);
    tCtx.drawImage(canvas, bounds.x, bounds.y, bounds.width + 20, bounds.height, 0, 0, bounds.width + 20, bounds.height);
    // tCtx.drawImage(canvas, bounds.x, bounds.y, bounds.width,bounds.height, 0,0,bounds.width,bounds.height);
    // tCtx.drawImage(canvas, bounds.x+20, bounds.y+20, bounds.width,bounds.height, 0,0,bounds.width,bounds.height);
    // tCtx.drawImage(canvas, 0, 0, document.getElementsByClassName("mask")[0].clientWidth, document.getElementsByClassName("mask")[0].clientHeight, 0,0,100,100);
    document.getElementsByClassName("mask")[0].style.backgroundImage = "url(" + tempCanvas.toDataURL() + ")";
    // document.body.appendChild(tempCanvas);
    document.getElementsByClassName("subnavbar")[0].style.display = "flex";
});
function openLoginPage() {
    if (document.getElementsByClassName("subnavbar")[0].style.height == "400px") {
        document.getElementById("navbartoggle").children[0].onclick = function() {this.parentElement.children[1].click();};
        document.getElementsByClassName("subnavbar")[0].style.height = "50px";
        document.getElementsByClassName("subnavbar")[0].style.display = "flex";
        document.getElementsByClassName("navbarlinks")[0].style.display = "block";
        document.getElementsByClassName("navbarlinks")[1].style.display = "block";
        document.getElementsByClassName("navbarlinks")[2].style.display = "block";
        document.getElementsByClassName("navbarlinks")[0].style.animation = "reappear 1s ease-in-out forwards";
        document.getElementsByClassName("navbarlinks")[1].style.animation = "reappear 1s ease-in-out forwards";
        document.getElementsByClassName("navbarlinks")[2].style.animation = "reappear 1s ease-in-out forwards";
        document.getElementById("login").style.animation = "dissolve 1s ease-in-out forwards";
        // setTimeout(function () {
            document.getElementById("login").style.display = "none";
        // }, 1000);
    }
    else {
        document.getElementsByClassName("subnavbar")[0].style.height = "400px";
        document.getElementsByClassName("subnavbar")[0].style.display = "block";
        document.getElementById("login").style.display = "block";
        document.getElementById("navbartoggle").children[0].onclick = function() {openLoginPage()};
        document.getElementsByClassName("navbarlinks")[0].style.animation = "dissolve 1s ease-in-out forwards";
        document.getElementsByClassName("navbarlinks")[1].style.animation = "dissolve 1s ease-in-out forwards";
        document.getElementsByClassName("navbarlinks")[2].style.animation = "dissolve 1s ease-in-out forwards";
        document.getElementById("login").style.animation = "reappear 1s ease-in-out forwards";
        // setTimeout(function() {
            document.getElementsByClassName("navbarlinks")[0].style.display = "none";
            document.getElementsByClassName("navbarlinks")[1].style.display = "none";
            document.getElementsByClassName("navbarlinks")[2].style.display = "none";
        // }, 1000);
    }
}
function openSignupPage() {
    if (document.getElementsByClassName("subnavbar")[0].style.height == "600px") {
        document.getElementById("navbartoggle").children[0].onclick = function() {openLoginPage();};
        document.getElementsByClassName("subnavbar")[0].style.height = "400px";
        document.getElementById("login").style.display = "block";
        document.getElementById("login").style.animation = "reappear 1s ease-in-out forwards";
        document.getElementById("signup").style.animation = "dissolve 1s ease-in-out forwards";
        // setTimeout(function () {
            document.getElementById("signup").style.display = "none";
        // }, 1000);
    }
    else {
        document.getElementsByClassName("subnavbar")[0].style.height = "600px";
        document.getElementsByClassName("subnavbar")[0].style.display = "block";
        document.getElementById("signup").style.display = "block";
        document.getElementById("navbartoggle").children[0].onclick = function() {
            openSignupPage();
            openLoginPage();};
        document.getElementById("login").style.animation = "dissolve 1s ease-in-out forwards";
        document.getElementById("signup").style.animation = "reappear 1s ease-in-out forwards";
        // setTimeout(function() {
        document.getElementById("login").style.display = "none";
        // }, 1000);
    }
}