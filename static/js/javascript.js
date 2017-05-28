$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
  });
$(document).ready(function(){
    $('.modal').modal();
    $(".button-collapse").sideNav();
    $('select').material_select();
  });
