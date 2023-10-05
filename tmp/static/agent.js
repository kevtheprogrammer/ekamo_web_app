$(document).ready(function () {
    $('#dtVerticalScrollExample').DataTable({
      "scrollY": "200px",
      "scrollCollapse": true,
    });
    $('.dataTables_length').addClass('bs-select');
  });

function toggletotalTransaction() {

    const popup = document.getElementById("agent_total_transaction");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }
function toggleCommission() {

    const popup = document.getElementById("commission");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }
function toggleDepositAmount() {

    const popup = document.getElementById("transaction");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }
function toggleDepositAwait() {

    const popup = document.getElementById("deposit-await");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }
function toggleExpence() {

    const popup = document.getElementById("expence");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }
function toggleBillfordCommission() {

    const popup = document.getElementById("billford");
    if (popup.style.display === "block") {
      popup.style.display = "none";
    } else {
      popup.style.display = "block";
    }

  }

  // Function to close the pop-up table
  