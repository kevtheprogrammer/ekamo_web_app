


$(document).ready(function(){
    $("#myInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

  // Function to filter dates
  function filterDates() {
    const startDate = document.getElementById("start-date").value;
    const endDate = document.getElementById("end-date").value;

    const filteredDates = dateList.filter(date => {
        return date >= startDate && date <= endDate;
    });

    displayFilteredDates(filteredDates);
}

// Function to display filtered dates
function displayFilteredDates(filteredDates) {
    const filteredDatesList = document.getElementById("filtered-dates");

    // Clear the list
    filteredDatesList.innerHTML = "";

    // Add filtered dates to the list
    filteredDates.forEach(date => {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
        listItem.textContent = date;
        filteredDatesList.appendChild(listItem);
    });
}

// Attach click event to filter button
const filterButton = document.getElementById("filter-button");
filterButton.addEventListener("click", filterDates);
