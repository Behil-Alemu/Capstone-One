
// $(function() {
// let searched_URL ="http://127.0.0.1:5000/";
// let objectIDs_api="https://collectionapi.metmuseum.org/public/collection/v1/objects/"
// async function ten_art_piece(){
//     const res = await axios.get(`${searched_URL}/ten_random`)
//     const ids=res.data
//     console.log(ids)


   

//     const responses = await Promise.all()(
//         ids.map(async id => {
//             const res = await fetch(
//                 `${objectIDs_api}${id}`
//             ); // Send request for each id
//         })
//     );
  
// }
// ten_art_piece()
// });



// seach with q= then display the first few searches(view more butten at the bottom)
// user can put in date to search (dateBegin=1700&dateEnd=1800)
// maybe later! add an interactive map to see art based on artist country