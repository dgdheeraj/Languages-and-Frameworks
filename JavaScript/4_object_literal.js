function addressMaker(city, state) {
    // const newAddress = {newCity:city, newState:state};

    // If we directly assign the variables to the object, var name becomes key
    // dont have to use {city:city, state:state}
    const newAddress = {city, state};

    console.log(newAddress);
}

addressMaker('Austin', 'Texas');