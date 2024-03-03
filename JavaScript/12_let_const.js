/*
Variable hoisting
*/
if (false) {
    var example = 5;
}

console.log(example)
//Output undefined

/*
var example;

if (false) {
    example = 5;
}
*/

// Let is stricter and has scope of the block it is defined in
// const also has the scope of the block, can't be reset for primitive types
// const for arrays can still be odified, like push to array, but cannot change existing value
