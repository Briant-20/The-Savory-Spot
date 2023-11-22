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

// Attach a change event listener to the element with id 'year'
$('#year').change(function () {
    // Get the selected year value
    let selectedYear = $(this).val();

    // Get the current year value from the element with id 'current_year'
    let currentYear = $('#current_year').val();

    // Get references to relevant HTML elements
    let currentMonthContainer = document.getElementById('current_month_container');
    let monthContainer = document.getElementById('month_container');
    let currentMonth = document.getElementById('current_month');
    let month = document.getElementById('month');

    // Check if the selected year is the same as the current year
    if (selectedYear === currentYear) {
        // Display the container for the current month
        currentMonthContainer.style.display = 'block';

        // Hide the container for selecting a different month
        monthContainer.style.display = 'none';

        // Make the 'month' input not required
        month.removeAttribute("required");

        // Make the 'currentMonth' input required
        currentMonth.setAttribute("required", "required");

        // Clear the value of the 'month' input
        month.value = "";
    } 
    else {
        // Hide the container for the current month
        currentMonthContainer.style.display = 'none';

        // Display the container for selecting a different month
        monthContainer.style.display = 'block';

        // Make the 'month' input required
        month.setAttribute("required", "required");

        // Make the 'currentMonth' input not required
        currentMonth.removeAttribute("required");

        // Clear the value of the 'currentMonth' input
        currentMonth.value = "";
    }
});


// Triggering the function when the value of the element with id 'day' changes
$('#day').change(function () {
    // Get the selected day from the dropdown
    let selectedDay = $(this).val();

    // Get the current day from the 'data-current_value' attribute of the element with id 'current_day_value'
    let currentDay = document.getElementById('current_day_value').getAttribute("data-current_value");
    
    // Format the current day with a postfix (assuming there's a function getDayWithPostfix)
    currentDay = getDayWithPostfix(currentDay);

    // Get the selected month from the element with id 'current_month'
    let selectedMonth = document.getElementById("current_month").value;

    // Get the selected year from the element with id 'year'
    let selectedYear = document.getElementById("year").value;

    // Get the current year from the element with id 'current_year'
    let currentYear = document.getElementById('current_year').value;

    // Get the current month from the element with id 'current_month_value'
    let currentMonth = document.getElementById('current_month_value').value;

    // Get references to various DOM elements
    let currentTimeContainer = document.getElementById("current_time_container");
    let timeContainer = document.getElementById("time_container");
    let currentTime = document.getElementById("current_time");
    let time = document.getElementById("time");

    // Check if the selected date is the current date
    if (selectedYear === currentYear && selectedMonth === currentMonth && selectedDay === currentDay) {
        // If yes, show the current time container and hide the time container
        currentTimeContainer.style.display = "block";
        timeContainer.style.display = "none";

        // Make adjustments to the 'required' attribute of the time input fields
        time.removeAttribute("required");
        currentTime.setAttribute("required", "required");

        // Reset the value of the time input field
        time.value = "";
    } else {
        // If not the current date, hide the current time container and show the time container
        currentTimeContainer.style.display = "none";
        timeContainer.style.display = "block";

        // Make adjustments to the 'required' attribute of the time input fields
        currentTime.removeAttribute("required");
        time.setAttribute("required", "required");

        // Reset the value of the current time input field
        currentTime.value = "";
    }
});