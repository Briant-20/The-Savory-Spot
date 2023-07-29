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
    let daysPerMonth = {
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

function getDayWithPostfix(day) {
    if (day >= 11 && day <= 13) {
            return day + 'th';}
    switch (day % 10) {
        case 1:
            return day + 'st';
        case 2:
            return day + 'nd';
        case 3:
            return day + 'rd';
        default:
            return day + 'th';
        }
}

$('.month').change(function () {
    let selectedMonth = $(this).val();
    let days = daysPerMonth[selectedMonth];
    let daySelector = $('#day');
    daySelector.empty();
    for (let day = 1; day <= days; day++) {
        date = getDayWithPostfix(day)
        daySelector.append(`<option value="${date}">${date}</option>`);
    }
});
});

$('#year').change(function () {
    let selectedYear = $(this).val();
    let current_year = $('#current_year').val();
    let current_month_container = document.getElementById('current_month_container');
    let month_container = document.getElementById('month_container');
    let current_month = document.getElementById('current_month');
    let month = document.getElementById('month');


    if (selectedYear === current_year) {
        current_month_container.style.display = 'block';
        month_container.style.display = 'none';
        month.removeAttribute("required");
        current_month.setAttribute("required", "required");
    } 
    else{
        current_month_container.style.display = 'none';
        month_container.style.display = 'block';
        month.setAttribute("required", "required");
        current_month.removeAttribute("required");
    }
});

