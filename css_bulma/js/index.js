// mobile menu
const burgerIcon = document.querySelector("#burger");
const navbarMenu = document.querySelector("#nav-links");

if (burgerIcon) {
    burgerIcon.addEventListener("click", () => {
        navbarMenu.classList.toggle("is-active")
    })    
}

// tabs
const tabs = document.querySelectorAll(".tabs li");
const tabContentBoxes = document.querySelectorAll("#tab-content > div");

if (tabs) {
    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            tabs.forEach(item => item.classList.remove("is-active"))
            tab.classList.add("is-active");
    
            const target = tab.dataset.target;
            console.log(target); // print
            tabContentBoxes.forEach(box => {
                if (box.getAttribute("id") == target) {
                    box.classList.remove("is-hidden");
                } else {
                    box.classList.add("is-hidden");
                }
            });
        })
    })
}
