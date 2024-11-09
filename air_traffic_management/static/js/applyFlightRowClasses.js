const applyFlightRowClasses = () => {
  const rows = document.querySelectorAll(
    "#currentFlightsTable tbody tr, #scheduledFlightsTable tbody tr"
  );
  //   console.log(rows);

  rows.forEach((row) => {
    // const status = row.querySelector("td:nth-child(4)").innerText.trim();
    const status = row.classList[0];
    // console.log(status);

    switch (status) {
      case "Scheduled":
        row.classList.add("flight-status-scheduled");
        break;
      case "Delayed":
        row.classList.add("flight-status-delayed");
        break;
      case "Departed":
        row.classList.add("flight-status-departed");
        break;
      case "Arrived":
        row.classList.add("flight-status-arrived");
        break;
      case "Cancelled":
        row.classList.add("flight-status-cancelled");
        break;
    }
    // console.log(status);
  });
};
document.addEventListener("DOMContentLoaded", applyFlightRowClasses);
