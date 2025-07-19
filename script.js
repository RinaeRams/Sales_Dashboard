const ctx = document.getElementById('salesChart').getContext('2d');

const chartDataSets = {
  monthly: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    data: [3100, 4500, 5000, 6200, 7200, 6900, 8100],
  },
  quarterly: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    data: [12600, 18900, 20500, 17500],
  },
  yearly: {
    labels: ['2021', '2022', '2023', '2024', '2025'],
    data: [52000, 68000, 74500, 81000, 89500],
  }
};

let currentChart;

function renderChart(type) {
  const chartData = chartDataSets[type];

  if (currentChart) currentChart.destroy();

  currentChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: chartData.labels,
      datasets: [{
        label: 'Sales',
        data: chartData.data,
        backgroundColor: 'rgba(79, 70, 229, 0.2)',
        borderColor: '#4f46e5',
        borderWidth: 2,
        tension: 0.4,
        fill: true,
        pointBackgroundColor: '#4f46e5',
        pointRadius: 4
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top'
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

// Initial render
renderChart('monthly');

// Filter event
document.getElementById('chartFilter').addEventListener('change', (e) => {
  renderChart(e.target.value);
});

// Theme toggle
const themeBtn = document.getElementById('themeToggle');

function setTheme(isDark) {
  document.body.classList.toggle('dark', isDark);
  themeBtn.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Load saved theme
const savedTheme = localStorage.getItem('theme') === 'dark';
setTheme(savedTheme);

// Toggle theme on click
themeBtn.addEventListener('click', () => {
  const isDark = !document.body.classList.contains('dark');
  setTheme(isDark);
});
