const table = document.querySelector(".responsive-table");
const rows = table.querySelectorAll(".table-row");
const pagination = document.querySelector("#pagination");
const previous = document.querySelector("#previous");
const next = document.querySelector("#next");

let currentPage = 1;
const rowsPerPage = 3;

function showPage() {
  const startRow = (currentPage - 1) * rowsPerPage;
  const endRow = startRow + rowsPerPage;

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    if (i >= startRow && i < endRow) {
      row.style.display = "flex";
    } else {
      row.style.display = "none";
    }
  }
}
if (rows.length < 4){
  pagination.style.display = "none";
}
if(pagination){
pagination.addEventListener("click", function(event) {
  if (event.target === previous) {
    currentPage--;
  } else if (event.target === next) {
    currentPage++;
  }

  showPage();
});};

showPage();
