let incomes = [62000, 67000, 75000];
let total = 0;

for (const val of incomes)
{
    total+=val;
}
// console.log(total);

const students = [ 
    { name: "John", city: "New York" },
    { name: "Peter", city: "Paris"},
    { name: "Kate", city: "Sidney" }
]

for (const student of students)
{
    console.log(`${student.name} lives in ${student.city}`);
}