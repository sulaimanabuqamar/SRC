function loop() {
    
}
var mouseinside = false;
window.addEventListener("mousemove", function(e) {
    if(e.clientY <100) {
        this.document.getElementById("menubar").style.animation = "showMenubar 0.5s ease-in-out forwards";
    }
    else {
        this.document.getElementById("menubar").style.animation = "hideMenubar 0.5s ease-in-out forwards";
    }
})