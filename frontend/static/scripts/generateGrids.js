import { removeClassClickListener, hideItemClickListener, 
  resetContainer, showItemClickListener, addClassClickListener, generateFinalGrid, removeNumberFromPanel, handleClickImageNotAdded, handleClickImageAdded } from "./eliminateParticipants.js";
import { setEventInfoName, setEventInfoDate, addBackground } from "./utils.js";

let host = 'http://localhost:8323'
let grid;
// Generate the grid and append it to the container
var container = document.getElementById("number-panel-grid");
var totalNumbers = 0;

var numberList = [];
var nameList = [];

// Define the URL of the image you want to use as background
// var imageUrl = "/static/images/Rectangle 7.png";
var imageUrl = null;

let barCodeNumber = '';


function qrCodeEliminator(event) {  
  var elements;
  var item;

  // Check if the key pressed was the "enter" key
  if (event.key == 'Enter') {
    elements = document.querySelectorAll(".number-panel-grid-item p");
    if (window.getComputedStyle(document.getElementById("number-panel-grid")).getPropertyValue('background-image') !== "none") {
      for (var i = 0; i < elements.length; i++) {
        if (elements[i].textContent === barCodeNumber) {
          // Eliminate the element
          item = document.getElementById(i+1);
          if (window.getComputedStyle(item).opacity == "1") {
            item.style.opacity = 0.25;
            removeNumberFromPanel(nameList, numberList, barCodeNumber, totalNumbers);
            if (totalNumbers - 10 == numberList.length) {        
              generateFinalGrid(nameList, numberList) 
            }
            else if (totalNumbers - 1 == numberList.length){
              generateWinnerBanner(nameList, numberList, totalNumbers);
            }
            else {
              let hiddenContainer = document.getElementById("elimination-ball");
              resetContainer(hiddenContainer);
            }
          }
        }
      }
    } else {
      for (var i = 0; i < elements.length; i++) {
        if (elements[i].textContent === barCodeNumber) {
          // Eliminate the element
          item = document.getElementById(i+1);
          if (!item.classList.contains("number-panel-grid-item-clicked")) {
            item.classList.add("number-panel-grid-item-clicked");
            removeNumberFromPanel(nameList, numberList, barCodeNumber, totalNumbers);
            if (totalNumbers - 10 == numberList.length) {
            
            
            generateFinalGrid(nameList, numberList) 
          }
          else if (totalNumbers - 1 == numberList.length){
              
              generateWinnerBanner(nameList, numberList, totalNumbers);
            }
            else {
              let hiddenContainer = document.getElementById("elimination-ball");
              resetContainer(hiddenContainer);
            }
          }
        }
      }
    }

    // Find the element with the same number as the barcode value
    barCodeNumber = '';
  } else {
    barCodeNumber += event.key;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  
  function generateGrid(totalNumbers, assignedNumbers, clickable) { 
    // assignedNumbers = assignedNumbers.slice(0,15)
    // totalNumbers = 15
    var columns;
    var grid = document.createElement("div");
    var number = 0;
    if (totalNumbers <= 50) {
      columns = 9;
      grid.className = "very-large-grid";
    } else if (totalNumbers <= 100) {
      columns = 12;
      grid.className = "large-grid";
    } else if (totalNumbers <= 150) {
      columns = 14;
      grid.className = "medium-grid";
    } else if (totalNumbers <= 200) {
      columns = 16;
      grid.className = "small-grid";
    } else if (totalNumbers <= 250) {
      columns = 18;
      grid.className = "very-small-grid";
    } else if (totalNumbers <= 300) {
      columns = 20;
      grid.className = "extremely-small-grid";
    }

    let count = 0;
    for (var i = 0; i < Math.ceil(totalNumbers / columns); i++) {
      for (var j = 0; j < columns && count < totalNumbers; j++) {
        var gridItem = document.createElement("div");
        gridItem.className = "number-panel-grid-item";
        number = assignedNumbers[count];
        gridItem.id = number;

        var paragraph = document.createElement("p");
        paragraph.className = "uncopiable";
        paragraph.textContent = number.toString();

        
        gridItem.appendChild(paragraph);
        
        if (clickable) {
          if (imageUrl != null) {
            gridItem.addEventListener('click', handleClickImageAdded(gridItem, nameList, numberList, number, totalNumbers, assignedNumbers))
          } else {
            gridItem.addEventListener('click', handleClickImageNotAdded(gridItem, nameList, numberList, number, totalNumbers, assignedNumbers))
          }
        }
        grid.appendChild(gridItem);
        count++;
      }
    }

    return grid;
  }

  var assignedNumbers = [];
  fetch(`${host}/getCSVData/`)
    .then(response => response.json())
    .then(data => {
        // assuming the JSON structure is like { "data": [ { "assign-number": "1", "first-name": "Ali", "last-name": "Abdullah", "date-added": "10-11-2012" }, { "assign-number": "2", "first-name": "Zohaib", "last-name": "Zafar", "date-added": "11-11-2012" } ] }
        data.data.forEach(item => {
            totalNumbers +=1;
            nameList.push(item["first-name"] + " " + item["last-name"]);
            assignedNumbers.push(item['assign-number'])
        })
    })
    .catch((error) => {
      console.error('Error:', error);
    });

    
  fetch(`${host}/getAdminConf/`)
  .then(response => response.json())
  .then(data => {
    imageUrl = data.background_image[0];
    let lastIndex = imageUrl.lastIndexOf(".");
    if (imageUrl != 'null' && imageUrl != 'undefined') {
      // Check whether the image provided is coming from static OR media
      if (!imageUrl.startsWith('/media/Background-Image')) 
      imageUrl = `${imageUrl.slice(0, lastIndex)} Large${imageUrl.slice(lastIndex)}`;
    } else {
      imageUrl = null;
    }
    const event_name = data.event_name
    const event_date = data.event_date
    const location = data.location
    const ads_banner_message = data.ads_banner_message
    const our_message = data.our_message
    const prize = data.prize
    const theme = data.theme[0].toLowerCase()
    const keypad_checked = data.keypad_checked[0]
    const barcode_checked = data.barcode_checked[0]
    const logo_image_path = data.logo_image_path || null;

    let themes;
    fetch('/static/themes.json')
    .then(response => response.json())
    .then(data => {
      themes = data;
        setTheme(themes, theme);
      })
      .catch((error) => {
        console.error('Error:', error);
      });

      // Grid Size Logic
      let grid_size = data.grid_size
      if (grid_size > nameList.length) {
        grid_size = nameList.length;
      }

      totalNumbers = grid_size;
      assignedNumbers = assignedNumbers.slice(0, grid_size)
      nameList = nameList.slice(0, grid_size);
      
      addBackground(imageUrl);
      if (keypad_checked != '') {
        grid = generateGrid(totalNumbers, assignedNumbers, true)
      } else {
        grid = generateGrid(totalNumbers, assignedNumbers, false)
      }
      container.appendChild(grid);

      if (barcode_checked) {
        document.addEventListener("keypress", qrCodeEliminator);
      }  

      document.getElementById('event-name').innerHTML = event_name
      document.getElementById('event-date').innerHTML = event_date
      document.getElementById('banner-text').innerHTML = ads_banner_message
      document.getElementById("winner-prize-name").innerHTML = prize;
      
      if (logo_image_path[0] != 'undefined') {
        document.getElementById("logo-image").setAttribute('src', '/media/Logo Uploaded.png')
      }

  })
  .catch((error) => {
    console.error('Error:', error);
  });

});

function setTheme(themes, themeName) {
  if (themes[themeName]) {
    let root = document.documentElement;
    let theme = themes[themeName];
    
    for (let color in theme) {
      let colorValue = theme[color].trim(); // Remove whitespace
      if (colorValue.endsWith(';')) {
        colorValue = colorValue.slice(0, -1); // Remove trailing semicolon
      }
      root.style.setProperty('--' + color, colorValue);
    }

  } else {
    console.error('Theme not found:', themeName);
  }
}

