const exampleSet = new Set([1,1,1,1,1,1,1]);
exampleSet.add(5);
exampleSet.add(5).add(16);
console.log(exampleSet.delete(5));
console.log(exampleSet);
console.log(exampleSet.has(7));
exampleSet.clear()
console.log(exampleSet);