const statusElement = document.getElementById("statusMessage");
function setStatus(msg) {
  statusElement.textContent = msg;
  setTimeout(() => {
    if (statusElement.textContent === msg) statusElement.textContent = "";
  }, 3000);
}

function renderCell(tag, cell) {
  const el = document.createElement(tag);
  el.className = "text-lg";
  if (URL.canParse(cell)) {
    const img = document.createElement("img");
    img.src = cell;
    img.alt = "";
    img.loading = "lazy";
    img.className = "w-28 object-contain";
    el.appendChild(img);
  } else {
    el.textContent = cell;
  }
  return el;
}

function displayCSV(text) {
  const { data } = Papa.parse(text, { skipEmptyLines: true });
  const table = document.getElementById("table");
  table.textContent = "";

  data.forEach((row, i) => {
    const tag = i === 0 ? "th" : "td";
    const tr = document.createElement("tr");
    if (i === 0) tr.className = "bg-blue-700 text-white";

    const tdIndex = document.createElement(tag);
    tdIndex.className = "text-xl font-bold px-4 py-2";
    tdIndex.textContent = i === 0 ? "#" : i;
    tr.appendChild(tdIndex);

    row.forEach((cell) => {
      const td = renderCell(tag, cell);
      td.classList.add("px-4", "py-2");
      tr.appendChild(td);
    });

    table.appendChild(tr);
  });
}

document.getElementById("fileInput").addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (event) => {
    displayCSV(event.target.result);
    setStatus(file.name + " loaded successfully!");
  };
  reader.readAsText(file);
});

async function loadCsv(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("File not found");

    const text = await response.text();
    displayCSV(text);
    setStatus("");
  } catch (err) {
    console.error("Error loading file:", err);
    setStatus("File not found. Please upload a CSV file.");
  }
}

loadCsv("billboard_hot_100.csv");
