let categoryTitles = document.getElementsByClassName("category-titles");
let categoryItems = document.getElementsByClassName("category-items");

let display_category = (categoryTitle) =>{
    return function(){
    categoryName = categoryTitle.getAttribute("name");
    category = categoryTitle.getAttribute("category");
    for (let i = 0; i < categoryItems.length; i++) {
        let categoryItem = categoryItems[i];
        itemCategory = categoryItem.getAttribute("category");
        if (itemCategory === category){
            categoryItem.style.visibility = 'visible';
        }
        else{
            categoryItem.style.visibility = 'hidden';
        }
    }
    }
}
for (let i = 0; i < categoryTitles.length; i++) {
    let categoryTitle = categoryTitles[i];
    categoryTitle.addEventListener("click", display_category(categoryTitle));
}