// Helpful when many arguments in a function

function add(nums) {
    //console.log(nums);
    //Output-> 4

    console.log(arguments);
    //output {0: 4, 1: 5, 2: 7, 3: 8, 4: 12} an iterator basically
}

add(4,5,7,8,12);


function add2(...nums) {
    console.log(nums);
}

add2(4,5,7,8,12);