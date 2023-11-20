let categoryTitles = document.getElementsByClassName("category-titles");
let categoryItems = document.getElementsByClassName("category-items");

let display_category = (categoryTitle) =>{
    return function(){
    let category = categoryTitle.getAttribute("data-category");
    for (let i = 0; i < categoryItems.length; i++) {
        let categoryItem = categoryItems[i];
        let itemCategory = categoryItem.getAttribute("data-category");
        if (itemCategory === category){
            categoryItem.style.display = 'block';
        }
        else{
            categoryItem.style.display = 'none';
        }
    }
    };
};
for (let i = 0; i < categoryTitles.length; i++) {
    let categoryTitle = categoryTitles[i];
    categoryTitle.addEventListener("click", display_category(categoryTitle));
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
    };

$('.month').change(function () {
    let selectedMonth = $(this).val();
    let selectedYear = document.getElementById("year").value;
    let currentYear = document.getElementById('current_year').value;
    let currentMonth = document.getElementById('current_month_value').value;
    let days = daysPerMonth[selectedMonth];
    let startDay = 1;
    if (selectedYear === currentYear){
        if ( selectedMonth === currentMonth){
            startDay = document.getElementById('current_day_value').getAttribute("data-current_value");
        }
    }
    let daySelector = $('#day');
    daySelector.empty();
    daySelector.append(`<option value="">Select a day</option>`);
    for (let day = startDay; day <= days; day++) {
        let date = getDayWithPostfix(day);
        daySelector.append(`<option value="${date}">${date}</option>`);
    }
});
});

$('#year').change(function () {
    let selectedYear = $(this).val();
    let currentYear = $('#current_year').val();
    let currentMonthContainer = document.getElementById('current_month_container');
    let monthContainer = document.getElementById('month_container');
    let currentMonth = document.getElementById('current_month');
    let month = document.getElementById('month');
    if (selectedYear === currentYear) {
        currentMonthContainer.style.display = 'block';
        monthContainer.style.display = 'none';
        month.removeAttribute("required");
        currentMonth.setAttribute("required", "required");
        month.value = "";
    } 
    else{
        currentMonthContainer.style.display = 'none';
        monthContainer.style.display = 'block';
        month.setAttribute("required", "required");
        currentMonth.removeAttribute("required");
        currentMonth.value = "";
    }
});

$('#day').change(function () {
    let selectedDay = $(this).val();
    let currentDay = document.getElementById('current_day_value').getAttribute("data-current_value");
    currentDay = getDayWithPostfix(currentDay);
    let selectedMonth = document.getElementById("current_month").value;
    let selectedYear = document.getElementById("year").value;
    let currentYear = document.getElementById('current_year').value;
    let currentMonth = document.getElementById('current_month_value').value;
    let currentTimeContainer = document.getElementById("current_time_container");
    let timeContainer = document.getElementById("time_container");
    let currentTime = document.getElementById("current_time");
    let time = document.getElementById("time");
    if (selectedYear === currentYear && selectedMonth === currentMonth && selectedDay === currentDay){
        currentTimeContainer.style.display = "block";
        timeContainer.style.display = "none";
        time.removeAttribute("required");
        currentTime.setAttribute("required", "required");
        time.value = "";
    }
    else{
        currentTimeContainer.style.display = "none";
        timeContainer.style.display = "block";
        currentTime.removeAttribute("required");
        time.setAttribute("required", "required");
        currentTime.value = "";
    }
});