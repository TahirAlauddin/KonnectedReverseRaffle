let validated = false;
let table = document.getElementById("table");
table.setAttribute('contenteditable', true);
let selectedRow = null;

let host = 'http://localhost:8323';

// Table Functions
function addRow() {
  let row = document.createElement("tr");
  
  // Select the table and add an event listener to each row
  row.onclick = function() {
    // Record the selected row
    selectedRow = this;  
  };

  for (let j = 0; j < 4; j++) {
    let cell = document.createElement("td");
    if (j === 0) {
      cell.classList.add("first-column");
    }
    cell.textContent = "..."
    row.appendChild(cell);
  }
    let cell = document.createElement("td");
    cell.setAttribute("contenteditable", "false");
    let button = document.createElement("button");
    button.textContent = "X";
    button.onclick = deleteRow;
    button.className = "delete-row-table";
    cell.appendChild(button);
    row.appendChild(cell);
    table.appendChild(row);

}

function deleteRow() {
  console.log(selectedRow);
  console.log(table);
  table.removeChild(selectedRow);
  selectedRow = null;
}

// Function for showing message
function showMessage(message, type) {
  var popup = document.getElementById('message-popup');
  var popupContent = document.getElementById('popup-content');
  var closeBtn = document.getElementById('close-btn');
  var popupMessage = document.getElementById('popup-message');
  
  if (type == 'success') {
    popupContent.style.backgroundColor = "#4CAF50"
    popupContent.style.color = "white"
    popupContent.style.borderColor = "#388E3C"
    closeBtn.style.backgroundColor = "#388E3C"
  } else {
    popupContent.style.backgroundColor = "#ff4f5a"
    popupContent.style.color = "white"
    popupContent.style.borderColor = "#b22234"
    closeBtn.style.backgroundColor = "#b22234"
  }

  popupMessage.textContent = message;
  popup.classList.remove('hidden');
  popup.classList.add('visible');
  
  closeBtn.onclick = function() {
    popup.classList.remove('visible');
    popup.classList.add('hidden');
  };
  
  function onEscapeKeyPressed(event) {
    if (event.key === 'Escape' || event.keyCode === 27) {
      popup.classList.remove('visible');
      popup.classList.add('hidden');
      // Remove the listener once the Escape key is pressed
      document.removeEventListener('keydown', onEscapeKeyPressed);
    }
  }
  // Add the listener
  document.addEventListener('keydown', onEscapeKeyPressed);
}
// Functions for changing gridsize
function increment() {
  document.getElementById("grid-size-selector").stepUp();
}

function decrement() {
  document.getElementById("grid-size-selector").stepDown();
}

// Functions for changing themes
const themes = ["Black", "Pink", "Purple", "Yellow", "Aqua", "Sunset", "Flower", "Industrial", "Midnight"];
let currentThemeIndex = 0;
let participantsDataSaved = false;

const themeSelector = document.getElementById("theme-selector");

function incrementTheme() {
  currentThemeIndex = (currentThemeIndex + 1) % themes.length;
  updateTheme();
}

function decrementTheme() {
  currentThemeIndex = (currentThemeIndex - 1 + themes.length) % themes.length;
  updateTheme();
}

function updateTheme() {
  const selectedTheme = themes[currentThemeIndex];
  themeSelector.value = selectedTheme;
  document.body.className = selectedTheme.toLowerCase() + "-theme";
}

updateTheme();

// Functions to add image to grid
document.getElementById("add-image").addEventListener("click", function () {
  document.getElementById("image-upload").click();
  
});

