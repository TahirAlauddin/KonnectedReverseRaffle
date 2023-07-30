window.addEventListener('resize', responsivePage);

function responsivePage() {
  finalContainer = document.querySelector("body");
  var parentWidth = finalContainer.offsetWidth;
  var parentHeight = finalContainer.offsetHeight;

  var relativeFontSize = Math.min(parentWidth / 18, parentHeight / 18);

  var style = document.createElement('style');
  document.head.appendChild(style);

  style.sheet.insertRule('body { font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; }', 0)

  style.sheet.insertRule('.sidebar-logo { height: ' + String((relativeFontSize * 180)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.admin-profile { height: ' + String((relativeFontSize * 70)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.sidebar-button, .admin-profile { height: ' + String((relativeFontSize * 130)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.upload-prize-image, .upload-logo { height: ' + String((relativeFontSize * 550)/ 100) + 'px; }', 0);
  style.sheet.insertRule('#grid-size-selector { height: ' + String((relativeFontSize * 90)/ 100) + 'px; font-size: ' + String((relativeFontSize * 35)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.run-button { height: ' + String((relativeFontSize * 90)/ 100) + 'px; font-size: ' + String((relativeFontSize * 25)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.up-arrow, .down-arrow { height: ' + String((relativeFontSize * 60)/ 100) + 'px !important; width: ' + String((relativeFontSize * 60)/ 100) + 'px !important;}', 0);
  style.sheet.insertRule('.up-arrow > object, .down-arrow > object { height: ' + String((relativeFontSize * 25)/ 100) + 'px !important; }', 0);
  style.sheet.insertRule('.form-group > input { height: ' + String((relativeFontSize * 70)/ 100) + 'px; font-size: ' + String((relativeFontSize * 25)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.form-group { margin-bottom: ' + String((relativeFontSize * 5)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.form-group > label { margin-right: ' + String((relativeFontSize * 25)/ 100) + 'px; width: ' + String((relativeFontSize * 300)/ 100) + 'px; font-size: ' + String((relativeFontSize * 30)/ 100) + 'px}', 0);
  style.sheet.insertRule('.inputs-container > * { font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.check-box { width: ' + String((relativeFontSize * 45)/ 100) + 'px; height: ' + String((relativeFontSize * 35)/ 100) + 'px; border: ' + String((relativeFontSize * 5)/ 100) + 'px solid white; }', 0);
  style.sheet.insertRule('.entry { width: ' + String((relativeFontSize * 500)/ 100) + 'px; }', 0);
  style.sheet.insertRule('#theme-selector { height: ' + String((relativeFontSize * 90)/ 100) + 'px; font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; width: ' + String((relativeFontSize * 450)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.add-image-button { height: ' + String((relativeFontSize * 90)/ 100) + 'px; font-size: ' + String((relativeFontSize * 25)/ 100) + 'px; width: ' + String((relativeFontSize * 400)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.circle { height: ' + String((relativeFontSize * 50)/ 100) + 'px; font-size: ' + String((relativeFontSize * 50)/ 100) + 'px; width: ' + String((relativeFontSize * 50)/ 100) + 'px; }', 0);
  style.sheet.insertRule('.image-grid-item { height: ' + String((relativeFontSize * 350)/ 100) + 'px; width: ' + String((relativeFontSize * 200)/ 100) + 'px; }', 0);
  style.sheet.insertRule('#input-license { height: ' + String((relativeFontSize * 130)/ 100) + 'px; font-size: ' + String((relativeFontSize * 45)/ 100) + 'px; border-radius: ' + String((relativeFontSize * 35)/ 100) + 'px;}', 0);
  style.sheet.insertRule('.activation-text { font-size: ' + String((relativeFontSize * 70)/ 100) + 'px; }', 0)
  style.sheet.insertRule('.activation-para { font-size: ' + String((relativeFontSize * 40)/ 100) + 'px; }', 0)
  style.sheet.insertRule('.license-button { font-size: ' + String((relativeFontSize * 30)/ 100) + 'px; border-radius: ' + String((relativeFontSize * 50)/ 100) + 'px; width: ' + String((relativeFontSize * 450)/ 100) + 'px; height: ' + String((relativeFontSize * 100)/ 100) + 'px; }', 0)
  style.sheet.insertRule('.user-list-heading { font-size: ' + String((relativeFontSize * 80)/ 100) + 'px; }', 0)
  style.sheet.insertRule('.user-button { font-size: ' + String((relativeFontSize * 40)/ 100) + 'px; height: ' + String((relativeFontSize * 100)/ 100) + 'px; width: ' + String((relativeFontSize * 450)/ 100) + 'px; }', 0)
  style.sheet.insertRule('.user-list { height: ' + String((relativeFontSize * 1300)/ 100) + 'px; }', 0);  
}

responsivePage();