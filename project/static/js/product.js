const deliveryDayInfos = document.querySelector("span#deliveryDayInformation");
var dayThatArrived = new Date().getDay();
// var taxValue = 45.32;
var taxValue = 0;
var taxValueDescount = taxValue - 10;
if (taxValueDescount <= 0) {
    deliveryDayInfos.innerHTML = `
        ${dayThatArrived} <strong class="text-success">Frete Gratis</strong>`;
} else {
    deliveryDayInfos.innerHTML = `
        ${dayThatArrived} por R$ ${taxValueDescount} <s class="text-body-emphasis" >R$ ${taxValue}</s>`;
}