document.getElementById("image-upload").addEventListener("change", function () {
  if (this.files && this.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      var div = document.createElement("div");
      div.className = "image-grid-item";
      var img = document.createElement("img");
      img.src = e.target.result;
      div.appendChild(img);
      img.addEventListener("click", function(event) {
        // if there is a previously selected image, remove its class
        if (selectedImg || selectedImg == event.target) {
          selectedImg.classList.remove('selected-image');
          selectedImg = null;
          selectedImgPath = null;
        }
        else {
          // add class to the clicked image and update selectedImg
          event.target.classList.add('selected-image');
          selectedImg = event.target;
          selectedImgPath = selectedImg.getAttribute('data-path');
        }
      });
      document.getElementById("images-grid").appendChild(div);
      
      // Making a POST request to save the image data
      fetch(`${host}/saveImage/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          image: e.target.result,
        }),
      })
      .then(response => response.json())
      .then(data => {
        console.log("Image saved successfully!", data);
        // Extracting just the file name (e.g., "abc.png")
        var fileName = data.file_path.split('\\').pop();
        console.log(fileName)
        // Constructing the new path
        var mediaUrl = "/media/" + fileName;
        img.setAttribute('data-path', mediaUrl);
      })
      .catch(error => {
        console.error("Error saving image:", error);
      });
    };
    reader.readAsDataURL(this.files[0]);
  }
});

var selectedImg = null; // global variable to keep track of the selected image tag
var selectedImgPath = null; // image path

function uploadImages() {
  var imgURLs = [
    '\\static\\images\\Rectangle 1.jpg',
    '\\static\\images\\Rectangle 2.jpg',
    '\\static\\images\\Rectangle 3.jpg',
    '\\static\\images\\Rectangle 4.jpg',
    '\\static\\images\\Rectangle 5.jpg',
    '\\static\\images\\Rectangle 6.jpg',
    '\\static\\images\\Rectangle 7.jpg',
  ];

  for (var i = 0; i < imgURLs.length; i++) {
    var div = document.createElement("div");
    div.className = "image-grid-item";
    var img = document.createElement("img");
    img.src = imgURLs[i];
    
    div.addEventListener("click", function(event) {
      // if there is a previously selected image, remove its class
      if (selectedImg || selectedImg == event.target) {
        selectedImg.classList.remove('selected-image');
        selectedImg = null;
        selectedImgPath = null;
      }
      else {
        // add class to the clicked image and update selectedImg
        event.target.classList.add('selected-image');
        selectedImg = event.target;
        selectedImgPath = selectedImg.src;
      }
    });

    div.appendChild(img);
    document.getElementById("images-grid").appendChild(div);
  }
}

uploadImages();

// Functions to upload CSV
function uploadCSV() {
  let fileInput = document.getElementById("csv-input");
  fileInput.click();

  // Create a Promise that resolves when the file is selected
  const fileSelectedPromise = new Promise((resolve) => {
    fileInput.addEventListener(
      "change",
      () => {
        resolve(fileInput.files[0]);
      },
      { once: true }
    );
  });

  fileSelectedPromise.then((file) => {
    let reader = new FileReader();

    reader.onload = function (event) {
      let data = event.target.result;

      // Parse CSV
      let rows = data.split("\n");
      let headers = rows[0].split(",");

      let table = document.getElementById("table");

      let arr = [
        "assign-number",
        "first-name",
        "last-name",
        "date-added",
        "blank-head",
      ];
      let row = document.createElement("tr");      
      // Select the table and add an event listener to each row
      row.onclick = function() {
        // Record the selected row
        selectedRow = this;  
      };

      for (let i = 0; i < rows.length; i++) {
        let row = document.createElement("tr");
        let cells = rows[i].split(",");
        
        // Remove any extra lines or rows with less than 4 cells
        if (cells.length < 4) {
          continue
        }

        for (let j = 0; j < cells.length; j++) {
          let cell = document.createElement("td");
          if (j === 0) {
            cell.classList.add("first-column");
          }
          cell.textContent = cells[j];
          row.appendChild(cell);
        }
        let cell = document.createElement("td");
        cell.setAttribute("contenteditable", "false");
        let button = document.createElement("button");
        button.textContent = "X";
        button.onclick = function () {
          selectedRow = row;
          deleteRow();
        }
        button.className = "delete-row-table";
        cell.appendChild(button);
        row.appendChild(cell);
        
        table.appendChild(row);
      }
    };
    reader.readAsText(file);
});
}

// Functions to handle sidebar buttons
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("license-activation").style.display = "none";
  document.getElementById("user-list-container").style.display = "none";
  document
    .getElementById("sidebar-dashboard-button")
    .classList.add("active-menu");
  document.getElementById("menu-grid").style.display = "grid";
});

document
  .getElementById("sidebar-dashboard-button")
  .addEventListener("click", function () {
    this.classList.add("active-menu");
    btn1 = document.getElementById("sidebar-user-list-button");
    btn2 = document.getElementById("sidebar-license-button");

    btn1.classList.remove("active-menu");
    btn2.classList.remove("active-menu");
    document.getElementById("menu-grid").style.display = "grid";
    document.getElementById("license-activation").style.display = "none";
    document.getElementById("user-list-container").style.display = "none";
  });

document
  .getElementById("sidebar-user-list-button")
  .addEventListener("click", function () {
    this.classList.add("active-menu");
    btn1 = document.getElementById("sidebar-dashboard-button");
    btn2 = document.getElementById("sidebar-license-button");

    btn1.classList.remove("active-menu");
    btn2.classList.remove("active-menu");
    document.getElementById("menu-grid").style.display = "none";
    document.getElementById("license-activation").style.display = "none";
    document.getElementById("user-list-container").style.display = "flex";
  });

document
  .getElementById("sidebar-license-button")
  .addEventListener("click", function () {
    this.classList.add("active-menu");
    btn1 = document.getElementById("sidebar-dashboard-button");
    btn2 = document.getElementById("sidebar-user-list-button");

    btn1.classList.remove("active-menu");
    btn2.classList.remove("active-menu");
    document.getElementById("menu-grid").style.display = "none";
    document.getElementById("license-activation").style.display = "flex";
    document.getElementById("user-list-container").style.display = "none";
  });

// Functions to upload Logo
function uploadLogo() {
  const fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.accept = "image/*";

  fileInput.addEventListener("cancel", () => {
    // Remove the file input element if the selection is canceled
    fileInput.remove();
  });

  fileInput.addEventListener("change", () => {
    fileInput.remove();

    const file = fileInput.files[0];

    // Display selected logo
    displayImage(file, "upload-logo-container", "upload-logo-image", "Logo");

    fileInput.remove();
  });

  fileInput.click();
}

// Functions to Upload Prize Image
function uploadPrizeImage() {
  const fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.accept = "image/*";

  fileInput.addEventListener("cancel", () => {
    // Remove the file input element if the selection is canceled
    fileInput.remove();
  });

  fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];

    // Display selected prize image
    displayImage(file, "upload-prize-image-container", "upload-prize-image-image", "Prize Image");

    fileInput.remove();
  });

  fileInput.click();
}

document.getElementById("upload-logo").addEventListener("click", uploadLogo);

document
  .getElementById("upload-prize-image")
  .addEventListener("click", uploadPrizeImage);

function displayImage(file, containerId, imageId, headingText) {
  const container = document.getElementById(containerId);
  // Add heading
  const heading = document.createElement("h3");
  heading.textContent = headingText;
  if (!container.querySelector('h3')) {
    container.prepend(heading);
  }

  if (file) {
    const image = document.getElementById(imageId)
    image.src = URL.createObjectURL(file);
    
    let reader = new FileReader();

    reader.onload = function(event) {
        let dataUrl = event.target.result;

        fetch('/saveImage/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: dataUrl, image_name: headingText})
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
          console.error('Error:', error);
        });
    };

    reader.readAsDataURL(file);

    // image.width = 200; // Set desired width
    // image.height = 200; // Set desired height
  }

  if (headingText == "Prize Image") {
    document
      .getElementById("upload-prize-image")
      .addEventListener("click", uploadPrizeImage);
  } else if (headingText == "Logo") {
    document
      .getElementById("upload-logo")
      .addEventListener("click", uploadLogo);
  }
}

// Functions to manage checkboxes
document
  .getElementById("keypad-check-box")
  .addEventListener("click", function () {
    if (this.textContent === "\u2713") {
      this.textContent = "";
    } else {
      this.textContent = "\u2713";
    }
  });

document
  .getElementById("barcode-check-box")
  .addEventListener("click", function () {
    if (this.textContent === "\u2713") {
      this.textContent = "";
    } else {
      this.textContent = "\u2713";
    }
  });


document.getElementById('run-button').addEventListener('click', function () {
  let event_name = document.getElementById('event-name-input').value
  let event_date = document.getElementById('date-input').value
  let ads_banner_message = document.getElementById('ads-banner-message-input').value
  let prize = document.getElementById('prize-input').value
  let theme = document.getElementById('theme-selector').value
  let keypad_checked = document.getElementById('keypad-check-box').innerHTML
  let barcode_checked = document.getElementById('barcode-check-box').innerHTML
  let location = document.getElementById('location-input').value
  let our_message = document.getElementById('our-message-input').value
  let prize_image_path = document.getElementById('upload-prize-image-image').src
  let logo_image_path = document.getElementById('upload-logo-image').src;
  let grid_size = document.getElementById('grid-size-selector').value;

  if (logo_image_path == [undefined]) {
    logo_image_path = undefined
  }
  
  function validateInputs() {
    var variables = [event_name, event_date, ads_banner_message, prize, theme];
    var variableNames = ["Event Name", "Event Date", "ads_banner_message", "prize", "theme"];
    
    for(var i = 0; i < variables.length; i++) {
      if(variables[i] === null || variables[i] === '') {
        showMessage('Please make sure ' + variableNames[i] + ' input is entered', 'error');
        return false; 
      }
    }
    if (!(prize_image_path)) {
      showMessage('Please make sure the prize image is provided!', 'error')
      return false; 
    }
    if (! (barcode_checked || keypad_checked)) {
      showMessage('Please make sure either keypad or barcode is checked.', 'error');
      return false; 
    }
    if (!participantsDataSaved) {
      showMessage('Please provide participants information in Users List Page.', 'error');
      return false;
    }
      
    return true;

  }  

  if (validated) {
    // Call the validation function
      if (validateInputs()) {
        window.location.href = `/home?background_image=${selectedImgPath}&event_name=${event_name}
    &event_date=${event_date}&location=${location}&ads_banner_message=${ads_banner_message}
    &our_message=${our_message}&prize=${prize}&theme=${theme}&keypad_checked=${keypad_checked}
    &barcode_checked=${barcode_checked}&grid_size=${grid_size}&logo_image_path=${logo_image_path}`
      }
  } else {
    showMessage('License Key is Required!', 'error')
  }
  
})

function downloadTableAsCSV() {
  let table = document.getElementById('table');
  // Make the table editable
  let rows = Array.from(table.querySelectorAll('tr'));
  let csvContent = '';

  for (let row of rows) {
      let cols = Array.from(row.querySelectorAll('td, th'));
      let values = cols.map(col => `"${col.textContent}"`); // Quote each cell to handle commas within cells
      csvContent += values.join(',') + '\n'; // Join each row's values by commas
  }

  // Create a Blob object from the CSV string
  let blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

  // Create a URL for blob
  let url = URL.createObjectURL(blob);

  // Create a download link
  let link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", "participants.csv");

  // This part will force click on the link
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Add an event listener to the button
document.getElementById('download-csv-button').addEventListener('click', downloadTableAsCSV);

document.getElementById('exit-button').addEventListener('click', function () {

  let table = document.getElementById('table');
  // Make the table editable
  let rows = Array.from(table.querySelectorAll('tr'));
  let csvContent = '';

  for (let row of rows) {
      let cols = Array.from(row.querySelectorAll('td, th'));
      let values = cols.map(col => `"${col.textContent}"`); // Quote each cell to handle commas within cells
      csvContent += values.join(',') + '\n'; // Join each row's values by commas
  }
  // POST CSV data to the server
  fetch(`${host}/saveCSVData/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(csvContent),
  })
  .then(response => response.json())
  .then(data => {
    participantsDataSaved = true;
    if (data.success) {
      showMessage("Participants Data saved!", "success");
    } else {
      showMessage(data.error, "error");
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
})

document.getElementById('license-button').addEventListener('click', function () {
  license_key = document.getElementById('input-license').value
  
  if (!license_key) {
    return;
  }
  // POST CSV data to the server
  fetch(`${host}/validateLicenseKey/${license_key}`, {
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log(data)
      validated = true;
      showMessage("License Key Validated successfully!", "success");
    } else {
      showMessage(data.error, "error");
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
} )

// Add an initial Row
addRow()


// Make sure license key is validated
fetch(`${host}/licenseKeyIsValid/`, {
  method: 'GET',
  headers: {
  'Content-Type': 'application/json',
  }
})
.then(response => response.json())
.then(data => {
  if (data.success) {
    validated = true;
  }
})
.catch((error) => {
  console.error('Error:', error);
});


document.getElementById('grid-size-selector').addEventListener('change', function (event) {
  let inputValue = parseInt(event.target.value);

  if (inputValue > 300) {
      event.target.value = 300;
  } else if (inputValue < 50) {
      event.target.value = 50;
  }
  console.log(event.target.value);
});
