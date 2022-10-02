$(".show-more").on("submit", function(evt){
    showmoreObjectIDs(evt);
})




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
