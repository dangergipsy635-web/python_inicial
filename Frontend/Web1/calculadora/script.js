const display = document.getElementById('display');

function append(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = '';
}

function deleteLast() {
  display.value = display.value.slice(0, -1);
}

function calculate() {
  try {
    display.value = eval(display.value.replace(/÷/g, '/').replace(/×/g, '*'));
  } catch {
    display.value = 'Error';
  }
}

// ✅ Soporte para el teclado
document.addEventListener('keydown', function(event) {
  const key = event.key;

  if (!isNaN(key) || key === '.') {
    append(key);
  } else if (['+', '-', '*', '/', '%'].includes(key)) {
    append(key);
  } else if (key === 'Enter' || key === '=') {
    calculate();
  } else if (key === 'Backspace') {
    deleteLast();
  } else if (key.toLowerCase() === 'c') {
    clearDisplay();
  }
});
