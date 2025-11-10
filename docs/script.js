function h(tag, className, text) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (text != null) el.textContent = text;
  return el;
}

const rankBox = (rank) =>
  h("div", "w-10 text-3xl font-bold text-slate-900 text-center", rank);

const coverArt = (src) => {
  const img = h("img", "w-20 h-20 rounded object-cover");
  img.src = src || "";
  img.alt = "";
  img.loading = "lazy";
  return img;
};

const mainInfo = (song, artist) => {
  const box = h("div", "flex-1");
  box.appendChild(h("div", "text-xl font-semibold text-slate-900", song));
  box.appendChild(h("div", "text-slate-500", artist));
  return box;
};

const statGrid = (lw, peak, weeks) => {
  const box = h("div", "ml-auto grid grid-cols-2 gap-x-6 gap-y-1 text-left");
  ["LW", lw, "PEAK", peak, "WEEKS", weeks].forEach((v, j) => {
    box.appendChild(
      h("div", j % 2 ? "font-semibold" : "text-slate-400 tracking-wider", v),
    );
  });
  return box;
};

const card = (rank, img, song, artist, lw, peak, weeks) => {
  const row = h(
    "div",
    "flex items-center gap-4 rounded-xl hover:bg-slate-50 ring-1 ring-slate-200 p-4",
  );
  row.append(
    rankBox(rank),
    coverArt(img),
    mainInfo(song, artist),
    statGrid(lw, peak, weeks),
  );
  return row;
};

function renderChart(csvText, chart) {
  const { data } = Papa.parse(csvText, { skipEmptyLines: true });
  if (data.length <= 1) return;

  chart.textContent = "";
  data.slice(1).forEach((row, i) => {
    const [img, song, artist, lw, peak, weeks] = row;
    chart.appendChild(card(i + 1, img, song, artist, lw, peak, weeks));
  });
}

async function loadCsv(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error("fetch failed");
    const text = await res.text();
    renderChart(text, document.getElementById("chart"));
  } catch (err) {
    console.error(err);
    document.getElementById("statusMessage").textContent =
      "File not found. Please upload a CSV file.";
  }
}

document.getElementById("fileInput")?.addEventListener("change", (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (ev) =>
    renderChart(ev.target.result, document.getElementById("chart"));
  reader.readAsText(file);
});

loadCsv("./billboard_hot_100.csv");
