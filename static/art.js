
$(function() {
let BASE_URL ="https://collectionapi.metmuseum.org/public/collection/v1";

let five_art_pieces=[]
async function five_art_piece(){
    let alldata = await $.getJSON(`${BASE_URL}/search?hasImages=true&q=Paintings`);
    for (let i = 1; i < 10; i++) {
        let randomIdx = Math.floor(Math.random()*alldata.objectIDs.length)
        let randomImg = await $.getJSON(`${BASE_URL}/objects/${alldata.objectIDs[randomIdx]}`);

    five_art_pieces.push(randomImg)
    let imageSpliced = five_art_pieces.splice(0,1)

    imageSpliced.map(art => {
        $("div").append(`<img  class="img-fluid " src="${art.primaryImage}"></img>`)
    })
    } 

}
five_art_piece()
});
