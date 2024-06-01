const deliveryDayInfos = document.querySelector("span#deliveryDayInformation");
const dayHour = document.querySelector("span#dayHour");

let date = new Date();
var days = [
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sabado"
];
let todayHourLeft = date.getHours();
let todayMinutesLeft = date.getMinutes();
let dayThatArrived = date.getDay();

let taxValue = 45.32;
let taxValueDescount = taxValue - 10;

if (taxValueDescount <= 0) {
    deliveryDayInfos.innerHTML = `
        ${days[dayThatArrived]} <strong class="text-success">Frete Gratis</strong>`;
    dayHour.innerHTML = `${todayHourLeft} h ${todayMinutesLeft} min`;
} else {
    deliveryDayInfos.innerHTML = `
        ${days[dayThatArrived]} por R$ ${taxValueDescount} <s class="text-body-emphasis" >R$ ${taxValue}</s>`;
}
