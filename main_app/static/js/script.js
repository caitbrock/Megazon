const plusButton = document.querySelector("#plus");
const minusButton = document.querySelector("#minus");
const number = document.querySelector(".number-entry");
const numberEntry = document.querySelector(".number-entry > h3");
const count = document.querySelector(".count > h1");

// VARIABLES
numberEntry.textContent = 10;
numberEntry.value = 10;
count.value = 0;

//FUNCTIONS
minusNum = () => {
  let randomInteger = Number(numberEntry.value) || 0;
  count.value = count.value - numberEntry.value;
  count.textContent = count.value;
};

plusNum = () => {
  let randomInteger = Number(numberEntry.value) || 0;
  count.value = count.value + numberEntry.value;
  count.textContent = count.value;

  //   count.textContent = numberEntry.value + 1;
  //   let randomInteger = Number(numberEntry.value) || 0;
  //   numberEntry.value = randomInteger + 1;
  //   numberEntry.textContent = numberEntry.value;
};

countCalc = () => {};
//EVENT LISTENERS
minusButton.addEventListener("click", minusNum);
plusButton.addEventListener("click", plusNum);