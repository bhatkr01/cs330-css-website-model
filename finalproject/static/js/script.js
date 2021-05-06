
/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

const BASE_URL ="http://bhatkr01.pythonanywhere.com/user";

async function getData(){
    var dataList= await fetch(`${BASE_URL}`)
    .then(response => response.json());
    document.getElementById("student_data").style.display = 'block';
    document.querySelector("#student_data>#real_table>tbody").innerHTML="";
    var newList;
    for (let data in dataList){
        newList=dataList[data]
        for (let index of newList){
            let row=document.createElement("tr");
            let td1=document.createElement("td");
            let td2=document.createElement("td");
            td1.innerHTML=index.name
            td2.innerHTML=index.email
            row.appendChild(td1);
            row.appendChild(td2);
            document.querySelector("#student_data>#real_table>tbody").append(row);
        }
        
    }
    $(document).ready(function(){
        $("#real_table").DataTable();
    });
}

window.onload = function() {
    $(document).ready(function(){
        $("#events_table").DataTable();
    });
  };



