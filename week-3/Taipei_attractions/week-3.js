async function fetchData(url) {
    const response = await fetch(url);
    const data = await response.json();

    for (let i = 1; i < 3; i++) {
        let data_results = data.result.results[i - 1].file;
        let link_split = data_results.split("jpg", 1) + "jpg";

        let img = document.createElement("img");
        img.src = link_split;
        document.getElementById(`Attractions${i}`).appendChild(img);

        let newListItem = document.createElement("div");
        newListItem.textContent = data.result.results[i - 1].stitle;
        document.getElementById(`Attractions${i}`).appendChild(newListItem).setAttribute("class", "BB1");
    }

    for (let i = 3; i < 11; i++) {
        let data_results2 = data.result.results[i - 1].file;
        let link_split2 = data_results2.split("jpg", 1) + "jpg";

        let img2 = document.createElement("img");
        img2.src = link_split2;
        document.getElementById(`Attractions${i}-1`).appendChild(img2);

        let newListItem2 = document.createElement("div");
        newListItem2.textContent = data.result.results[i - 1].stitle;
        document.getElementById(`Attractions${i}-2`).appendChild(newListItem2);

    }

}

fetchData("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")





