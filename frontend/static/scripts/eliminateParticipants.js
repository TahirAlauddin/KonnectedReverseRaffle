import { setRecentDrawnTickets, setEliminationText } from "./utils.js";
import { setBackInText } from "./utils.js";

var timer;
var hiddenContainer;

export function generateFinalGrid(nameList, numberList, assignedNumbers) {

  const gridData = {};

  // Remove numbers from assignedNumbers based on values in numberList
  assignedNumbers = assignedNumbers.filter(number => !numberList.includes(number));
  for (let i = 0; i < assignedNumbers.length; i++) {
    const number = assignedNumbers[i];
    const name = nameList[i];
    gridData[number] = name;
  }

  const gridContainer = document.querySelector(".final-10-grid");
  gridContainer.innerHTML = "";

  // Iterate over the grid data and create grid items
  Object.entries(gridData).forEach(([number, name]) => {
    const gridItem = document.createElement("div");
    gridItem.className = "final-10-grid-item";
    // Set the innerHTML of the grid item
    gridItem.innerHTML = `<div class="final-number-container round-div">${number}</div><div class="final-name">${name}</div>`;
    // Append the grid item to the grid container
    gridContainer.appendChild(gridItem);

  });
  var finalContainer = document.getElementById("final-border");
  finalContainer.style.zIndex = "-999";
  finalContainer.style.opacity = "1";
  resetContainer(finalContainer);
}

export function generateWinnerBanner(nameList, numberList, totalNumbers) {
  // decrement every element in the numberList by 1 to align with JavaScript's 0-based indexing
  const adjustedNumberList = numberList.map(num => num - 1);
  let missingNumbers = [];

  // filter out names at indices specified in adjustedNumberList
  const filteredNames = nameList.filter((name, index) => !adjustedNumberList.includes(index));

  for (let i = 1; i <= totalNumbers; i++) {
    if (!numberList.includes(i)) {
      missingNumbers.push(i);
    }
  }  

  document.getElementById("winner-number-ball").innerHTML = missingNumbers[0];
  document.getElementById("winner-name").innerHTML = filteredNames[0];

  const winnerContainer = document.getElementById("winner-container");
  winnerContainer.style.zIndex = "998";
  winnerContainer.style.opacity = "1";

  let elements = document.querySelectorAll('.number-panel-grid-item');

  // Loop through all elements and add the class 'uncopiable' to them
  elements.forEach(element => element.classList.add('uncopiable'));
}


export function addClassClickListener(item, nameList, numberList, number, totalNumbers, assignedNumbers) {
  return function (event) {
    if (!item.classList.contains("number-panel-grid-item-clicked")) {
      item.classList.add("number-panel-grid-item-clicked");
      removeNumberFromPanel(nameList, numberList, number, totalNumbers);
      if (totalNumbers - 10 == numberList.length) {
        
        generateFinalGrid(nameList, numberList, assignedNumbers) 
      }
      else if (totalNumbers - 1 == numberList.length){
        

        generateWinnerBanner(nameList, numberList, totalNumbers);
      }
      else {
        hiddenContainer = document.getElementById("elimination-ball");
        resetContainer(hiddenContainer);
      }
    }
  }
};


export function removeClassClickListener(item, nameList, numberList, number, totalNumbers) {
  return function (event) {
    item.classList.remove("number-panel-grid-item-clicked");
    getNumberBack(nameList, numberList, number, totalNumbers);
  };
}


export function hideItemClickListener(item, nameList, numberList, number, totalNumbers, assignedNumbers) {
  return function (event) {
    if (window.getComputedStyle(item).opacity == "1") {
      item.style.opacity = 0.25;
      removeNumberFromPanel(nameList, numberList, number, totalNumbers);
      if (totalNumbers - 10 == numberList.length) {
        

        generateFinalGrid(nameList, numberList, assignedNumbers) 
      }
      else if (totalNumbers - 1 == numberList.length){
        

        generateWinnerBanner(nameList, numberList, totalNumbers);
      }
      else {
        hiddenContainer = document.getElementById("elimination-ball");
        resetContainer(hiddenContainer);
      }
    }
  }
}


export function showItemClickListener(item, nameList, numberList, number, totalNumbers) {
  return function (event) {
    item.style.opacity = 1;
    getNumberBack(nameList, numberList, number, totalNumbers);
  };
}


