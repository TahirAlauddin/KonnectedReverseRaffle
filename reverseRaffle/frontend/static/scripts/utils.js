
export function setRecentDrawnTickets(list) {
    var ticketNumbers = document.querySelectorAll(
      ".recent-drawn-tickets .ticket-number"
    );

    // Remove old ticket numbers
    ticketNumbers.forEach((ticket) => ticket.remove());

    // Create new ticket numbers
    list.forEach((_, index) => {
      var ticketParagraph = document.createElement("p");
      ticketParagraph.className = "ticket-number uncopiable";
      ticketParagraph.textContent = list[index];
      document
        .querySelector(".recent-drawn-tickets")
        .appendChild(ticketParagraph);
    });
}

export function setBackInText(number, numberList) {
    var element = document.getElementById("back-number"); // replace with the actual id of your element
    console.log(numberList)
    if (numberList.length > 0) {
      element.textContent = number;
    }
}

export function setEliminationText(numberList) {
    var element = document.getElementById("elimination-number"); // replace with the actual id of your element
    if (numberList.length > 0) {
        element.textContent = numberList[0];
    }
}

export function setEventInfoName(name) {
    var eventName = document.getElementById("event-name");
    eventName.textContent = name;
}

export function setEventInfoDate(date) {
    var eventDate = document.getElementById("event-date");
    eventDate.textContent = date;
}

export function addBackground(imageUrl) {
    document.getElementById("number-panel-grid").setAttribute('style', `background-image: url("${imageUrl}"); background-repeat: no-repeat; background-size: cover;`);
}
