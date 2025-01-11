// Function to show or hide additional recipe details
function toggleDetails(button, detailsId) {
  const details = document.getElementById(detailsId);
  if (details.style.display === "none" || details.style.display === "") {
      details.style.display = "block";
      button.textContent = "Hide Details";
  } else {
      details.style.display = "none";
      button.textContent = "Show Details";
  }
}

// Highlight elements on hover
document.querySelectorAll('.recipe-item').forEach(item => {
  item.addEventListener('mouseover', () => {
      item.style.boxShadow = "0 8px 16px rgba(0, 0, 0, 0.2)";
  });

  item.addEventListener('mouseout', () => {
      item.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.1)";
  });
});