export function hideContainer(hiddenContainer) {
  hiddenContainer.style.opacity = "0";
  hiddenContainer.style.display = "none";
  hiddenContainer.style.zIndex = "-999";
}


export function setLastEliminatedHeader(nameList, numberList) {
    var lastEliminatedNum = "";
    var lastEliminatedName = "";
    if (numberList.length > 0) {
      lastEliminatedNum = numberList[0];
      lastEliminatedName = nameList[lastEliminatedNum - 1];
    }
    var lastEliminatedHeader = document.getElementById(
      "last-eliminated-header"
    );
    lastEliminatedHeader.innerHTML = `<b>#${lastEliminatedNum}</b> - ${lastEliminatedName}`;
}

function updateProgressBar (numberList, totalNumbers) {
  // Update Progress Bar
  let progress = (numberList.length / totalNumbers * 100);
  let progressBar = document.getElementById('progress-bar');
  progressBar.style.width = `${100 - progress}%`
}

export function removeNumberFromPanel(nameList, numberList, number, totalNumbers) {
  if (!numberList.includes(number)) {
    numberList.unshift(number);
  }
  hiddenContainer = document.getElementById("elimination-ball");
  setEliminationText(numberList);
  setLastEliminatedText(numberList);
  setLastEliminatedHeader(nameList, numberList);
  setRecentDrawnTickets(numberList);
  setTicketsNumber(numberList, totalNumbers);
  updateProgressBar(numberList, totalNumbers);
}

export function getNumberBack(nameList, numberList, number, totalNumbers) {
  setBackInText(number, numberList);
  var index = numberList.indexOf(number);
  if (index !== -1) {
    numberList.splice(index, 1);
  }
  setRecentDrawnTickets(numberList);
  setEliminationText(numberList);
  setLastEliminatedHeader(nameList, numberList);
  setLastEliminatedText(numberList);
  setTicketsNumber(numberList, totalNumbers);
  hiddenContainer = document.getElementById("back-container");
  resetContainer(hiddenContainer);
  updateProgressBar(numberList, totalNumbers);
}

export function resetContainer(hiddenContainer) {
  clearTimeout(timer);
  showContainer(hiddenContainer);

  var overlay = document.createElement("div");
  var pandelGrid = document.getElementById("number-panel-grid");
  var rect = pandelGrid.getBoundingClientRect();
  overlay.id = "modal-overlay";
  overlay.style.position = "fixed";
  overlay.style.backdropFilter = "blur(10px)";
  overlay.style.top = String(rect.top - 5) + "px";
  overlay.style.left = String(rect.left - 5) + "px";
  overlay.style.width = String(pandelGrid.offsetWidth + 10) + "px";
  overlay.style.height = String(pandelGrid.offsetHeight + 10) + "px";
  // console.log(pandelGrid.offsetWidth, pandelGrid.offsetHeight)
  overlay.style.zIndex = "998"; // should be less than the z-index of the hiddenContainer
  pandelGrid.appendChild(overlay);

  timer = setTimeout(function () {
    hideContainer(hiddenContainer);
    if (document.body.contains(overlay)) {
      document.getElementById("number-panel-grid").removeChild(overlay);
    }
  }, hiddenContainer.id === 'final-border' ? 5000 : 1000);
}


export function showContainer(hiddenContainer) {
  hiddenContainer.style.zIndex = "999";
  hiddenContainer.style.display = "flex";
  hiddenContainer.style.opacity = "1";
}


export function revertContainer(hiddenContainer) {
  hideContainer(hiddenContainer);
  clearTimeout(timer);
}


export function setTicketsNumber(numberList, totalNumbers) {
  var drawnTickets = document.getElementById("drawn-tickets-number");
  var unDrawnTickets = document.getElementById("undrawn-tickets-number");

  drawnTickets.textContent = numberList.length;
  unDrawnTickets.textContent = totalNumbers - numberList.length;
}


export function setLastEliminatedText(numberList) {
  var element = document.getElementById("last-eliminated"); // replace with the actual id of your element
  if (numberList.length > 0) {
    element.textContent = numberList[0];
  } else {
    element.textContent = "-";
  }
}

