//Used in Network requests to fetch API
const buyFlightTicket = () => {
    return new Promise((resolve, reject)=> {
        //Wrap API Call around a timeout of 3s
        setTimeout(()=>{
            const error = true;
            //Make API Call here
            if (error){
                reject("Payment failed");
            }
            else{
                resolve("Payment successful");
            }
        }, 3000)
    });
}

buyFlightTicket()
.then((success)=>{
    console.log(success)
})
.catch((error)=>{
    console.log(error);
});

