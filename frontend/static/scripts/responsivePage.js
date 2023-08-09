window.addEventListener('resize', responsivePage);

function responsivePage() {

    try {
      
    var finalContainer = document.getElementById('final-container');
    var finalBorder = document.getElementById('final-border');
    var finalHeading = document.getElementById('final-heading');
    
    var parentWidth = finalContainer.offsetWidth; // Get the width of the parent element
    var parentHeight = finalContainer.offsetHeight; // Get the height of the parent element
    
    var relativeFontSize = Math.min(parentWidth / 8, parentHeight / 8); // Adjust the division factor (10) to achieve the desired font size
    
    finalHeading.style.fontSize = relativeFontSize + 'px';
    finalHeading.style.marginBottom = ((relativeFontSize * 10) / 100) + "px";
    finalHeading.style.marginTop = ((relativeFontSize * 50) / 100) + "px";
    
    var borderRadius = Math.min(parentWidth, parentHeight) / 10; // Adjust the division factor (10) to achieve the desired border radius
    
    finalContainer.style.borderRadius = borderRadius + 'px'; // Apply the calculated border radius to the child element
    finalBorder.style.borderRadius = borderRadius + 'px'; // Apply the calculated border radius to the child element

    var style = document.getElementById('head-style')
    
    // Add a new CSS rule for the '.final-heading' class
    style.sheet.insertRule('.final-number-container { font-size: ' + String((relativeFontSize * 30 )/ 100) + 'px; height: ' + String((relativeFontSize * 72 )/ 100) + 'px; width: ' + String((relativeFontSize * 72 )/ 100) + 'px; margin: ' + String((relativeFontSize * 10 )/ 100) + 'px ' + String((relativeFontSize * 24 )/ 100) + 'px; }', 0);
    style.sheet.insertRule('.final-name { font-size: ' + String((relativeFontSize * 38 )/ 100) + 'px; }', 0);
    style.sheet.insertRule('.final-10-grid-item { height: ' + String((relativeFontSize * 72 )/ 100) + 'px; }', 0);
    style.sheet.insertRule('.final-10-grid { grid-gap:' + String((relativeFontSize * 12)/ 100) + 'px; }', 0);
    style.sheet.insertRule('.sidebar-logo { margin-top:' + String((relativeFontSize * 20)/ 100) + 'px; height: ' + String((relativeFontSize * 200)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.outer-ball { height: calc(' + String((relativeFontSize * 750)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 750)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.popup-outer-ball { height: calc(' + String((relativeFontSize * 750)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 750)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.ball-gradient-border { height: calc(' + String((relativeFontSize * 650)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 650)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.popup-ball-gradient-border { height: calc(' + String((relativeFontSize * 640)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 640)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.inner-ball { height: calc(' + String((relativeFontSize * 625)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 625)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.popup-inner-ball { height: calc(' + String((relativeFontSize * 625)/ 100) + 'px * var(--ball-size)); width: calc(' + String((relativeFontSize * 625)/ 100) + 'px * var(--ball-size)); }', 0)
    style.sheet.insertRule('.last-elimination { font-size: ' + String((relativeFontSize * 44)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.tickets-drawn, .tickets-undrawn { max-width: ' + String((relativeFontSize * 170)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.tickets-drawn > .heading, .tickets-undrawn > .heading { font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.tickets-drawn > .ticket-number, .tickets-undrawn > .ticket-number { font-size: ' + String((relativeFontSize * 60)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.recent-drawn-tickets > .ticket-number { font-size: ' + String((relativeFontSize * 70)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.recent-drawn-tickets { height: ' + String((relativeFontSize * 500)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.recent-drawn-numbers { height: ' + String((relativeFontSize * 400)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.recent-drawn-tickets > .heading { font-size: ' + String((relativeFontSize * 38)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.line { height: ' + String((relativeFontSize * 200)/ 100) + 'px; margin-right: ' + String((relativeFontSize * 10)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.number-panel-grid-item { font-size: ' + String((relativeFontSize * 42)/ 100) + 'px; height: ' + String((relativeFontSize * 80)/ 100) + 'px;}', 0)
    style.sheet.insertRule('.elimination-text { font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.elimination-heading { font-size: ' + String((relativeFontSize * 50)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.elimination-number { font-size: ' + String((relativeFontSize * 250)/ 100) + 'px;   line-height:' + String((relativeFontSize * 220)/ 100) + 'px;}', 0)
    style.sheet.insertRule('.final-border, .final-container { border-radius: ' + String(borderRadius) + 'px;   }', 0)
    style.sheet.insertRule('.back-text { font-size: ' + String((relativeFontSize * 80)/ 100) + 'px; line-height: ' + String((relativeFontSize * 80)/ 100) + 'px;}', 0)
    style.sheet.insertRule('.back-heading { font-size: ' + String((relativeFontSize * 110)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.sidebar-ball { font-size: ' + String((relativeFontSize * 125)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.event-name { font-size: ' + String((relativeFontSize * 60)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.event-date { font-size: ' + String((relativeFontSize * 40)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.event-info > .last-eliminated { font-size: ' + String((relativeFontSize * 65)/ 100) + 'px;  line-height: ' + String((relativeFontSize * 5)/ 100) + 'px;}', 0)  
    style.sheet.insertRule('.banner-text { font-size: ' + String((relativeFontSize * 40 ) /100) + 'px; }', 0)
    style.sheet.insertRule('.winner-message { font-size: ' + String((relativeFontSize * 160 ) /100) + 'px; line-height: ' + String((relativeFontSize * 85)/ 100) + 'px; }', 0)
    style.sheet.insertRule('.winner-congratulations { font-size: ' + String((relativeFontSize * 60 ) /100) + 'px; }', 0)
    style.sheet.insertRule('.winner-number-ball { font-size: ' + String((relativeFontSize * 60 ) /100) + 'px;  height: ' + String((relativeFontSize * 180)/ 100) + 'px; width: ' + String((relativeFontSize * 180)/ 100) + 'px;}', 0)
    style.sheet.insertRule('.winner-name { font-size: ' + String((relativeFontSize * 80 ) /100) + 'px; }', 0)
    style.sheet.insertRule('.winner-prize { font-size: ' + String((relativeFontSize * 40 ) /100) + 'px; }', 0)
    style.sheet.insertRule('.winner-prize-name { font-size: ' + String((relativeFontSize * 40 ) /100) + 'px; }', 0)
    style.sheet.insertRule('.up-arrow, .down-arrow { height: ' + String((relativeFontSize * 60)/ 100) + 'px !important; width: ' + String((relativeFontSize * 60)/ 100) + 'px !important;}', 0);
    style.sheet.insertRule('.up-arrow > object, .down-arrow > object { height: ' + String((relativeFontSize * 25)/ 100) + 'px !important; }', 0);
    style.sheet.insertRule('#grid-size-selector { height: ' + String((relativeFontSize * 90)/ 100) + 'px; font-size: ' + String((relativeFontSize * 35)/ 100) + 'px; }', 0);
  
  } catch (error) {
    console.log(error)      
  }


  }
responsivePage();