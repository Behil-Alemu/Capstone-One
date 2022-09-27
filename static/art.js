


const search_base_api = "https://collectionapi.metmuseum.org/public/collection/v1/search"


async function randomObjectIDs(evt){
    evt.preventDefault();
    const search = $('#search_id').val()
    let alldata = await $.getJSON(search_base_api,{"q":search, "hasImages": "true"});
    let allImage = getMultipleRandom(alldata["objectIDs"], 10)

    const axiosRequests = []
    for (let i = 0; i < allImage.length; i++) {
        axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${allImage[i]}`));
    }
    const imgURLs = []
    const imgIds = document.querySelectorAll("img")
    const imgResponse = await axios.all(axiosRequests)
    for (let i = 0; i < allImage.length; i++) {

        imgIds[i].src = imgResponse[i].data["primaryImage"]
        console.log( imgIds[i].src)
        }


    
}
$(".search-txt").on("submit", function(evt){
    randomObjectIDs(evt);
})


function getMultipleRandom(arr, num) {
    const shuffled = [...arr].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, num);
  }


// const imgIds = document.querySelectorAll("img")


// async function main() {
//     const axiosRequests = []
//     for (let i = 0; i < imgIds.length; i++) {
//         axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${imgIds[i]}`));
//     }

//     const imgResponse = await axios.all(axiosRequests)
//     for (const i = 0; i < imgIds.length(); i++) {
//         imgIds[i].src = imgResponse[i].data["primaryImage"]
//     }
// }

// main();


// seach with q= then display the first few searches(view more butten at the bottom)
// user can put in date to search (dateBegin=1700&dateEnd=1800)
// maybe later! add an interactive map to see art based on artist country