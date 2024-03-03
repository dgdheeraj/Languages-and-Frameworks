let contacts = ["Mary", "Joel", "Danny"];

// Spread Operator to make a copy of array

// let p = [...contacts]
let  p = ["Dheeraj", ...contacts, "David"]
contacts.push("J");

console.log("after push contacts:",contacts);
console.log("after push p: ",p);

let person = {
    name: "Adam",
    age: 25,
    city: "LA"
}

let employee = {
    ...person,
    id:"125"
}


