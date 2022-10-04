// return search result


const imgIds = document.querySelectorAll("img")
const artist = document.getElementsByClassName("artist-name")
const title = document.getElementsByClassName("artist-title")
const wikiA = document.getElementsByClassName("artist-wiki")
const wikiT = document.getElementsByClassName("title-wiki")


async function main() {
    
    const axiosRequests = []
    for (let i = 0; i < imgIds.length; i++) {
        axiosRequests.push(axios.get(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${imgIds[i]['id']}`));
    }
    const imgResponse = await axios.all(axiosRequests)

        for (let i = 0; i < imgIds.length; i++) {
            console.log(imgResponse[i].data)
            if (imgResponse[i].data["primaryImageSmall"])
            {
            imgIds[i].src = imgResponse[i].data["primaryImageSmall"]
            }else if(imgResponse[i].data["primaryImageSmall"] ==''){
                imgIds[i].src = "https://www.appliancepartscompany.com/webapp/img/no_image_available.jpeg"
            }
            
            if (imgResponse[i].data["artistDisplayName"]){
            artist[i].innerHTML =imgResponse[i].data["artistDisplayName"]
            } 
            if (imgResponse[i].data["title"] ){
            title[i].innerHTML =imgResponse[i].data["title"] 
            }

            if (imgResponse[i].data["artistWikidata_URL"]){
            wikiA[i].href =imgResponse[i].data["artistWikidata_URL"]
            }

            if (imgResponse[i].data["objectWikidata_URL"])
            {
            wikiT[i].href =imgResponse[i].data["objectWikidata_URL"]  
            }
          
    }
}

main();





