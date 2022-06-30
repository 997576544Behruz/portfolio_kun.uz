const dropdowns=document.querySelectorAll(".dropdown")
dropdowns.forEach(e=>{
    const select=e.querySelector('.select')
    const caret=e.querySelector(".caret")
    const menu=e.querySelector(".menu")
    const options=e.querySelectorAll(".menu-item")
    const selected=e.querySelector(".selected")
select.addEventListener('click',()=>{
    select.classList.toggle("select-clicked")
    caret.classList.toggle("caret-rotate")
    menu.classList.toggle("menu-open")
})   
options.forEach(option=>{
    console.log(option)
    option.addEventListener('click',()=>{
        selected.innerText=option.innerText
        select.classList.remove('select-clicked')
        caret.classList.remove('caret-rotate')
        menu.classList.remove("menu-open")
        options.forEach(option=>{
            option.classList.remove('active')
        })
        option.classList.add("active")
    })
})
})
