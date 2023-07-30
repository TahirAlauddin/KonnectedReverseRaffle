document.addEventListener("DOMContentLoaded", () => {

    // URL of the image used as background
    const imageUrl = "/static/images/Rectangle 7.png";
  
    // Function to add background to the panel
    const addBackground = (imageUrl) => {
      document.getElementById("number-panel-grid").style.background = `url("${imageUrl}") no-repeat cover`;
    };
  
    // Grid data for the final 10 numbers
    const gridData = [
      { number: 1, name: "Alan Alan Alan" },
      { number: 2, name: "Bob Bob Bob" },
      { number: 3, name: "Charlie Charlie" },
      { number: 4, name: "David David David" },
      { number: 5, name: "Eve Eve Eve Eve" },
      { number: 6, name: "Frank Frank Frank" },
      { number: 7, name: "Grace Grace Grace" },
      { number: 8, name: "Hank Hank Hank" },
      { number: 9, name: "Ivy Ivy Ivy Ivy" },
      { number: 10, name: "Jack Jack Jack" },
    ];
  
    // Definitions of grid size based on the total number of items
    const gridSizeDefinitions = [
      { max: 50, columns: 9, className: "very-large-grid" },
      { max: 100, columns: 12, className: "large-grid" },
      { max: 150, columns: 14, className: "medium-grid" },
      { max: 200, columns: 16, className: "small-grid" },
      { max: 250, columns: 18, className: "very-small-grid" },
      { max: 300, columns: 20, className: "extremely-small-grid" },
    ];
  
    // Other definitions used across the file
    let barCodeNumber = '';
    let totalNumbers = 0;
    let numberList = [];
    let nameList = [];
    let timer;
  
    // Fetch data from CSV file and generate the grid
    fetch('http://localhost:8000/getCSVData/')
      .then(response => response.json())
      .then(data => {
          data.data.forEach(item => {
              totalNumbers +=1;
              nameList.push(item["first-name"] + " " + item["last-name"]);
          })
          const grid = generateGrid(totalNumbers)
          document.getElementById("number-panel-grid").appendChild(grid);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  
    // Functions related to the management of the grid
    const generateGrid = (totalNumbers) => {
      let columns, className;
      for (let sizeDefinition of gridSizeDefinitions) {
        if (totalNumbers <= sizeDefinition.max) {
          columns = sizeDefinition.columns;
          className = sizeDefinition.className;
          break;
        }
      }
  
      const grid = document.createElement("div");
      grid.className = className;
      

    // ... grid generation logic here
    // ... grid generation logic here
    // ... grid generation logic here
    // ... grid generation logic here
    // ... grid generation logic here
    // ... grid generation logic here
    // ... grid generation logic here

    for (let i = 0; i < totalNumbers; i++) {
        const numberPanelGridItem = document.createElement("div");
        numberPanelGridItem.classList.add("number-panel-grid-item");
        numberPanelGridItem.textContent = i + 1;
        numberPanelGridItem.addEventListener('click', removeClassClickListener(numberPanelGridItem, i + 1));
        numberPanelGridItem.addEventListener('contextmenu', hideItemClickListener(numberPanelGridItem, i + 1));
        numberPanelGridItem.addEventListener('dblclick', showItemClickListener(numberPanelGridItem, i + 1));
        grid.appendChild(numberPanelGridItem);
      }
  
      return grid;
    };
  
    const removeClassClickListener = (item, number) => (event) => {
      item.classList.remove("number-panel-grid-item-clicked");
      getNumberBack(number);
    };
  
    const hideItemClickListener = (item, number) => (event) => {
      item.style.opacity = 0;
      removeNumberFromPanel(number);
  
      if (totalNumbers - 10 === numberList.length) {
        generateFinalGrid();
      }
    };
  
    const showItemClickListener = (item, number) => (event) => {
      item.style.opacity = 1;
      removeNumberFromPanel(number);
    };
  
    // Functions related to the management of the numbers
  
    const removeNumberFromPanel = (number) => {
      if (!numberList.includes(number)) {
        numberList.unshift(number);
      }
      const hiddenContainer = document.getElementById("elimination-ball");
      setEliminationText();
      setLastEliminatedText();
      setLastEliminatedHeader();
      setRecentDrawnTickets(numberList);
      setTicketsNumber();
      resetContainer(hiddenContainer);
    };
  
    const getNumberBack = (number) => {
      setBackInText(number);
      const index = numberList.indexOf(number);
      if (index !== -1) {
        numberList.splice(index, 1);
      }
      setLastEliminatedHeader();
      setLastEliminatedText();
      setTicketsNumber();
      const hiddenContainer = document.getElementById("back-container");
      resetContainer(hiddenContainer);
    };
  
    // Other utility functions
    
    function resetContainer(hiddenContainer) {
        clearTimeout(timer);
        showContainer(hiddenContainer);
    
        var overlay = document.createElement("div");
        pandelGrid = document.getElementById("number-panel-grid");
        var rect = pandelGrid.getBoundingClientRect();
        overlay.id = "modal-overlay";
        overlay.style.position = "fixed";
        overlay.style.backdropFilter = "blur(10px)";
        overlay.style.top = String(rect.top - 5) + "px";
        overlay.style.left = String(rect.left - 5) + "px";
        overlay.style.width = String(pandelGrid.offsetWidth + 10) + "px";
        overlay.style.height = String(pandelGrid.offsetHeight + 10) + "px";
        console.log(pandelGrid.offsetWidth, pandelGrid.offsetHeight)
        overlay.style.zIndex = "998"; // should be less than the z-index of the hiddenContainer
        pandelGrid.appendChild(overlay);
    
        overlay.addEventListener("click", function () {
          revertContainer(hiddenContainer);
          document.getElementById("number-panel-grid").removeChild(overlay);
        });
    
        timer = setTimeout(function () {
          hideContainer(hiddenContainer);
          if (document.body.contains(overlay)) {
            document.getElementById("number-panel-grid").removeChild(overlay);
          }
        }, 4000);
      }
  
    // To be continued in the next part
      // To be continued from the previous part
      // To be continued from the previous part
      // To be continued from the previous part
  
  const setRecentDrawnTickets = (list) => {
    console.log(list);
    const ticketNumbers = document.querySelectorAll(".recent-drawn-tickets .ticket-number");

    // Remove old ticket numbers
    ticketNumbers.forEach((ticket) => ticket.remove());

    // Create new ticket numbers
    list.forEach((ticketNumber) => {
      const ticketParagraph = document.createElement("p");
      ticketParagraph.className = "ticket-number uncopiable";
      ticketParagraph.textContent = ticketNumber;
      document.querySelector(".recent-drawn-tickets").appendChild(ticketParagraph);
    });
  };
  // Function to display the number that has been added back to the pool
  const setBackInText = (number) => {
    // Fetch the element in which the number to be added back is displayed
    const element = document.getElementById("back-number");
    // If there are numbers in the list, display the last number that was added back
    if (numberList.length > 0) {
      element.textContent = number;
    }
  };

  // Function to display the last number that was eliminated
  const setEliminationText = () => {
    // Fetch the element in which the last eliminated number is displayed
    const element = document.getElementById("elimination-number");
    // If there are numbers in the list, display the last eliminated number
    if (numberList.length > 0) {
      element.textContent = numberList[0];
    }
  };

  // Function to display the last eliminated number (or "-" if no numbers were eliminated yet)
  const setLastEliminatedText = () => {
    // Fetch the element in which the last eliminated number is displayed
    const element = document.getElementById("last-eliminated");
    // Display the last eliminated number or "-" if there were no numbers eliminated yet
    element.textContent = numberList.length > 0 ? numberList[0] : "-";
  };

  // Function to display the current count of drawn and undrawn tickets
  const setTicketsNumber = () => {
    // Fetch the elements in which the counts are displayed
    const drawnTickets = document.getElementById("drawn-tickets-number");
    const unDrawnTickets = document.getElementById("undrawn-tickets-number");

    // Display the counts
    drawnTickets.textContent = numberList.length;
    unDrawnTickets.textContent = totalNumbers - numberList.length;
  };

  // Function to display the header for the last eliminated number
  const setLastEliminatedHeader = () => {
    // Initialize placeholders for the last eliminated number and name
    let lastEliminatedNum = "";
    let lastEliminatedName = "";
    // If there are numbers in the list, fetch the last eliminated number and the corresponding name
    if (numberList.length > 0) {
      lastEliminatedNum = numberList[0];
      lastEliminatedName = nameList[lastEliminatedNum - 1];
    }
    // Fetch the header element
    const lastEliminatedHeader = document.getElementById("last-eliminated-header");
    // Display the header
    lastEliminatedHeader.textContent = `#${lastEliminatedNum} - ${lastEliminatedName}`;
  };

  // Function to display the name of the event
  const setEventInfoName = (name) => {
    // Fetch the element in which the name is displayed
    const eventName = document.getElementById("event-name");
    // Display the name
    eventName.textContent = name;
  };

  // Function to display the date of the event
  const setEventInfoDate = (date) => {
    // Fetch the element in which the date is displayed
    const eventDate = document.getElementById("event-date");
    // Display the date
    eventDate.textContent = date;                      
  };

  // Calling these functions would depend on your UI logic.
  // You might want to call them as soon as the page loads, or as a result of user interactions.
  // Example usage:
  setEventInfoName("Your Event Name");
  setEventInfoDate("Your Event Date");

  // End of the code
})