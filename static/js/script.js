// Get all elements with the class "category-titles"
let categoryTitles = document.getElementsByClassName("category-titles");

// Get all elements with the class "category-items"
let categoryItems = document.getElementsByClassName("category-items");

// Function to display items based on selected category
let display_category = (categoryTitle) => {
    return function () {
        // Get the data-category attribute value of the clicked category title
        let category = categoryTitle.getAttribute("data-category");

        // Loop through all category items
        for (let i = 0; i < categoryItems.length; i++) {
            let categoryItem = categoryItems[i];

            // Get the data-category attribute value of the current category item
            let itemCategory = categoryItem.getAttribute("data-category");

            // Check if the category of the clicked title matches the category of the current item
            if (itemCategory === category) {
                categoryItem.style.display = 'block'; // Display the item
            } else {
                categoryItem.style.display = 'none';  // Hide the item
            }
        }
    };
};

// Add click event listeners to each category title
for (let i = 0; i < categoryTitles.length; i++) {
    let categoryTitle = categoryTitles[i];
    categoryTitle.addEventListener("click", display_category(categoryTitle));
}

// Function to get the day with the appropriate postfix (e.g., 1st, 2nd, 3rd)
function getDayWithPostfix(day) {
    // Special case for 11th to 13th
    if (day >= 11 && day <= 13) {
        return day + 'th';
    }

    // Determine the postfix based on the last digit of the day
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

// Execute the following code when the document is fully loaded and ready
$(document).ready(function () {

    // Define the number of days for each month in a non-leap year
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

    // Attach an event listener to the 'change' event of elements with class 'month'
    $('.month').change(function () {
        
        // Get the selected month value
        let selectedMonth = $(this).val();
        
        // Get the selected year value from the element with id 'year'
        let selectedYear = document.getElementById("year").value;

        // Get the current year value from the element with id 'current_year'
        let currentYear = document.getElementById('current_year').value;

        // Get the current month value from the element with id 'current_month_value'
        let currentMonth = document.getElementById('current_month_value').value;

        // Initialize the number of days in the selected month
        let days = daysPerMonth[selectedMonth];

        // Initialize the start day as 1
        let startDay = 1;

        // Check if the selected year is the same as the current year
        if (selectedYear === currentYear) {
            // Check if the selected month is the same as the current month
            if (selectedMonth === currentMonth) {
                // If true, set the start day to the current day value
                startDay = document.getElementById('current_day_value').getAttribute("data-current_value");
            }
        }

        // Get the day selector element with id 'day'
        let daySelector = $('#day');

        // Empty the day selector dropdown and add a default option
        daySelector.empty();
        daySelector.append(`<option value="">Select a day</option>`);

        // Populate the day selector with options for each day in the selected month
        for (let day = startDay; day <= days; day++) {
            // Format the day with a postfix (e.g., 1st, 2nd, 3rd)
            let date = getDayWithPostfix(day);
            // Append the formatted date as an option to the day selector
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