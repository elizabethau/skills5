"use strict";

function showHuman(evt) {

 evt.preventDefault();

 const selectedId = $('#human-id').val();

 let formData = {
    "human_id": selectedId

 };
 // alert(selectedId);
 // $('dd').html('Jesus');
 // $('dd').html(selectedId);
 $.get("/api/human/" + selectedId, (response) => {
    $('#fname').html(response.fname);
 });

 $.get("/api/human/" + selectedId, (response) => {
    $('#lname').html(response.lname);
 });

 $.get("/api/human/" + selectedId, (response) => {
    $('#email').html(response.email);
 });

}

$('#get-human').on('submit', showHuman);
