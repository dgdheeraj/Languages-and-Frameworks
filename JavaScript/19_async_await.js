const photos = []

// function photoUpload() {
//     let uploadStatus = new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             photos.push("Profile Pic");
//             resolve("Photo Uploaded");
//         },3000)
//     })

//     let result = uploadStatus;
//     console.log(result);
//     //0-> since its not waiting
//     console.log(photos.length);
// }

// photoUpload();


async function photoUpload() {
    let uploadStatus = new Promise((resolve, reject)=>{
        setTimeout(()=>{
            photos.push("Profile Pic");
            resolve("Photo Uploaded");
        },3000)
    })

    let result = await uploadStatus;
    console.log(result);
    //0-> since its not waiting
    console.log(photos.length);
}

photoUpload();