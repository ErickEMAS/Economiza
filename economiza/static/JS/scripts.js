function abrirMenu (){
    let menu = document.querySelector('.open-nav');
    menu.classList.toggle('close');
    let menuItens = document.querySelector('.menu');
    menuItens.classList.toggle('active');
    console.log ('Menuteste')
}
