class Animal {
    constructor(type, legs) {
        this.type = type;
        this.legs = legs;
    }

    makeNoise(sound = "Loud Noise") {
        console.log(sound);
    }

    static returnVal() {
        return 10;
    }

    //treats like a property
    get metaData() {
        return `${this.type} ${this.legs}`;
    }
}

let cat = new Animal("Mammal", 4);
cat.type = "Cat";
cat.makeNoise();
cat.makeNoise("Meow");
console.log(Animal.returnVal());
console.log(cat.metaData)

//Inheritance

class Dog extends Animal {
    constructor(type, legs) {
        super(type, legs);
    }

    makeNoise(sound = "Meow"){
        console.log(sound);
    }
}

let obj2 = new Dog("Dog", 4);
obj2.makeNoise();

/*

Create a class Player with the following:
- Add a Name and Country properties
- Add a function that when it runs should print into the console ("Messi was born in Argentina");
- Make sure to adapt this function to receive dynamic Names and Clubs.

Create a Subclass called TennisPlayer that extends from the class Player
- Add a new property Age.
- Add a function that when it runs should print into the console something similar ("Rafael Nadal is 34 years old and knows how to play Tennis");
- Make sure the Name and Age are dynamic.
*/
class Player {
    constructor(name, country) {
        this.name = name;
        this.country = country;
    }

    getInfo() {
        return `${this.name} was born in ${this.country}`;
    }
}

class TennisPlayer extends Player {
    constructor(name, country, age) {
        super(name, country)
        this.age = age;
    }

    getInfo() {
        return `${this.name} is ${this.age} years old and knows how to play Tennis`
    }
}