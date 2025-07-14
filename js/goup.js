//получить доступ к кнопке
const topBtn = document.querySelector(".go-top");

//Скроллинг окна
window.addEventsListener("scroll", trackScroll);
//Реакция на нажатие
topBtn.addEventsListener("click", goTop);

function trackScroll() {
    // вычисляем положение от верхушки окна
    сonst scrolled = window.pageYOffset;
    // высота клиентской области окна браузера
    //const coord = document.documentElement.clientHeight;
     const wh = document.documentElement.clientHeight; // coord или wh (одно и то же)
     // в прокрутке вышли за пределы одного экрана
     if (scrolled > wh) {
     // должна показаться кнопка
     // topBtn.classList.add("go-top--show");
     topBtn.style.display = 'block';
     }else{
     // или исчезает
     //topBtn.classList.remove("go-top--show");
      topBtn.style.display = 'none';
     }
}

function goTop() {
    // пока не дошли до верха
    if (window.pageYOffset > 0) {
    // скроллим к верху (принудительно прокручиваем окно к верху страницы)
    window.scrollBy(0, -500); // по Y на 28 px (c регулированием скорости прокрутки быстро -500)
    setTimeout(goTop, 0); // рекурсивный вызов через задержку
    }
}
