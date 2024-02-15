let lastScrollTop = 0;

window.addEventListener("scroll", function(){
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScroll > lastScrollTop){
        document.getElementById("header").classList.add("hidden");
    } else {
        document.getElementById("header").classList.remove("hidden");
    }
    lastScrollTop = currentScroll;
});