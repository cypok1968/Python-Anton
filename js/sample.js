// скрипт sample.оы
// - комментарий в java script
/****************************
Здесь некоторые элементы языка
подробнее здесь: htths://learn.javascript.ru
******************************/

// Функция (как объявляется, пример)
function sayHello(name) {
document.writeln("Вас зовут" + name); // в java script строка только двойных каваычках, разделители строк в коде ; !!!!
}

let colors = ["Красный", "Синий", "Голубой"]

//объявлять переменную можно let и var (устаревшее)
/*let name = promt("Ваше имя: ");
sayHello(name); //вызов функции */
//создаем Цикл for по длине массива
/*document.writeln("<h1>Цвета:</h1><ul>");
for(let i=0; i<colors.length; i++) {
for(let i=0; i<3; i++) {
    document.writeln("<li>" + colors[i] + "</li>");
}
document.write("</ol>")*/

function changeColor() {
    //document.getElementById('alive').style.color = 'red';
    const txt = document.getElementById('alive');
    // совпадают по типу данных и по значению (===)
    if(txt.style.display === 'none') {
    txt.style.display = 'block';
    } else {
        txt.style.display ='none'
    }
}

//Подключаюсь к элементу в DOM
const txt = document.getElementById('alive').onclick = changeColor;
