//function declatation
function breakfastMenu() {
    return " SAmple string";
}

//anonymous function
const lunchMenu = function() {
    return "Sample String"
}

// Arrow Function
// const dinnerMenu = (s1) => {
//     return `${s1} Sample Menu`;
// }

//If you're only returning a single value from this function
const dinnerMenu = (s1) => `${s1} Sample Menu`;


console.log(dinnerMenu("Salad"));