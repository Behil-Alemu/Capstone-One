


// const search_base_api = "https://collectionapi.metmuseum.org/public/collection/v1/search?"

// async function randomObjectIDs(evt){
//     evt.preventDefault()
//     const search = $('#search_id').val()
//     $('.searched-txt').append('Searched term: '+ search)
//     let alldata = await $.getJSON(search_base_api,{"q":search, "hasImages": "true"});

//     console.log(search)
//     let allImage = getMultipleRandom(alldata["objectIDs"], 10)
//     const axiosRequests = []
//     for (let i = 0; i < allImage.length; i++) {
//         axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${allImage[i]}`));
//     }


//     const imgResponse = await axios.all(axiosRequests)
//     for (let i = 0; i < allImage.length; i++) {

//         imgIds[i].src = imgResponse[i].data["primaryImage"]

//         $('#img').append(`<img  class="img-thumbnail" class="card-image" src="${imgResponse[i].data["primaryImage"]}" id="${imgResponse[i].data["objectID"]}"></img>`)
//         }



    
// }
// $(".show-more").on("submit", function(evt){
//     randomObjectIDs(evt);
// })


// function getMultipleRandom(arr, num) {
//     const shuffled = [...arr].sort(() => 0.5 - Math.random());
//     return shuffled.slice(0, num);
//   }






const imgIds = document.querySelectorAll("img")
const artist = document.getElementById("p")


async function main() {
    const axiosRequests = []
    for (let i = 0; i < imgIds.length; i++) {
        axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${imgIds[i]['id']}`));
    }
    const imgResponse = await axios.all(axiosRequests)
        for (let i = 0; i < imgIds.length; i++) {
            imgIds[i].src = imgResponse[i].data["primaryImage"]
        //     artist.innerHTML =  imgResponse[i].data["artistDisplayName"]  
        // }
        }
}

main();

$(".show-more").on("submit", function(evt){
    showmoreObjectIDs(evt);
})


// seach with q= then display the first few searches(view more butten at the bottom)
// user can put in date to search (dateBegin=1700&dateEnd=1800)
// maybe later! add an interactive map to see art based on artist country