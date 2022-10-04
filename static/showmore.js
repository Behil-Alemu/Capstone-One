
let showMore =document.getElementById("showMore");


// const SMartist = document.getElementsByClassName("SMartist-name")
// const SMtitle = document.getElementsByClassName("SMartist-title")
// const SMwikiA = document.getElementsByClassName("SMartist-wiki")
// const SMwikiT = document.getElementsByClassName("SMtitle-wiki")

showMore.addEventListener('click', function(){
    showmoreObjectIDs();
})




const search_base_api = "https://collectionapi.metmuseum.org/public/collection/v1/search?"

async function showmoreObjectIDs(){
    // evt.preventDefault()
    // const search = $('#search_id').val()
    let url = new URL(window.location.href);
    let search = url.searchParams.get("image");
    $('.searched-txt').append('Searched term: '+ search)
    let alldata = await $.getJSON(search_base_api,{"q":search, "hasImages": "true"});

    console.log(search)
    let allImage = getMultipleRandom(alldata["objectIDs"], 10)
    const axiosRequests = []
    for (let i = 0; i < allImage.length; i++) {
        axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${allImage[i]}`));
    }


    const imgResponse = await axios.all(axiosRequests)
    for (let i = 0; i < allImage.length; i++) {

        imgIds[i].src = imgResponse[i].data["primaryImage"]
        if(imgResponse[i].data["primaryImage"]){

            $('#img').append(`
            <img  class="img-thumbnail" class="card-image" src="${imgResponse[i].data["primaryImage"]}"></img>
            <h4>Artist Name:</h4>
            <a href="https://www.metmuseum.org/art/collection/search/${imgResponse[i].data["objectID"]}">
            <h4>${imgResponse[i].data["artistDisplayName"]}
            </h4></a>

            <h5>Art Title: </h5>
            <a href="${imgResponse[i].data["objectWikidata_URL"]}">
            <h5>${imgResponse[i].data["title"]}
            </h5></a>`
            )
        }else{
            $('#img').append(`
            <img  class="img-thumbnail" class="card-image" src="https://www.appliancepartscompany.com/webapp/img/no_image_available.jpeg"></img>

           <h4>Artist Name:</h4>
            <a href="https://www.metmuseum.org/art/collection/search/${imgResponse[i].data["objectID"]}">
            <h4>${imgResponse[i].data["artistDisplayName"]}
            </h4></a>

            <h5>Art Title: </h5>
            <a href="${imgResponse[i].data["objectWikidata_URL"]}">
            <h5>${imgResponse[i].data["title"]}
            </h5></a>`
            )
        }
        
        }



    
}
// $(".show-more").on("submit", function(evt){
//     randomObjectIDs(evt);
// })


function getMultipleRandom(arr, num) {
    const shuffled = [...arr].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, num);
  }
