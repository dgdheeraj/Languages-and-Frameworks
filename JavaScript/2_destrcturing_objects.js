const player = {
    name: "abc",
    club: "fweg",
    address: {
        city: "Los Angeles"
    }
};

// Long to always access attributes of nested objects with a .
console.log(player.address.city);

// destructuring objects in this way makes it easier
const {pname, club, address:{city} } = player;
// console.log(pname);
// console.log(club);
// console.log(city);


const student = {
    name: "Kyle",
    age: 24,
    projects: {
        diceGame: "Two player dice game using JavaScript"
    }
}

const {name, age, projects: {diceGame} } = student;
console.log(`${name} is of age ${age} and has project in ${diceGame}`);