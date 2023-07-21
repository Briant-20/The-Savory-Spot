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
            categoryItem.style.display = 'block';
        }
        else{
            categoryItem.style.display = 'none';
        }
    }
    }
}
for (let i = 0; i < categoryTitles.length; i++) {
    let categoryTitle = categoryTitles[i];
    categoryTitle.addEventListener("click", display_category(categoryTitle));
}

$(document).ready(function () {
    const daysPerMonth = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

        $('#month').change(function () {
            let selectedMonth = $(this).val();
            let days = daysPerMonth[selectedMonth];
            let daySelector = $('#day');
            daySelector.empty();
            for (let day = 1; day <= days; day++) {
                daySelector.append(`<option value="${day}">${day}</option>`);
            }
        });
    });